from django import forms
from django.contrib.auth import get_user_model, authenticate
from . models import StudentProfile

User = get_user_model()

class RegistrationForm(forms.ModelForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('This email has been taken')
        return email
        
    def clean_password_confirm(self):
        password = self.cleaned_data['password']
        password_confirm = self.cleaned_data['password_confirm']
        if password != password_confirm:
            raise forms.ValidationError('The password did not match')
        return password_confirm

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password_confirm'
        ]

class LogInForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid credentials')
        return super().clean(*args, **kwargs)
    

class StudentProfileForm(forms.ModelForm):
    
    class Meta:
        model = StudentProfile
        fields = ["profile_pic", "matric_no", "telephone", "school", "level",  "department", "gender"]
