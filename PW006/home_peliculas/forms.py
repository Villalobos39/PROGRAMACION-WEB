from django import forms

from home_peliculas.models import Pelis

class LeadForm(forms.ModelForm):
    class Meta:
        model = Pelis  
        fields = "__all__"
       ## exclude = [ ]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Pelis
        fields = "__all__"
        ## exclude = [""]