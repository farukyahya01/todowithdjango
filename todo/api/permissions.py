from rest_framework import permissions
#CUSTOM PERMISSION CLASSES

# VAR OLAN KULLANICI SADECE KENDİ OLUŞTURDUĞU TODOLARDA İŞLEM YAPABİLİR
class IsTodoRecordOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.user
        