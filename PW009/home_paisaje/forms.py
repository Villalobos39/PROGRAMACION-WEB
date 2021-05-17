from django import forms

from .models import Paisajes

class LeadForm(forms.ModelForm):
    class Meta:
        model = Paisajes
        fields = "__all__"
       ## exclude = ["register_timestamp", "regidter_update"]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Paisajes
        fields = "__all__"
       ## exclude = ["register_timestamp", "regidter_update"]