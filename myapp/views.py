from django.core import paginator
from .forms import ATSFomrs, UtilisateurForms
from .models import Conge, Employee, Prime, Utilisateur ,Paie
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate ,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db.models import Q
from itertools import chain
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from datetime import date
from django.core.paginator import Paginator
from datetime import datetime
from .helper import render_to_pdf #created in step 4

# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        messages.add_message(request, messages.SUCCESS, "Soyez le bienvenue !")
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.add_message(request, messages.WARNING, "Nom d'utilisateur ou mot de passe est incorrect !")
    return render(request,'login.html')

@login_required
def Logout(request):
    logout(request)
    return redirect('/login')

@login_required
def home(request):
    return render(request,'home.html')

@login_required
def UsersView(request):
    search_post = request.GET.get('search') 
    if search_post:
        by_name = Utilisateur.objects.filter(Q(nom__icontains=search_post))
        by_prenon = Utilisateur.objects.filter(Q(prenom__icontains=search_post))
        by_func = Utilisateur.objects.filter(Q(fonction__icontains=search_post))
        users = list(chain(by_name,by_prenon,by_func))
    else : 
        users = Utilisateur.objects.all()
    num = 10
    paginator = Paginator(users,num)
    page_number = request.GET.get('page')
    if page_number == None :
        page_number = 1
    page_obj = paginator.get_page(page_number)
    is_paginated = (len(page_obj)==num)
    context = {'users':page_obj,'page_number':page_number,'is_paginated':is_paginated}
    return render(request,'users.html',context)

@login_required
def SuprimerUser(request,pk):
    try :
        user = Utilisateur.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.add_message(request, messages.WARNING, 'Operation indesirable')
        return redirect('/utilisateurs')
    user.delete()
    messages.add_message(request, messages.SUCCESS, 'Utilisateurs a etait supprimé.')
    return redirect('/utilisateurs')

@login_required
def EditeUser(request,pk):
    try:
        user = Utilisateur.objects.get(pk=pk)
    except :
        messages.add_message(request, messages.WARNING, 'Operation indesirable')
        return redirect('/utilisateurs')
    form = UtilisateurForms(instance=user)

    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:

            user.nom = request.POST['nom']
            user.prenom = request.POST['prenom']
            user.username= request.POST['username']
            user.numero = request.POST['numero']
            if request.POST['fonction'] == 'A':
                user.fonction = "A"
                user.is_admin = True
                user.is_staff = True
                user.is_superuser = True
            elif request.POST['fonction'] == 'C':
                user.fonction = "C"
                user.is_admin = False
                user.is_staff = False
                user.is_superuser = False
            else : 
                messages.add_message(request, messages.WARNING, 'Operation indesirable, veuillez choisir une fonction')
                return redirect('/utilisateurs')
                if request.POST['password'] != " " :
                    print('pas')
                    user.set_password(request.POST['password'])
            form = UtilisateurForms(request.POST,request.FILES,instance=user)
            if form.is_valid():
                form.save()
            user.save()
            return redirect('/utilisateurs')
        else : 
            messages.add_message(request, messages.WARNING, 'Operation indesirable, mot de passe incorrect')
            return redirect('/utilisateurs')
    context = {"user":user,"form":form}
    return render(request,'modifierUtilisateurs.html',context)



@login_required
def AjoutUtilisateurs(request):
    form = UtilisateurForms()
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            if request.POST['fonction'] == 'A':
                try : 
                    user = Utilisateur.objects.create_superuser(
                        email = request.POST['email'],
                        password = request.POST['password'],
                        username=request.POST['username']

                    )
                except ObjectDoesNotExist:
                    messages.add_message(request, messages.WARNING, 'Operation indesirable.')
                    return redirect('/utilisateurs')
            elif request.POST['fonction'] == 'C':
                try : 
                    user = Utilisateur.objects.create_user(
                        email = request.POST['email'],
                        password = request.POST['password'],
                        username=request.POST['username']
                    )
                except ObjectDoesNotExist:
                    messages.add_message(request, messages.WARNING, 'Operation indesirable.')
                    return redirect('/utilisateurs')
            else : 
                messages.add_message(request, messages.WARNING, 'Operation indesirable, mot de passe incorrect')
                return redirect('/utilisateurs')
            user.nom = request.POST['nom']
            user.prenom = request.POST['prenom']
            user.numero = request.POST['numero']
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Utilisateurs créé.')
            form = UtilisateurForms(request.POST,request.FILES,instance=user)
            print(form.is_valid())
            if form.is_valid():
                form.save()
            
            return redirect('/utilisateurs')
        else : 
            return HttpResponse('non valid')
    context = {'form':form}       
    return render(request,'ajoutUtilisateurs.html',context)


