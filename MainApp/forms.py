from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Message

class CustomerCreationForm(UserCreationForm):
    bank_account_no = forms.CharField(max_length=20, required=True, label="bank_account_no", widget=forms.TextInput(attrs={"class": "form-control"}))
    phone_no = forms.CharField(max_length=15, required=True, label="phone_no", widget=forms.TextInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=50, label="First Name", widget=forms.TextInput(attrs={"class": "form-control"}) )
    last_name = forms.CharField(max_length=50, label="Last Name", widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(max_length=50, label="Username", widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=50, label="Email", widget=forms.EmailInput(attrs={"class": "form-control"}))
    
    def save(self, commit=True):
        user = super().save(commit=False)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        bank_account_no = self.cleaned_data['bank_account_no']
        phone_no = self.cleaned_data['phone_no']
        if commit:
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            UserProfile.objects.create(user=user, bank_account_no=bank_account_no, phone_no=phone_no )
        return user


class AddMoneyForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['balance']


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = UserProfile
        fields = ['phone_no']  # Fields to be updated

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = self.instance.user.first_name
        self.fields['last_name'].initial = self.instance.user.last_name
        self.fields['email'].initial = self.instance.user.email

    def save(self, commit=True):
        user = self.instance.user
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            return super(ProfileUpdateForm, self).save(commit=commit)


class MoneyTransferForm(forms.Form):
    receiver_username = forms.CharField(max_length=150, required=True)
    receiver_email = forms.EmailField(required=True)
    receiver_bank_account_no = forms.CharField(max_length=150, required=True)
    amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    sender_bank_account_no = forms.CharField(max_length=150, required=True)
    sender_username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 8}),
        }