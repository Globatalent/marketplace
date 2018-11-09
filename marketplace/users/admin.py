from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import (
    UserChangeForm as AuthUserChangeForm,
    UserCreationForm as AuthUserCreationForm,
)
from django.utils.translation import ugettext_lazy as _

from marketplace.users.models import User


class UserChangeForm(AuthUserChangeForm):
    class Meta(AuthUserChangeForm.Meta):
        model = User


class UserCreationForm(AuthUserCreationForm):
    error_message = AuthUserCreationForm.error_messages.update(
        {"duplicate_email": "This email has already been taken."}
    )

    class Meta(AuthUserCreationForm.Meta):
        model = User
        fields = ("email",)

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages["duplicate_email"])


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_email_verified",
                    "verification_code",
                    "restore_password_code",
                    "restore_password_code_requested_at",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Profile"), {"fields": ("first_name", "last_name", "following")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )
    list_display = ("email", "is_superuser", "date_joined")
    ordering = ("id",)
    search_fields = ("email",)
    autocomplete_fields = ["following"]
