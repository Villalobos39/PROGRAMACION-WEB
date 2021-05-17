from django import forms

from home_name.models import Alumnos

class LeadForm(forms.ModelForm):
    class Meta:
        model = Alumnos  
        fields = "__all__"
       ## exclude = [ ]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Alumnos
        fields = "__all__"
        ## exclude = [""]