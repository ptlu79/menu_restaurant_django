# Generated by Django 3.1.6 on 2021-02-10 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identitystore',
            old_name='adresse_restaurant',
            new_name='adresse',
        ),
        migrations.RenameField(
            model_name='identitystore',
            old_name='code_postal_restaurant',
            new_name='code_postal',
        ),
        migrations.RenameField(
            model_name='identitystore',
            old_name='nom_restaurant',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='identitystore',
            old_name='pays_restaurant',
            new_name='pays',
        ),
        migrations.RenameField(
            model_name='identitystore',
            old_name='telephone_restaurant',
            new_name='telephone',
        ),
        migrations.RenameField(
            model_name='identitystore',
            old_name='ville_restaurant',
            new_name='ville',
        ),
    ]
