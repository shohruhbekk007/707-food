from django.contrib import admin
from .models import ComandStart, Taomlar, Menyu, Users
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


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', "phone_number")

# Register your models here.
