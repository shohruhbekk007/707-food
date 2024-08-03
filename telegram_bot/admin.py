from django.contrib import admin
from .models import ComandStart, Taomlar, Menyu
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Menyu)
class MenyuAdmin(admin.ModelAdmin):
    list_display = ('taom_turi',)

@admin.register(Taomlar)
class TaomAdmin(admin.ModelAdmin):
    list_display = ('nomi', 'narxi')


@admin.register(ComandStart)
class MenyuAdmin(admin.ModelAdmin):
    list_display = ('title',)



# Register your models here.
