from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to update their own profile"""

    def has_object_permission(self, request,  view, object):
        """Check if the users trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True

        return object.id == request.user.id