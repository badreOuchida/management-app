from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)

		user.fonction = 'C'
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.fonction = "A"
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


FONCTION = (
	('A','SOUS DIRECTEUR PERSONNEL'),
	('C','CHEF ATS')
)

class Utilisateur(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    numero = models.CharField(max_length=10)
    fonction = models.CharField(max_length=1,choices=FONCTION,null=False)
    profile_pic = models.ImageField(default="profile.jpg", null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
	    return self.username

	# For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, obj=None):
	    return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
	    return True



FONCTION2 = (
    ('R','rien'),
    ('D',"directeur"),
    ('DA','directeur adjoint'),
    ('SD','sous-directeur'),
    ('SDF','sous-directeur de finances')
)

SITUATION_FAMILIALE = (
    ('C','celibataire'),
    ('M','marié'),
    ('D',"devorcé")
)

NATURE = (
    ('S','stagiaire'),
    ('F','fonctionnaire')
)


MOTIF = (
    ('N','None'),
    ('DE','Décédé'),
    ('M','Mutation'),
    ('DI','Dimensionné'),
    ('R','Retraité')
)

DECISION = (
    ('N','None'),
    ('A','Automatique'),
    ('C','Commission')
)

ALERT = (
    ('0','0'),
    ('1',"1 an"),
    ('2','2 ans'),
    ('3','3 ans'),
    ('4','4 ans'),
    ('5','5 ans'),
    ('6','6 ans'),
)

class Employee(models.Model):
    image = models.ImageField(default="profile.jpg", null=True, blank=True)
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    function=models.CharField(choices=FONCTION2 , max_length=3,null=True)
    numero =models.CharField(max_length=10,null=True)
    naissance=models.DateField()
    adresse = models.CharField(max_length=200,null=True)
    email = models.EmailField(max_length=200,null=True)
    situation = models.CharField(choices=SITUATION_FAMILIALE , max_length=1,null=True)
    # date recrutememtn
    date_joined = models.DateField()
    date_recretment  = models.DateField()
    Nenfant=models.IntegerField()
    nature=models.CharField(choices=NATURE , max_length=1,null=True)
    numccp=models.IntegerField()
    numss=models.IntegerField()
    Xfonctionnair = models.BooleanField(default=False)
    motif = models.CharField(default="N", choices=MOTIF,max_length=2)
    date_supression = models.DateField(auto_now_add=True,null=True,blank=True)
    comentaire = models.TextField(null=True,blank=True)
    date_effet = models.DateField(blank=True,null=True)
    cheked = models.BooleanField(default=False)
    is_greater_than_2 = models.BooleanField(default=False)
    is_greater_than_10 = models.BooleanField(default=False)
    decision = models.CharField(default="N",max_length=1,choices=DECISION) 
    color = models.CharField(max_length=10,null=True,blank=True)
    checked = models.BooleanField(default=False)
    date = models.DateField(blank=True,null=True)
    alerte = models.CharField(default="0", max_length=1,choices=ALERT)
    def __str__(self):
        return self.nom

FILIERE = (
        ('0','Filiere'),
        ('A','Administration'),
        ('I','Informatique'),
    )

GRADES = (
    # default
    ('0','Grade'),
    # Adminitration
    ('GA','Adimistrateur'),
    ('GAP','Administrateur principal'),
    ('GAC','Administrateur conseiller'),
    ('GAA',"Attaché d'administration"),
    ('GPA',"Attaché principale d'administration"),
    ('AB',"Agents de bureau"),
    ('AA',"Agent d'administration"),
    ('APA',"Agent principale d'administration"),
    ('AS',"Agents de saisie"),
    ('S',"Secretaire"),
    ("SD","Secretaire de direction"),
    ('SPD',"Secretaire principale de direction"),
    ('ACA',"Aide comptable administrative"),
    ("CA","Compatble administrative"),
    ('CAP',"Comptable administrative principale"),
    #Informatique
    ("IA","Ingenieur d'application"),
    ("IE","Ingenieur d'etat"),
    ("IP","Ingenieur principal"),
    ("IC","Ingenieur en chef"),
    ("T","Technicien"),
    ("TS","Technicien superieur"),
    ("AT","Adjoint technique"),
    ("AST","Agent technique")
)

CORPS = (
    # default
    ("0","COPRS"),
    #admnisi
    ("A","Adminstrateurs"),
    ("AD","Attachés d'dministrations"),
    ("AA","Agents d'dministrations"),
    ("S","Secretaire"),
    ("CA","Comptables administratifs"),
    # info
    ("I","Ingenieurs"),
    ("T","Techniciens"),
    ("AT","Adjoint techniques"),
    ("AST","Agents techniques"),
)



POSTES = (
    ('R','Rien'),
    ('D','Directeur'),
    ('DA','Directeur adjoint'),
    ('CD','Chef de departement'),
    ('SG','Secretaire generale'),
    ('DB','Directeur de la bibliotheque'),
    ('SDPF','Sous directeur des personnels et de la formation'),
    ('SDFM','Sous directeur des finances et de moyens'),
    ('RCIA',"Responsable de centre d'impression et d'audiovisuel"),
    ('RCSI',"Responsable de centre de systemes et reseaux d'informations"),
    ("RHT","Responsable de hall de technologies"),
    ("RFP","Responsable de la forme de production")
)

PROMO = (
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('6','6'),
    ('7','7'),
    ('8','8'),
    ('9','9'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
)

ECHELON = (
    ('0','0'),
    ('1','1er'),
    ('2','2eme'),
    ('3','3eme'),
    ('4','4eme'),
    ('5','5eme'),
    ('6','6eme'),
    ('7','7eme'),
    ('8','8eme'),
    ('9','9eme'),
    ('10','10eme'),
    ('11','11eme'),
    ('12','12eme'),
)

class Paie(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    filiere = models.CharField(default='0',max_length=1,choices=FILIERE)
    grade = models.CharField(default="0",max_length=3,choices=GRADES)
    corps = models.CharField(default="0",max_length=3,choices=CORPS)
    categorie = models.IntegerField(default=0)
    indice = models.IntegerField(default=0)
    salaire = models.FloatField(default=0.0)
    poste_occupe = models.CharField(default='R',max_length=4,choices=POSTES)
    indiciaire = models.FloatField(default=0.0)
    categorie_promo = models.CharField(default="0",max_length=2,choices=PROMO)
    groupe = models.CharField(default="None",max_length=10)
    indice_minimale = models.FloatField(default=0.0)
    indice_echelon = models.CharField(default="0",max_length=2,choices=ECHELON)
    echelon = models.IntegerField(default=0)
    grille = models.FloatField(default=0.0) 
    indemite_sac = models.FloatField(default=0.0)   
    indemite_stc = models.FloatField(default=0.0)
    securite = models.FloatField(default=0.0)
    salaire_brut = models.FloatField(default=0.0)
    indimnite_transport = models.IntegerField(default=0)
    indimnite_panier = models.IntegerField(default=0)
    totale_brute_imposable_irg = models.FloatField(default=0.0)
    irg = models.IntegerField(default=0)
    allocation_familiale = models.IntegerField(default=0)
    totale = models.FloatField(default=0.0)
    nombre_travaille = models.IntegerField(default=0)
    nombre_absence = models.IntegerField(default=0)
    salaire_net = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.nom




NATUREC = (
    ('M','Maladie'),
    ('A','Annuel'),
    ('E','Exceptionnel')
)

class Conge(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    debut = models.DateField(null=True,blank=True)
    fin = models.DateField(null=True,blank=True)
    nombre = models.CharField(max_length=50,null=True,blank=True)
    nature = models.CharField(null=True,blank=True,max_length=1,choices=NATUREC)
    retour = models.DateTimeField(null=True,blank=True)
    commentaire = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.employee.nom



TRIMESTRE = (
    ("1","1er trimestre"),
    ("2","2eme trimestre"),
    ('3','3eme trimestre'),
    ('4',"4eme trimestre")
)


class Prime(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    note_prime = models.IntegerField(blank=True,null=True)
    commentaire = models.TextField(blank=True,null=True)
    trimestre = models.CharField(max_length=1,choices=TRIMESTRE,blank=True,null=True)
    date = models.DateField(blank=True,null=True)
    salaire_principal = models.FloatField() 
    salaire_brut_mensulle = models.FloatField() 
    salaire_brut_trimi = models.FloatField() 
    securite_sociale = models.FloatField() 
    base_impot = models.FloatField() 
    irg = models.FloatField() 
    prime_net = models.FloatField() 
    created_at = models.DateTimeField(auto_now_add=True)
    