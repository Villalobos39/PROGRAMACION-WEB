from django import forms

from home_bebidas.models import Bebida

class LeadForm(forms.ModelForm):
    class Meta:
        model = Bebida  
        fields = "__all__"
       ## exclude = [ ]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = "__all__"
        ## exclude = [""]