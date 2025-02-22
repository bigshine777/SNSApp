from allauth.account.forms import SignupForm
from django import forms
from .models import CustomUser


class CustomSignupForm(SignupForm):
    icon = forms.ImageField(required=False, label="アイコン")

    class Meta:
        model = CustomUser
        fields = ("username", "email", "icon", "password1", "password2")

    def save(self, request):
        user = super().save(request)
        if self.cleaned_data["icon"]:
            user.icon = self.cleaned_data["icon"]
            user.save()

        return user
