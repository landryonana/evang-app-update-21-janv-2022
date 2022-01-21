# Generated by Django 2.2.24 on 2022-01-08 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evangelisation', '0003_auto_20211224_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evangelisation',
            name='boss',
            field=models.ManyToManyField(blank=True, null=True, related_name='participations', to='evangelisation.Participant', verbose_name='Qui sont présents ?'),
        ),
        migrations.AlterField(
            model_name='person',
            name='boss',
            field=models.ManyToManyField(blank=True, help_text='selectionner les personnes ayant évangelisés cette personne', null=True, related_name='personnes', to='evangelisation.Participant', verbose_name="Qui l'ont évangelisé ?"),
        ),
        migrations.AlterField(
            model_name='person',
            name='contacts',
            field=models.PositiveIntegerField(blank=True, error_messages={'unique': 'Une personne avec ce numéro de télephone existe déjà'}, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='quartier_d_habitation',
            field=models.CharField(blank=True, help_text='ce champ doit avoir au moins trois caractères', max_length=200, null=True, verbose_name="Quartier d'habitation"),
        ),
        migrations.AlterField(
            model_name='person',
            name='whatsapp',
            field=models.CharField(blank=True, choices=[('oui', 'Oui'), ('non', 'Non')], max_length=15, null=True, verbose_name='Whatsapp'),
        ),
    ]