from django import forms

from home_comida.models import Comida

class LeadForm(forms.ModelForm):
    class Meta:
        model = Comida  
        fields = "__all__"
       ## exclude = [ ]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Comida
        fields = "__all__"
        ## exclude = [""]