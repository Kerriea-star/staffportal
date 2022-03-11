from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read only permissions are alllowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissiosn are only allowed to the staff
        return obj.name == request.user