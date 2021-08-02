from django.forms import ModelForm
from .models import Employee, Utilisateur

class UtilisateurForms(ModelForm):
    class Meta:
        model = Utilisateur
        fields = ["profile_pic"]

class ATSFomrs(ModelForm):
    class Meta:
        model = Employee
        fields = ["image"]