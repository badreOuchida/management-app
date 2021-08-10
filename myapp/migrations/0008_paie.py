# Generated by Django 3.2.5 on 2021-08-08 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_employee_date_joined'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filiere', models.CharField(choices=[('0', 'Filiere'), ('A', 'Administration'), ('I', 'Informatique')], default='0', max_length=1)),
                ('grade', models.CharField(choices=[('0', 'Grade'), ('GA', 'Adimistrateur'), ('GAP', 'Administrateur principal'), ('GAC', 'Administrateur conseiller'), ('GAA', "Attaché d'administration"), ('GPA', "Attaché principale d'administration"), ('AB', 'Agents de bureau'), ('AA', "Agent d'administration"), ('APA', "Agent principale d'administration"), ('AS', 'Agents de saisie'), ('S', 'Secretaire'), ('SD', 'Secretaire de direction'), ('SPD', 'Secretaire principale de direction'), ('ACA', 'Aide comptable administrative'), ('CA', 'Compatble administrative'), ('CAP', 'Comptable administrative principale'), ('IA', "Ingenieur d'application"), ('IE', "Ingenieur d'etat"), ('IP', 'Ingenieur principal'), ('IC', 'Ingenieur en chef'), ('T', 'Technicien'), ('TS', 'Technicien superieur'), ('AT', 'Adjoint technique'), ('AST', 'Agent technique')], default='0', max_length=3)),
                ('corps', models.CharField(choices=[('0', 'COPRS'), ('A', 'Adminstrateurs'), ('AD', "Attachés d'dministrations"), ('AA', "Agents d'dministrations"), ('S', 'Secretaire'), ('CA', 'Comptables administratifs'), ('I', 'Ingenieurs'), ('T', 'Techniciens'), ('AT', 'Adjoint techniques'), ('AST', 'Agents techniques')], default='0', max_length=3)),
                ('categorie', models.IntegerField(default=0)),
                ('indice', models.IntegerField(default=0)),
                ('salaire', models.FloatField(default=0.0)),
                ('poste_occupe', models.CharField(choices=[('R', 'Rien'), ('D', 'Directeur'), ('DA', 'Directeur adjoint'), ('CD', 'Chef de departement'), ('SG', 'Secretaire generale'), ('DB', 'Directeur de la bibliotheque'), ('SDPF', 'Sous directeur des personnels et de la formation'), ('SDFM', 'Sous directeur des finances et de moyens'), ('RCIA', "Responsable de centre d'impression et d'audiovisuel"), ('RCSI', "Responsable de centre de systemes et reseaux d'informations"), ('RHT', 'Responsable de hall de technologies'), ('RFP', 'Responsable de la forme de production')], default='R', max_length=4)),
                ('indiciaire', models.IntegerField(default=0)),
                ('categorie_promo', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16')], default='0', max_length=2)),
                ('groupe', models.CharField(default='None', max_length=10)),
                ('indice_minimale', models.IntegerField(default=0)),
                ('indice_echelon', models.CharField(choices=[('0', '0'), ('1', '1er'), ('2', '2eme'), ('3', '3eme'), ('4', '4eme'), ('5', '5eme'), ('6', '6eme'), ('7', '7eme'), ('8', '8eme'), ('9', '9eme'), ('10', '10eme'), ('11', '11eme'), ('12', '12eme')], default='0', max_length=2)),
                ('echelon', models.IntegerField(default=0)),
                ('grille', models.IntegerField(default=0)),
                ('indemite_sac', models.IntegerField(default=0)),
                ('indemite_stc', models.IntegerField(default=0)),
                ('securite', models.IntegerField(default=0)),
                ('salaire_brut', models.IntegerField(default=0)),
                ('indimnite_transport', models.IntegerField(default=0)),
                ('indimnite_panier', models.IntegerField(default=0)),
                ('totale_brute_imposable_irg', models.IntegerField(default=0)),
                ('irg', models.IntegerField(default=0)),
                ('allocation_familiale', models.IntegerField(default=0)),
                ('totale', models.IntegerField(default=0)),
                ('nombre_travaille', models.IntegerField(default=0)),
                ('nombre_absence', models.IntegerField(default=0)),
                ('salaire_net', models.IntegerField(default=0)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
        ),
    ]
