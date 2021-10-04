from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from project.settings.production import DEBUG
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from ..models import Contact
from ..serializers import ContactSerializer


class SettingsTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_populate_data(self):
        self.assertEqual(DEBUG, False)


class ContactsTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        self.client = APIClient()
        permission_view = Permission.objects.get(name='Can view contact')
        permission_add = Permission.objects.get(name='Can add contact')
        permission_delete = Permission.objects.get(name='Can delete contact')
        permission_change = Permission.objects.get(name='Can change contact')
        self.test_user_read = User.objects.create_user(username='test_user_read',
                                                       email='test_user_read@foo.com',
                                                       password='test_user_read$$')
        self.test_user_read.user_permissions.add(permission_view)
        self.test_user_read_token = Token.objects.create(user=self.test_user_read)
        self.test_user_read_token.save()
        self.test_user_read_add = User.objects.create_user(username='test_user_read_add',
                                                           email='test_user_read_add@foo.com',
                                                           password='test_user_read_add')
        self.test_user_read_add_token = Token.objects.create(user=self.test_user_read_add)
        self.test_user_read_add.user_permissions.add(permission_view)
        self.test_user_read_add.user_permissions.add(permission_add)
        self.test_user_read_add_token.save()
        self.test_user_read_add_delete = User.objects.create_user(username='user_read_add_delete',
                                                                  email='user_read_add_delete@foo.com',
                                                                  password='test_user_read$$')
        self.test_user_read_add_delete.user_permissions.add(permission_view)
        self.test_user_read_add_delete.user_permissions.add(permission_add)
        self.test_user_read_add_delete.user_permissions.add(permission_delete)
        self.test_user_read_add_delete_token = Token.objects.create(user=self.test_user_read_add_delete)
        self.test_user_read_add_delete_token.save()

        self.test_user_read_add_delete_change = User.objects.create_user(username='test_user_read_add_delete_change',
                                                                         email='test_user_read_add_delete_change@foo.com',
                                                                         password='test_user_read_add_delete_change')
        self.test_user_read_add_delete_change.user_permissions.add(permission_view)
        self.test_user_read_add_delete_change.user_permissions.add(permission_add)
        self.test_user_read_add_delete_change.user_permissions.add(permission_delete)
        self.test_user_read_add_delete_change.user_permissions.add(permission_change)
        self.test_user_read_add_delete_change_token = Token.objects.create(user=self.test_user_read_add_delete_change)
        self.test_user_read_add_delete_change_token.save()

    def test_all_get_not_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_one_get_not_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION='')
        response = self.client.get(reverse('contact', kwargs={'pk': 256}))
        self.assertEqual(response.data['detail'], 'Authentication credentials were not provided.')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def all_logic(self):
        response = self.client.get(reverse('contacts'), format='json')
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        data = response.json()
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_contacts_read_permission_read(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_token.key)
        self.all_logic()

    def test_get_all_contacts__read_create_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_token.key)
        self.all_logic()

    def test_get_all_contacts__read_create_delete_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_delete_token.key)
        self.all_logic()

    def test_get_all_contacts__read_create_delete_update_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_delete_change_token.key)
        self.all_logic()

    def one_logic(self):
        response = self.client.get(reverse('contact', kwargs={'pk': 256}))
        contact = Contact.objects.get(pk=256)
        serializer = ContactSerializer(contact, many=False)
        data = response.json()
        self.assertEqual(data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_contact__read_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_token.key)
        self.one_logic()

    def test_get_one_contact__read_create_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_token.key)
        self.one_logic()

    def test_get_one_contact__read_create_delete_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_delete_token.key)
        self.one_logic()

    def test_get_one_contact__read_create_delete_update_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_delete_change_token.key)
        self.one_logic()

    def patch_contact(self):
        response = self.client.get(reverse('contact', kwargs={'pk': 256}))
        data = response.json()
        data['name'] = 'Patched contact'
        response_patch = self.client.patch(reverse('contact', kwargs={'pk': 256}), data=data)
        response_patched = self.client.get(reverse('contact', kwargs={'pk': 256}))
        return response_patch, data, response_patched

    def test_patch_one_contact__read_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_token.key)
        response_patch, data, response_patched = self.patch_contact()
        self.assertEqual(response_patch.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(data, response_patched.json())

    def test_patch_one_contact__read_create_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_token.key)
        response_patch, data, response_patched = self.patch_contact()
        self.assertEqual(response_patch.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(data, response_patched.json())

    def test_patch_one_contact__read_create_delete_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_delete_token.key)
        response_patch, data, response_patched = self.patch_contact()
        self.assertEqual(response_patch.status_code, status.HTTP_403_FORBIDDEN)
        self.assertNotEqual(data, response_patched.json())

    def test_patch_one_contact__read_create_delete_update_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_delete_change_token.key)
        response_patch, data, response_patched = self.patch_contact()
        self.assertEqual(response_patch.status_code, status.HTTP_200_OK)
        self.assertEqual(data, response_patched.json())

    def create_contact(self):
        data = {'name': 'new_created', 'email': 'new_created@new_created.ru'}
        response_create = self.client.post(reverse('contacts'), data=data)
        # print('response_create.json()', response_create.json())
        response_get = None
        if 'id' in response_create.json():
            response_get = self.client.get(reverse('contact', kwargs={'pk': response_create.json()['id']}))
        return response_create, data, response_get

    def test_create_one_contact__read_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_token.key)
        response_patch, data, response_get = self.create_contact()
        self.assertEqual(response_patch.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_one_contact__read_create_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_token.key)
        response_patch, data, response_get = self.create_contact()
        self.assertEqual(response_patch.status_code, status.HTTP_201_CREATED)

    def test_create_one_contact__read_create_delete_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_delete_token.key)
        response_patch, data, response_get = self.create_contact()
        self.assertEqual(response_patch.status_code, status.HTTP_201_CREATED)

    def test_create_one_contact__read_create_delete_update_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_delete_change_token.key)
        response_patch, data, response_get = self.create_contact()
        self.assertEqual(response_patch.status_code, status.HTTP_201_CREATED)

    def delete_contact(self):
        response_delete = self.client.delete(reverse('contact', kwargs={'pk': 256}))
        return response_delete

    def test_delete_one_contact__read_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_token.key)
        response_delete = self.delete_contact()
        self.assertEqual(response_delete.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_one_contact__read_create_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_token.key)
        response_delete = self.delete_contact()
        self.assertEqual(response_delete.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_one_contact__read_create_delete_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_delete_token.key)
        response_delete = self.delete_contact()
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_one_contact__read_create_delete_update_permission(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.test_user_read_add_delete_change_token.key)
        response_delete = self.delete_contact()
        self.assertEqual(response_delete.status_code, status.HTTP_204_NO_CONTENT)
