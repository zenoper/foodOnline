from django import forms
from .models import Vendor, OpenHours
from accounts.validators import allow_only_images_validator

class VendorForm(forms.ModelForm):
    vendor_license = forms.FileField(widget=forms.FileInput(attrs={'class': 'btn btn-info'}), validators=[allow_only_images_validator])
    class Meta:
        model = Vendor
        fields = ['vendor_name', 'vendor_license']

class OpenHoursForm(forms.ModelForm):
    class Meta:
        model = OpenHours
        fields = ['day', 'from_hour', 'to_hour', 'is_closed']