# employee
@login_required
def EmployeeView(request):
    search_post = request.GET.get('search') 
    if search_post:
        by_name = Employee.objects.filter(Q(nom__icontains=search_post),Xfonctionnair=False)
        by_prenon = Employee.objects.filter(Q(prenom__icontains=search_post),Xfonctionnair=False)
        by_func = Employee.objects.filter(Q(function__icontains=search_post),Xfonctionnair=False)
        employees = list(chain(by_name,by_prenon,by_func))
    else : 
        try : 
            employees = Employee.objects.filter(Xfonctionnair=False)
        except ObjectDoesNotExist:
            messages.add_message(request, messages.WARNING, 'Operation indesirable.') 
            return redirect('/')
    num = 10
    paginator = Paginator(employees,num)
    page_number = request.GET.get('page')
    if page_number == None :
        page_number = 1
    page_obj = paginator.get_page(page_number)
    is_paginated = (len(page_obj)==num)
    fonctionnaire = False
    context = {'employees':page_obj,'page_number':page_number,'is_paginated':is_paginated,'fonctionnaire':fonctionnaire}
    return render(request,"employee.html",context)

def XfonctionnaireView(request):
    search_post = request.GET.get('search') 
    if search_post:
        by_name = Employee.objects.filter(Q(nom__icontains=search_post),Xfonctionnair=True)
        by_prenon = Employee.objects.filter(Q(prenom__icontains=search_post),Xfonctionnair=True)
        by_func = Employee.objects.filter(Q(function__icontains=search_post),Xfonctionnair=True)
        employees = list(chain(by_name,by_prenon,by_func))
    else : 
        try : 
            employees = Employee.objects.filter(Xfonctionnair=True)
        except ObjectDoesNotExist:
            messages.add_message(request, messages.WARNING, 'Operation indesirable.') 
            return redirect('/')
    num = 10
    paginator = Paginator(employees,num)
    page_number = request.GET.get('page')
    if page_number == None :
        page_number = 1
    page_obj = paginator.get_page(page_number)
    is_paginated = (len(page_obj)==num)
    fonctionnaire = True
    context = {'employees':page_obj,'page_number':page_number,'is_paginated':is_paginated,'fonctionnaire':fonctionnaire}
    return render(request,"employee.html",context)


