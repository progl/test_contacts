from rest_framework import serializers
from .models import Contact


# Serializers define the API representation.
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'email', ]
