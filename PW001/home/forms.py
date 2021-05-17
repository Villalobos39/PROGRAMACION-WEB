from django import forms

from .models import OnePiece

class LeadForm(forms.ModelForm):
    class Meta:
        model = OnePiece
        fields = "__all__"
       ## exclude = ["register_timestamp", "regidter_update"]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = OnePiece
        fields = "__all__"
        ## exclude = ["register_timestamp", "regidter_update"]