@login_required
def ajoutatsView(request):
    if request.method == 'POST':
        employee = Employee.objects.create(
            nom = request.POST["nom"],
            prenom = request.POST["prenom"],
            function = request.POST['function'],
            numero = request.POST['numero'],
            naissance = request.POST['naissance'],
            adresse = request.POST['adresse'],
            email = request.POST['email'],
            situation = request.POST['situation'],
            date_joined = request.POST['date_joined'],
            date_recretment = request.POST['date_recretment'],
            Nenfant= request.POST['Nenfant'],
            nature = request.POST['nature'],
            numccp = request.POST['numccp'],
            numss = request.POST['numss']
        ) 
        paie = Paie.objects.create(employee=employee) 
        form = ATSFomrs(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.save()
        messages.add_message(request, messages.SUCCESS, 'ATS ajouté') 
        return redirect('/ats')
    form = ATSFomrs()
    context = {"form":form}
    return render(request,"ajoutats.html",context)

@login_required
def supprimeratsView(request,pk):
    try : 
        employee = Employee.objects.get(pk=pk)
    except: 
        messages.add_message(request, messages.WARNING, 'Operation indesirable ') 
        return redirect('/ats')
    employee.Xfonctionnair =True
    employee.save()
    messages.add_message(request, messages.SUCCESS, 'ATS supprimé.') 
    return redirect('/ats')

def suppatsView(request,pk):
    try : 
        employee = Employee.objects.get(pk=pk)
    except: 
        messages.add_message(request, messages.WARNING, 'Operation indesirable ') 
        return redirect('/ats')
    employee.delete()
    messages.add_message(request, messages.SUCCESS, 'ATS supprimé defenitivement.')
    return redirect('/ats')

@login_required
def editeatsView(request,pk):
    try : 
        employee = Employee.objects.get(pk=pk)
    except : 
        messages.add_message(request, messages.WARNING, 'Operation indesirable ') 
        return redirect('/ats')

    if request.method == 'POST':
        employee.nom = request.POST["nom"]
        employee.prenom = request.POST["prenom"]
        employee.function = request.POST['function']
        employee.numero = request.POST['numero']
        employee.naissance = request.POST['naissance']
        employee.adresse = request.POST['adresse']
        employee.email = request.POST['email']
        employee.situation = request.POST['situation']
        employee.Nenfant= request.POST['Nenfant']
        employee.nature = request.POST['nature']
        employee.numccp = request.POST['numccp']
        employee.numss = request.POST['numss']
        employee.date_recretment = request.POST['date_recretment']
        employee.date_joined = request.POST['date_joined']
        employee.save()
        form = ATSFomrs(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.save()
        messages.add_message(request, messages.SUCCESS, 'ATS modifié') 
        return redirect('/ats')
    form = ATSFomrs(instance=employee)
    context = {'employee':employee,'form':form}
    return render(request, 'editats.html', context)

def AjoutPaie(request,pk):
    employee = Employee.objects.get(pk=pk)
    paies = Paie.objects.filter(employee=employee).order_by('-created_at')
    paie = paies.first()
    if request.method == 'POST':
        paie = Paie.objects.create(employee=employee)
        paie.filiere = request.POST['filiere']
        paie.grade = request.POST['grade']
        paie.corps = request.POST['corps']
        paie.categorie = request.POST['categorie']
        paie.indice = request.POST['indice']
        paie.salaire = request.POST['salaire']
        paie.poste_occupe = request.POST['poste_occupe']
        paie.indiciaire = request.POST['indiciaire']
        paie.categorie_promo = request.POST['categorie_promo']
        paie.groupe = request.POST['groupe']
        paie.indice_minimale = request.POST['indice_minimale']
        paie.indice_echelon = request.POST['indice_echelon']
        paie.echelon = request.POST['echelon']
        paie.grille = request.POST['grille']
        paie.indemite_sac = request.POST['indemite_sac']
        paie.indemite_stc = request.POST['indemite_stc']
        paie.securite = request.POST['securite']
        paie.salaire_brut = request.POST['salaire_brut']
        paie.indimnite_transport = request.POST['indimnite_transport']
        paie.indimnite_panier = request.POST['indimnite_panier']
        paie.irg = request.POST['irg']
        paie.totale_brute_imposable_irg = request.POST['totale_brute_imposable_irg']
        paie.allocation_familiale = request.POST['allocation_familiale']
        paie.totale = request.POST['totale']
        paie.nombre_travaille = request.POST['nombre_travaille']
        paie.nombre_absence = request.POST['nombre_absence']
        paie.salaire_net = request.POST['salaire_net']
        paie.save()
        messages.add_message(request, messages.SUCCESS, 'Operation validé.') 
        return redirect('/ats')
    else : 
        messages.add_message(request, messages.WARNING, 'Operation non validé') 
    context = {'paie':paie}
    return render(request,'paie.html',context)



def congeView(request,pk):
    try : 
        employee = Employee.objects.get(pk=pk,Xfonctionnair=False)
    except ObjectDoesNotExist : 
        messages.add_message(request, messages.WARNING, 'Operation validé.') 
        return redirect('/ats')
    if request.method == "POST" : 
        conge = Conge.objects.create(employee=employee)
        conge.debut = request.POST['debut']
        conge.fin = request.POST['fin']
        conge.nombre = request.POST['nombre']
        conge.nature = request.POST['nature']
        conge.retour = request.POST['retour']
        conge.commentaire = request.POST['commentaire']
        conge.save()
        print(conge)
        messages.add_message(request, messages.SUCCESS, 'Congé ajouté.')
        return redirect(f"/pdf/conge/{conge.employee.id}")
    context = {"employee":employee}
    return render(request,'congeform.html',context)

def titreConeView(request,pk):
    employee = Employee.objects.get(pk=pk)
    if employee.Xfonctionnair :
        messages.add_message(request, messages.WARNING, 'Operation non validé.') 
        return redirect('/ats') 
    try : 
        conges = Conge.objects.filter(employee=employee).order_by('-created_at')
        conge = conges.first()
    except ObjectDoesNotExist : 
        messages.add_message(request, messages.WARNING, 'Operation non validé.') 
        return redirect('/ats')
    return redirect(f"/pdf/conge/{conge.employee.id}")

def Congepdf(request,pk):
    employee = Employee.objects.get(pk=pk)
    conges = Conge.objects.filter(employee=employee).order_by('-created_at')
    conge = conges.first()
    fdate = date.today().strftime('%d/%m/%Y')
    employee = conge.employee
    if employee.Xfonctionnair :
        messages.add_message(request, messages.WARNING, 'ATS dans la liste des Xfonctionnaire.')
        return redirect('/ats')
    context = {'employee':employee,"user":request.user,"conge":conge,"current":fdate}
    pdf = render_to_pdf('pdf/conge.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"conge/{employee.nom}&{employee.prenom}%s.pdf" %("12341231")
        content = "inline; filename=%s" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


def primeRendementView(request,pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        prime = Prime.objects.create(employee=employee,
        note_prime = request.POST['note_prime'],
        commentaire = request.POST['commentaire'],
        trimestre = request.POST['trimestre'],
        date = request.POST['date'],
        salaire_principal = request.POST['sp'],
        salaire_brut_mensulle = request.POST['A'],
        salaire_brut_trimi = request.POST['B'],
        securite_sociale = request.POST['C'],
        base_impot = request.POST['D'],
        irg = request.POST['E'],
        prime_net = request.POST['H']
        )
        return redirect('/ats')
    paies = Paie.objects.filter(employee=employee).order_by('-created_at')
    paie = paies.first()
    sp = paie.securite
    context = {
        'employee':employee,
        'sp':round(sp,2),
        'A': 0.0,
        'B':0.0,
        'C':0.0,
        'D':0.0,
        'E':0,
        'H':0.0,
    }
    return render(request,'primeRendement.html',context)


def travaillePDF(request,pk):
    template = get_template('pdf/attestation.html')
    employee = Employee.objects.get(pk=pk)
    fdate = date.today().strftime('%d/%m/%Y')
    context = {'employee':employee,"user":request.user ,"current":fdate }
    html = template.render(context)
    pdf = render_to_pdf('pdf/attestation.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"attestationDeTravaille/{employee.nom}&{employee.prenom}%s.pdf" %("12341231")
        content = "inline; filename=%s" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")

def FicheDePaieView(request,pk):
    employee = Employee.objects.get(pk=pk)
    paies = Paie.objects.filter(employee=employee).order_by('-created_at')
    paie = paies.first()
    fdate = date.today().strftime('%d/%m/%Y')
    currentYear = datetime.now().year
    currentMonth = datetime.now().month
    securite = paie.securite * 9 /100
    totale = securite + paie.irg
    print(currentMonth)
    context = {"totale":round(totale, 2),"securite":round(securite,2),'employee':employee,"user":request.user ,"current":fdate,'month':currentMonth,'year':currentYear,'paie':paie }
    pdf = render_to_pdf('pdf/paie.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = f"FicheDePaie/{employee.nom}&{employee.prenom}%s.pdf" %("12341231")
        content = "inline; filename=%s" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename=%s" %(filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")

def HistoriqueView(request,pk):
    employee = Employee.objects.filter(pk=pk)
    conges = Conge.objects.filter(employee=employee).order_by('-created_at')
    paies = Paie.objects.filter(employee=employee).order_by('-created_at')
    primes = Prime.objects.filter(employee=employee).order_by('-created_at')
    num = 10
    #conges
    Congepaginator = Paginator(conges,num)
    page_number = request.GET.get('page')
    if page_number == None :
        page_number = 1
    congesList = Congepaginator.get_page(page_number)
    Conge_is_paginated = (len(congesList)==num)
    #paies
    Paiepaginator = Paginator(paies,num)
    page_number = request.GET.get('page')
    if page_number == None :
        page_number = 1
    PaiesList = Paiepaginator.get_page(page_number)
    Paie_is_paginated = (len(PaiesList)==num)
    #prime 
    Primepaginator = Paginator(primes,num)
    page_number = request.GET.get('page')
    if page_number == None :
        page_number = 1
    PrimeList = Primepaginator.get_page(page_number)
    Prime_is_paginated = (len(PrimeList)==num)
    context = {'paies':PaiesList,'conges':congesList,
        'primes':PrimeList,'Prime_is_paginated':Prime_is_paginated,
        'Paie_is_paginated':Paie_is_paginated,
        'Conge_is_paginated':Conge_is_paginated
        }
    return render(request,'historique.html',context)
