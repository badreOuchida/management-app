# Generated by Django 3.2.5 on 2021-08-03 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_employee_date_recretment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_recretment',
            field=models.DateField(blank=True, null=True),
        ),
    ]