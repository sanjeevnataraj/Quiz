from django import forms
from .models import User


class RegistrationPageForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]

    def __init__(self,*args,**kwrags):
        super(RegistrationPageForm,self).__init__(*args,**kwrags)
        self.fields['password'] = forms.CharField(label="Password", widget=forms.PasswordInput)
        self.fields['password1'] = forms.CharField(label="Password", widget=forms.PasswordInput)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter the Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter the Password'
        self.fields['password1'].widget.attrs['placeholder'] = 'Re-enter the Password '
        self.fields['email'].widget.attrs['placeholder'] = 'Enter the Email'


    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        print(username,password,password1,email)
        
        if password != password1:
            print('***')
            self.add_error('password1', 'Password Does not Matched')
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'username already exists')
        if User.objects.filter(email=email).exists():
            self.add_error('email', 'Email already exists. Try Sign-in.')
 