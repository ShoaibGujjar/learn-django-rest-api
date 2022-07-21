
from rest_framework import permissions
from .permission import IsStaffEditorPermission
from rest_framework.response import Response


class StaffEditorPermissionMixin():
    permissions_classes=[
        permissions.IsAdminUser,
        IsStaffEditorPermission,
    ]

class UserQuerySetMixin():
    user_field='user'
    allow_staff_view=False
    def get_queryset(self,*args,**kwargs):
        user=self.request.user
        lookup_data={}
        lookup_data[self.user_field]=user
        qs=super().get_queryset(*args,**kwargs)
        if self.allow_staff_view and user.is_staff:
            return qs
        return qs.filter(**lookup_data)
    

    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     search = self.request.GET.get('user', None)
    #     queryset = queryset.filter(engineer=self.request.user)
    #     if search:
    #         queryset = queryset.filter(
    #             Q(project_title__icontains=search) |
    #             Q(category__title__icontains=search)
    #         ).distinct()
    #     return queryset