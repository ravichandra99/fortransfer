from django import forms
from transfer.models import JustBase


class BaseForm(forms.ModelForm):
	class Meta:
		model = JustBase
		fields = '__all__'

class OTPAuthenticationForm(forms.Form):
    OTP = forms.CharField(required=False, widget=forms.PasswordInput)
    sotp = forms.CharField(required=False, widget=forms.HiddenInput)

    
