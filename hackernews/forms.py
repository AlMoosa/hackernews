from django.contrib.auth.forms import UserCreationForm
from hackernews.models import User, Profile
from django.forms import ModelForm


class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username', 'fullname', 'password1','password2',
        )


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            'avatar', 'info', 'age', 'gender'
        )


