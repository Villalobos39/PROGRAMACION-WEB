from django import forms

from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        exclude = ["register_timestamp", "regidter_update"]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        exclude = ["register_timestamp", "regidter_update"]