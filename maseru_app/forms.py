from django import forms
from maseru_app.models import MaseruStaffModel


class StaffForms(forms.ModelForm):
    class Meta:
        model = MaseruStaffModel
        fields = '__all__'