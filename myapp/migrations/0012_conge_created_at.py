# Generated by Django 3.2.5 on 2021-08-10 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_conge'),
    ]

    operations = [
        migrations.AddField(
            model_name='conge',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
