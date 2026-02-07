from rest_framework import permissions
from .models import Fundraiser

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user ## created custom permission class
    
class IsFundraiserSoftDeleted(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        fundraiser_id = request.data.get('fundraiser')
        if not fundraiser_id:
            return False

        return Fundraiser.objects.filter(pk=fundraiser_id, is_deleted=False).exists()


    