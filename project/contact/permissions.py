from rest_framework.permissions import DjangoModelPermissions


# Using DjangoModelPermissions we can limit access by checking user permissions.

# Rights need only for CreateUpdateDelete actions.
class CUDModelPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': [],
        'OPTIONS': [],
        'HEAD': ['%(app_label)s.read_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
