# Generated by Django 2.2.24 on 2021-12-20 17:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evangelisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now, error_messages={'unique': "ce moment d'évangelisation existe déjà"}, unique=True, verbose_name="Jour d'évangélisation")),
                ('heure_de_debut', models.TimeField(default=django.utils.timezone.now, verbose_name='Heure de début')),
                ('heure_de_fin', models.TimeField(default=django.utils.timezone.now, verbose_name='Heure de fin')),
                ('observation', models.TextField(blank=True, null=True, verbose_name='Observations')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evangs', to=settings.AUTH_USER_MODEL, verbose_name='créer par ')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_et_prenom', models.CharField(error_messages={'unique': 'Un participant avec ce nom et\\ou prénom existe déjà'}, max_length=200, unique=True)),
                ('sexe', models.CharField(choices=[('masculin', 'Masculin'), ('féminin', 'Féminin')], max_length=15, verbose_name='Sexe')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participants', to=settings.AUTH_USER_MODEL, verbose_name='créer par ')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('nom_et_prenom', models.CharField(error_messages={'unique': 'Une personne avec ce nom existe déjà'}, help_text='ce champ doit avoir au moins trois caractères', max_length=200, unique=True, verbose_name='Nom et Prénom')),
                ('contacts', models.PositiveIntegerField(error_messages={'unique': 'Une personne avec ce numéro de télephone existe déjà'}, unique=True)),
                ('quartier_d_habitation', models.CharField(help_text='ce champ doit avoir au moins trois caractères', max_length=200, verbose_name="Quartier d'habitation")),
                ('accepte_jesus', models.CharField(choices=[('oui', 'Oui'), ('non', 'Non'), ('ras', 'Indécis'), ('déjà', 'Déjà')], max_length=15, verbose_name='Accepté JÉSUS')),
                ('sexe', models.CharField(choices=[('masculin', 'Masculin'), ('féminin', 'Féminin')], max_length=15, verbose_name='Sexe')),
                ('whatsapp', models.CharField(choices=[('oui', 'Oui'), ('non', 'Non')], max_length=15, verbose_name='Whatsapp')),
                ('sujets_de_priere', models.TextField(blank=True, help_text='ce champ est optionnel', null=True, verbose_name='Prière et observation')),
                ('temoignages', models.TextField(blank=True, help_text='ce champ est optionnel', null=True, verbose_name='Témoignage')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='créer à')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='mis à jour à')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_personnes', to=settings.AUTH_USER_MODEL, verbose_name='ajouter par ')),
                ('boss', models.ManyToManyField(help_text='selectionner les personnes ayant évangelisés cette personne', related_name='personnes', to='evangelisation.Participant', verbose_name="Qui l'ont évangelisé ?")),
                ('evangelisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personnes', to='evangelisation.Evangelisation', verbose_name="Moment d'évangelisation")),
            ],
            options={
                'verbose_name': 'Personne évangélisé',
                'ordering': ('nom_et_prenom',),
            },
        ),
        migrations.CreateModel(
            name='Suivi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nbre_appel', models.PositiveIntegerField(default=0, verbose_name="Nombre d'appel")),
                ('nbre_visite_au_culte', models.PositiveIntegerField(default=0, verbose_name='Nombre de visite')),
                ('nbre_invitation_au_culte', models.PositiveIntegerField(default=0, verbose_name="Nombre d'invitation au culte")),
                ('nbre_presence_total_au_culte', models.PositiveIntegerField(default=0, verbose_name='Nombre de présence éffective au culte')),
                ('choix_person', models.CharField(choices=[('---', '---'), ('rester', 'Rester'), ('passager', 'Passager'), ('indécis', 'Indécis')], default='---', max_length=25, verbose_name='Choix de la personne')),
                ('boos_suivi', models.TextField(verbose_name='Boss ayant éffectuer le suivi')),
                ('sujets_de_priere_suivi', models.TextField(blank=True, help_text='ce champ est optionnel', null=True, verbose_name='Sujet de prière')),
                ('temoignages_suivi', models.TextField(blank=True, help_text='ce champ est optionnel', null=True, verbose_name='Témoignage')),
                ('observation_suivi', models.TextField(blank=True, help_text='ce champ est optionnel', null=True, verbose_name='Observation')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='suivis', to=settings.AUTH_USER_MODEL, verbose_name='ajouter par ')),
                ('person', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='evangelisation.Person', verbose_name='Personne')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_site_evangelisation', models.CharField(error_messages={'unique': 'Un site avec ce nom existe déjà'}, help_text='le nom du site doit avoir au moins 03 caractères', max_length=200, unique=True, verbose_name="site d'évangélisation")),
                ('description', models.TextField(blank=True, help_text='ajouter une description du site', null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, help_text='ajouter une image', null=True, upload_to='images/site/%Y/%m/%d/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to=settings.AUTH_USER_MODEL, verbose_name='ajouter par ')),
            ],
            options={
                'verbose_name': "Site d'évangélisation",
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='ajouter une photo', null=True, upload_to='images/profile/%Y/')),
                ('phone', models.PositiveIntegerField(blank=True, error_messages={'unique': 'Une boss avec ce numéro de télephone existe déjà'}, help_text='le numéro de télephone doit avoir 9 chiffres', null=True, unique=True)),
                ('sexe', models.CharField(choices=[('masculin', 'Masculin'), ('féminin', 'Féminin')], max_length=15, verbose_name='Sexe')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(error_messages={'unique': 'Une image avec ce titre existe déjà'}, max_length=250, verbose_name='Titre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('image', models.ImageField(blank=True, upload_to='images/gallerie/%Y/%m/%d/')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publier le ')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to=settings.AUTH_USER_MODEL, verbose_name='créer par ')),
                ('evangelisation', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='images', to='evangelisation.Evangelisation', verbose_name='Évangelsation du ')),
            ],
        ),
        migrations.AddField(
            model_name='evangelisation',
            name='boss',
            field=models.ManyToManyField(blank=True, related_name='participations', to='evangelisation.Participant', verbose_name='Qui sont présents ?'),
        ),
        migrations.AddField(
            model_name='evangelisation',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='evangelisations', to='evangelisation.Site', verbose_name="Lieu d'évangelisation"),
        ),
    ]
