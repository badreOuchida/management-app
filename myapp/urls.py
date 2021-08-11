from django.urls import path
from .views import *

urlpatterns = [
    path("login",login,name="login"),
    path('',home,name="home"),
    path('utilisateurs',UsersView,name="users"),
    path('ajoutUtilisateur',AjoutUtilisateurs,name="ajout"),
    path('supprimeruser/<int:pk>',SuprimerUser,name="supprimer"),
    path("edite/<int:pk>",EditeUser,name="edite"),
    path('logout',Logout,name="logout"),
    path('ats',EmployeeView,name="ats"),
    path('ajoutats',ajoutatsView,name="ajoutats"),
    path('supprimerats/<int:pk>',supprimeratsView,name="supprimerats"),
    path('editats/<int:pk>',editeatsView,name="editats"),
    path('ajoutpaie/<int:pk>',AjoutPaie,name="ajoutpaie"),
    path('conge/<int:pk>',congeView,name="conge"),
    path('pdf/conge/<int:pk>',Congepdf,name="pdfconge"),
    path('prime/<int:pk>',primeRendementView,name="prime"),
    path('pdf/attestation/<int:pk>',travaillePDF,name="attestation"),
    path('Xfonctionnaire',XfonctionnaireView,name="Xfonctionnaire"),
    path('suppats/<int:pk>',suppatsView,name="suppats"),
    path('titreConge/<int:pk>',titreConeView,name="titreConge")
]
