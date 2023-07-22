from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff :
            if user.has_perm('api.view_food'):      # 'appName.verb_modelName'
                return True
        return False


# Below permission is equivalent to 'permissions.IsAdminUser' permission
class IsStaffMemberPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        return super().has_permission(request,view)


class IsStaffEditorPermission2(permissions.DjangoModelPermissions):
    # Using the params_map we can specify which methods should be allowed for which models.
    # app_label and model_name in params_map will be automatically rendered.
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        # when a GET request is made, the DjangoModelPermissions class will check
        # if the user making the request has the permission 'appName.view_modelName'.
        # If the user has the permission, they will be granted access to the object;
        # otherwise, the request will be denied.
        # !!! Here, if the request method is 'GET', then class won't check any other
        # permission related to other request methods('POST', 'PUT', ...).
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class IsStaffEditorGetPermission(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': [],
        'PUT': [],
        'PATCH': [],
        'DELETE': [],
    }