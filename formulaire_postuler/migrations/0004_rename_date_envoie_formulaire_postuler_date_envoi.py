# Generated by Django 4.1 on 2022-08-19 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulaire_postuler', '0003_alter_formulaire_postuler_telephone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formulaire_postuler',
            old_name='date_envoie',
            new_name='date_envoi',
        ),
    ]