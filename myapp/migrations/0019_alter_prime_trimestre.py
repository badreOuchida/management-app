# Generated by Django 3.2.5 on 2021-08-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_auto_20210811_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prime',
            name='trimestre',
            field=models.CharField(blank=True, choices=[('1', '1er trimestre'), ('2', '2eme trimestre'), ('3', '3eme trimestre'), ('4', '4eme trimestre')], max_length=1, null=True),
        ),
    ]