from .models import User
from django import forms


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm_password')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password didn't match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UpdateForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email', 'image']