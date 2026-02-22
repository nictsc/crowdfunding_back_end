from rest_framework import permissions
from .models import Fundraiser

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        ## Allow safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user ## created custom permission class
    
class IsFundraiserSoftDeleted(permissions.BasePermission):
    def has_permission(self, request, view):
        ## Allow safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        fundraiser_id = request.data.get('fundraiser')
        if not fundraiser_id:
            return False

        return Fundraiser.objects.filter(pk=fundraiser_id, is_deleted=False).exists()

class IsEndUserActiveAndNotSoftDeleted(permissions.BasePermission):
    def has_permission(self, request, view):
        ## Allow safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        ## For POST, PUT, PATCH, DELETE methods, user must be authenticated
        if not request.user.is_authenticated:
            return False
        
        ## User must be active AND not soft-deleted
        return request.user.is_active and not request.user.is_deleted
   

    