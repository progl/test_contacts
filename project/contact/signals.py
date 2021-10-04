from .models import Contact
from django.db.models.signals import post_delete
from django.db.models.signals import post_migrate
from django.apps import AppConfig
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
import logging

logger = logging.getLogger('django')


def populate_table_data(model):
    model(**{'name': 'Aarica', 'email': 'Aarica@zorro.com'}).save()
    model(**{'name': 'Tiffay', 'email': 'Tiffay@zorro.com'}).save()
    model(**{'name': 'Shinita', 'email': 'Shinita@zorro.com'}).save()
    model(**{'name': 'Niki', 'email': 'Niki@zorro.com'}).save()
    model(**{'name': 'Janal', 'email': 'Janal@zorro.com'}).save()
    model(**{'name': 'Laneshia', 'email': 'Laneshia@zorro.com'}).save()
    model(**{'name': 'Osbaldo', 'email': 'Osbaldo@zorro.com'}).save()
    model(**{'name': 'Mercy', 'email': 'Mercy@zorro.com'}).save()
    model(**{'name': 'Arran', 'email': 'Arran@zorro.com'}).save()
    model(**{'name': 'Corey', 'email': 'Corey@zorro.com'}).save()
    model(**{'name': 'Yahayra', 'email': 'Yahayra@zorro.com'}).save()
    model(**{'name': 'Nataya', 'email': 'Nataya@zorro.com'}).save()
    model(**{'name': 'Autry', 'email': 'Autry@zorro.com'}).save()
    model(**{'name': 'Argelia', 'email': 'Argelia@zorro.com'}).save()
    model(**{'name': 'Bridger', 'email': 'Bridger@zorro.com'}).save()
    model(**{'name': 'Louise', 'email': 'Louise@zorro.com'}).save()
    model(**{'name': 'Lacara', 'email': 'Lacara@zorro.com'}).save()
    model(**{'name': 'Musa', 'email': 'Musa@zorro.com'}).save()
    model(**{'name': 'Marcas', 'email': 'Marcas@zorro.com'}).save()
    model(**{'name': 'Valissa', 'email': 'Valissa@zorro.com'}).save()
    model(**{'name': 'Casy', 'email': 'Casy@zorro.com'}).save()
    model(**{'name': 'Hope', 'email': 'Hope@zorro.com'}).save()
    model(**{'name': 'Mariella', 'email': 'Mariella@zorro.com'}).save()
    model(**{'name': 'Quillan', 'email': 'Quillan@zorro.com'}).save()
    model(**{'name': 'Shavawn', 'email': 'Shavawn@zorro.com'}).save()
    model(**{'name': 'Angelino', 'email': 'Angelino@zorro.com'}).save()
    model(**{'name': 'Missie', 'email': 'Missie@zorro.com'}).save()
    model(**{'name': 'Otisha', 'email': 'Otisha@zorro.com'}).save()
    model(**{'name': 'Joya', 'email': 'Joya@zorro.com'}).save()
    model(**{'name': 'Tiron', 'email': 'Tiron@zorro.com'}).save()
    model(**{'name': 'Catelin', 'email': 'Catelin@zorro.com'}).save()
    model(**{'name': 'Carols', 'email': 'Carols@zorro.com'}).save()
    model(**{'name': 'Lorine', 'email': 'Lorine@zorro.com'}).save()
    model(**{'name': 'Dovid', 'email': 'Dovid@zorro.com'}).save()
    model(**{'name': 'Rasheen', 'email': 'Rasheen@zorro.com'}).save()
    model(**{'name': 'Daunte', 'email': 'Daunte@zorro.com'}).save()
    model(**{'name': 'Salina', 'email': 'Salina@zorro.com'}).save()
    model(**{'name': 'Loyal', 'email': 'Loyal@zorro.com'}).save()
    model(**{'name': 'Jerell', 'email': 'Jerell@zorro.com'}).save()
    model(**{'name': 'Annalise', 'email': 'Annalise@zorro.com'}).save()
    model(**{'name': 'Angalena', 'email': 'Angalena@zorro.com'}).save()
    model(**{'name': 'Female', 'email': 'Female@zorro.com'}).save()
    model(**{'name': 'Katieann', 'email': 'Katieann@zorro.com'}).save()
    model(**{'name': 'Brendon', 'email': 'Brendon@zorro.com'}).save()
    model(**{'name': 'Alaine', 'email': 'Alaine@zorro.com'}).save()
    model(**{'name': 'Joao', 'email': 'Joao@zorro.com'}).save()
    model(**{'name': 'Susane', 'email': 'Susane@zorro.com'}).save()
    model(**{'name': 'Mattheu', 'email': 'Mattheu@zorro.com'}).save()
    model(**{'name': 'Nichlous', 'email': 'Nichlous@zorro.com'}).save()
    model(**{'name': 'Kehinde', 'email': 'Kehinde@zorro.com'}).save()
    model(**{'name': 'Sanita', 'email': 'Sanita@zorro.com'}).save()
    model(**{'name': 'Justyn', 'email': 'Justyn@zorro.com'}).save()
    model(**{'name': 'Ashton', 'email': 'Ashton@zorro.com'}).save()
    model(**{'name': 'Zachery', 'email': 'Zachery@zorro.com'}).save()
    model(**{'name': 'Erice', 'email': 'Erice@zorro.com'}).save()
    model(**{'name': 'Arletta', 'email': 'Arletta@zorro.com'}).save()
    model(**{'name': 'Mayer', 'email': 'Mayer@zorro.com'}).save()
    model(**{'name': 'Takima', 'email': 'Takima@zorro.com'}).save()
    model(**{'name': 'Clenton', 'email': 'Clenton@zorro.com'}).save()
    model(**{'name': 'Marshae', 'email': 'Marshae@zorro.com'}).save()
    model(**{'name': 'Marcus', 'email': 'Marcus@zorro.com'}).save()
    model(**{'name': 'Dat', 'email': 'Dat@zorro.com'}).save()
    model(**{'name': 'Marquail', 'email': 'Marquail@zorro.com'}).save()
    model(**{'name': 'Tore', 'email': 'Tore@zorro.com'}).save()
    model(**{'name': 'Tiffiny', 'email': 'Tiffiny@zorro.com'}).save()
    model(**{'name': 'Shoshana', 'email': 'Shoshana@zorro.com'}).save()
    model(**{'name': 'Deitra', 'email': 'Deitra@zorro.com'}).save()
    model(**{'name': 'Sirron', 'email': 'Sirron@zorro.com'}).save()
    model(**{'name': 'Abbigail', 'email': 'Abbigail@zorro.com'}).save()
    model(**{'name': 'Hiroko', 'email': 'Hiroko@zorro.com'}).save()
    model(**{'name': 'Sherrese', 'email': 'Sherrese@zorro.com'}).save()
    model(**{'name': 'Darrious', 'email': 'Darrious@zorro.com'}).save()
    model(**{'name': 'Alonna', 'email': 'Alonna@zorro.com'}).save()
    model(**{'name': 'Yuko', 'email': 'Yuko@zorro.com'}).save()
    model(**{'name': 'Kyoko', 'email': 'Kyoko@zorro.com'}).save()
    model(**{'name': 'Mariateresa', 'email': 'Mariateresa@zorro.com'}).save()
    model(**{'name': 'Bambi', 'email': 'Bambi@zorro.com'}).save()
    model(**{'name': 'Temisha', 'email': 'Temisha@zorro.com'}).save()
    model(**{'name': 'Cal', 'email': 'Cal@zorro.com'}).save()
    model(**{'name': 'Sharon', 'email': 'Sharon@zorro.com'}).save()
    model(**{'name': 'Lawrance', 'email': 'Lawrance@zorro.com'}).save()
    model(**{'name': 'Esmond', 'email': 'Esmond@zorro.com'}).save()
    model(**{'name': 'Dawnetta', 'email': 'Dawnetta@zorro.com'}).save()
    model(**{'name': 'Tedra', 'email': 'Tedra@zorro.com'}).save()
    model(**{'name': 'Kaila', 'email': 'Kaila@zorro.com'}).save()
    model(**{'name': 'Alisa', 'email': 'Alisa@zorro.com'}).save()
    model(**{'name': 'Tashunda', 'email': 'Tashunda@zorro.com'}).save()
    model(**{'name': 'Janesha', 'email': 'Janesha@zorro.com'}).save()
    model(**{'name': 'Kateri', 'email': 'Kateri@zorro.com'}).save()
    model(**{'name': 'Jahmai', 'email': 'Jahmai@zorro.com'}).save()
    model(**{'name': 'Maurisha', 'email': 'Maurisha@zorro.com'}).save()
    model(**{'name': 'Jerman', 'email': 'Jerman@zorro.com'}).save()
    model(**{'name': 'Merry', 'email': 'Merry@zorro.com'}).save()
    model(**{'name': 'Stacia', 'email': 'Stacia@zorro.com'}).save()
    model(**{'name': 'Mark', 'email': 'Mark@zorro.com'}).save()
    model(**{'name': 'Donica', 'email': 'Donica@zorro.com'}).save()
    model(**{'name': 'Waldo', 'email': 'Waldo@zorro.com'}).save()
    model(**{'name': 'Christien', 'email': 'Christien@zorro.com'}).save()
    model(**{'name': 'Jonnathan', 'email': 'Jonnathan@zorro.com'}).save()
    model(**{'name': 'Reyes', 'email': 'Reyes@zorro.com'}).save()
    permission_view = Permission.objects.get(name='Can view contact')
    permission_add = Permission.objects.get(name='Can add contact')
    permission_delete = Permission.objects.get(name='Can delete contact')
    permission_change = Permission.objects.get(name='Can change contact')

    if not User.objects.get(username='read'):
        user_read = User.objects.create_user(username='read',
                                             email='jlennon@beatles.com',
                                             password='read$$')
        user_read.user_permissions.add(permission_view)

    if not User.objects.get(username='read_create'):
        user_read_add = User.objects.create_user(username='read_create',
                                                 email='jlennon@beatles.com',
                                                 password='read_create$$')
        user_read_add.user_permissions.add(permission_view)
        user_read_add.user_permissions.add(permission_add)

    if not User.objects.get(username='read_create_delete'):
        user_read_add_delete = User.objects.create_user(username='read_create_delete',
                                                        email='jlennon@beatles.com',
                                                        password='read_create_delete$$')
        user_read_add_delete.user_permissions.add(permission_view)
        user_read_add_delete.user_permissions.add(permission_add)
        user_read_add_delete.user_permissions.add(permission_delete)

    if not User.objects.get(username='user_read_add_delete_change'):
        user_read_add_delete_change = User.objects.create_user(username='user_read_add_delete_change',
                                                               email='jlennon@beatles.com',
                                                               password='user_read_add_delete_change$$')
        user_read_add_delete_change.user_permissions.add(permission_view)
        user_read_add_delete_change.user_permissions.add(permission_add)
        user_read_add_delete_change.user_permissions.add(permission_delete)
        user_read_add_delete_change.user_permissions.add(permission_change)

    return True


# noinspection PyUnusedLocal
def auto_increment_start(sender, **kwargs):
    print('sender', sender, 'kw', kwargs)
    model = sender.get_model('contact')
    if not model.objects.exists():
        logger.debug(f"populating table data")
        from django.db import connection, transaction
        cursor = connection.cursor()
        # noinspection PyProtectedMember
        cursor.execute(f"""ALTER table {model._meta.db_table} AUTO_INCREMENT=256;""")
        populate_table_data(model)
        transaction.commit()


def on_delete_contact(sender, **kwargs):
    instance = kwargs.get('instance')
    logger.debug(f"on_delete_contact {instance.email} sending {instance.email in settings.EMAILS_FOR_WATCH}")
    email = None
    if instance.email in settings.EMAILS_FOR_WATCH:
        email = EmailMessage('Test', f'The email {instance.email} was deleted successefully! Thanks!',
                             to=[instance.email], )
        email.send()
    else:
        return False
    return email


post_delete.connect(on_delete_contact, sender=Contact, dispatch_uid='on_delete_contact')
post_migrate.connect(auto_increment_start, sender=AppConfig)
