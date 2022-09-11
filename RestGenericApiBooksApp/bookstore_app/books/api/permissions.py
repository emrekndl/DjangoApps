from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """ Only admin users can edit or create """

    def has_permission(self, request, view):
        """ Check if user is admin or request is safe """
        is_admin = super().has_permission(request, view)
        return request.method in permissions.SAFE_METHODS or is_admin


class IsCommenterOrReadOnly(permissions.BasePermission):
    """ Only comment creator can edit or create """

    def has_object_permission(self, request, view, obj):
        """ Check if user is commenter or request is safe """

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.commenter == request.user
