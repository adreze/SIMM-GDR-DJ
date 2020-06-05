from django.contrib import admin
from django.contrib.auth.models import User,Group
from import_export.admin import ImportExportModelAdmin
from library.resources import UserResource, GroupResource
from .models import Install
from .models import Reinstall
from .models import Replacement
from .models import StudentPC


@admin.register(Install)
class InstallAdmin(ImportExportModelAdmin):
    pass


@admin.register(Reinstall)
class ReinstallAdmin(ImportExportModelAdmin):
    pass


@admin.register(Replacement)
class ReplacementAdmin(ImportExportModelAdmin):
    pass


@admin.register(StudentPC)
class StudentPCAdmin(ImportExportModelAdmin):
    pass


admin.site.unregister(User)


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource


admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(ImportExportModelAdmin):
    resource_class = GroupResource
