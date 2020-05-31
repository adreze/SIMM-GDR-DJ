from django.contrib import admin

from .models import Install
from .models import Reinstall
from .models import Replacement
from .models import StudentPC


admin.site.register(Install)
admin.site.register(Reinstall)
admin.site.register(Replacement)
admin.site.register(StudentPC)