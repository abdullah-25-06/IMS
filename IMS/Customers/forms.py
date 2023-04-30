from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm as BaseUserChangeForm
from .models import User
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

    
class CustomLoginForm(AuthenticationForm):
    email= forms.EmailField(required=True)
    password= forms.PasswordInput()

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields.pop('username')

    def clean(self):
        super().clean()
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache= authenticate(request=self.request,username=email,password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Invalid email or password")
            elif not self.user_cache.is_active:
                raise forms.ValidationError("This account is inactive")
        return self.cleaned_data

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required= True)
    username = forms.CharField(required= True,max_length=30)

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    class Meta:
        model=get_user_model()
        fields=['username','password1','password2','email']



    
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm
from django.contrib.auth import get_user_model

class UserChangeForm(BaseUserChangeForm):
    def clean_email(self):
        super().clean()
        email = self.cleaned_data['email']
        if email and User.objects.all().exclude(username=email).filter(username=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email
    class Meta(BaseUserChangeForm.Meta):
        model = get_user_model()
        fields=['email']
    
    # class Meta(BaseUserChangeForm.Meta):
    #     model = get_user_model()
    #     fields = ('email', 'first_name', 'last_name')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['email'].disabled = True

    # def cleaned_email(self):
    #     email = self.cleaned_data.get('email')
    #     if email:
    #         email = email.lower()
    #     return email

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.email = self.cleaned_data['email'].lower()
    #     if commit:
    #         user.save()
    #     return user
