from django.contrib.auth.models import User
from django import forms

def add_attrs(field, attr_name, attr_new_val):
    existing_attr = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing_attr} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'],'Your username')
        add_placeholder(self.fields['email'],'Your email')
        add_placeholder(self.fields['first_name'],'Your first name')
        add_placeholder(self.fields['last_name'],'Your last name')



    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Your Password',
        }),
        error_messages={
            'required': 'Password must be empty'
        },
        help_text=(
            'Password must have at last one uppercase letter. '
            'one lowercase letter and one number. The length should be'
            'at least 8 characters '
        )
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Repeat your password',
        })
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
        ]
