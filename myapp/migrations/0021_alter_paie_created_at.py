# Generated by Django 3.2.5 on 2021-08-12 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_paie_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
