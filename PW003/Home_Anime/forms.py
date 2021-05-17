from django import forms

from Home_Anime.models import Anime

class LeadForm(forms.ModelForm):
    class Meta:
        model = Anime  
        fields = "__all__"
       ## exclude = [ ]

class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = "__all__"
        ## exclude = [""]