# Generated by Django 3.2.5 on 2021-08-23 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_employee_alerte'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='employee',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
