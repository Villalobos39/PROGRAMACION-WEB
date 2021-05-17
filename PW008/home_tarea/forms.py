from django import forms

from .models import Tarea

class LeadForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = "__all__"
       ## exclude = ["register_timestamp", "regidter_update"]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = "__all__"
       ## exclude = ["register_timestamp", "regidter_update"]