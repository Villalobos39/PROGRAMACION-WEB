from django import forms

from .models import Musica

class LeadForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = "__all__"
       ## exclude = ["register_timestamp", "regidter_update"]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Musica
        fields = "__all__"
       ## exclude = ["register_timestamp", "regidter_update"]