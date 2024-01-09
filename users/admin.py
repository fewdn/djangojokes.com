from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from common.admin import DjangoJokesAdmin
from common.utils.admin import append_fields, move_fields, remove_fields
from django.utils.safestring import mark_safe
from django.urls import reverse
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialToken

# Register your models here.
CustomUser = get_user_model()

@admin.register(CustomUser)
class CustomUserAdmin(DjangoJokesAdmin, UserAdmin):
    model = CustomUser

    #add_fieldsets = UserAdmin.add_fieldsets + (
    #    ('Optional Fields', {
    #        'classes': ('wide',),
    #        'fields': ('email', 'first_name', 'last_name'),
    #    }),
    #)

    # List Attributes
    list_display = UserAdmin.list_display + ('is_superuser',)
    list_display_links = ('username', 'email', 'first_name', 'last_name')

    # Read-only fields
    readonly_fields = ['password_form']

    # Fields for editing existing user
    new_fields = ('dob', 'avatar')
    # Add new fields to "Personal info" fieldset
    append_fields(UserAdmin.fieldsets, 'Personal info', new_fields)
    # Move the email field to the unlabelled fieldset
    move_fields(UserAdmin.fieldsets, 'Personal info', None, ('email',))
    # Remove password field
    remove_fields(UserAdmin.fieldsets, None, ('password',))
    append_fields(UserAdmin.fieldsets, None, ('password_form',))

    # Fields for adding new user
    new_fields = ('email',)
    # Add new fields to unlabelled fieldset
    add_fieldsets = append_fields(UserAdmin.add_fieldsets, None, new_fields)
    
    # Add optional fields to new 'Optional Fields' fieldset
    optional_fields = ('first_name', 'last_name', 'dob')
    add_fieldsets = append_fields(UserAdmin.add_fieldsets, 'Optional Fields', optional_fields)

    # Add Save buttons to the top of the change user form
    def get_form(self, request, obj=None, **kwargs):
        self.save_on_top = obj is not None
        return super().get_form(request, obj, **kwargs)
    
    def password_form(self, obj):
        url = reverse('admin:auth_user_password_change', args=[obj.pk])
        return mark_safe(f'<a href="{url}">Change Password</a>')
    
    # Unregister these apps to remove Social Accounts section from Django Admin
    admin.site.unregister(SocialApp)
    admin.site.unregister(SocialAccount)
    admin.site.unregister(SocialToken)