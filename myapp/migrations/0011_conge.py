# Generated by Django 3.2.5 on 2021-08-10 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20210810_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debut', models.DateField()),
                ('fin', models.DateField()),
                ('nombre', models.CharField(max_length=50)),
                ('nature', models.CharField(choices=[('M', 'Maladie'), ('A', 'Annuel'), ('E', 'Exceptionnel')], max_length=1)),
                ('retour', models.DateTimeField()),
                ('commentaire', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
        ),
    ]