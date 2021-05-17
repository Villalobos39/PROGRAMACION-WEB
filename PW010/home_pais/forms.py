from django import forms

from .models import Pais

class LeadForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = "__all__"
       ## exclude = ["register_timestamp", "regidter_update"]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Pais
        fields = "__all__"
       ## exclude = ["register_timestamp", "regidter_update"]