('/Users/asnounsamir/workspaces/django_projects/CommunityBethnoe/Bethnoe/locale',)
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class BibleenkabyleChapitrebible(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content = models.TextField()
    titre = models.CharField(max_length=250)
    livre = models.ForeignKey('BibleenkabyleLivrebible', models.DO_NOTHING)
    audio = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'BibleEnKabyle_chapitrebible'


class BibleenkabyleLivrebible(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titre = models.CharField(max_length=250)
    type_na = models.CharField(max_length=2)
    slug = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'BibleEnKabyle_livrebible'


class EglisebethnoeAdresse(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type_rue = models.CharField(max_length=2)
    nom_rue = models.CharField(max_length=150)
    ville = models.CharField(max_length=150)
    code_dep = models.CharField(max_length=150)
    num_rue = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_adresse'


class EglisebethnoeAdressesimple(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    num_rue = models.IntegerField()
    type_rue = models.CharField(max_length=2)
    nom_rue = models.CharField(max_length=150)
    ville = models.CharField(max_length=150)
    code_postale = models.CharField(max_length=150)
    pays = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_adressesimple'


class EglisebethnoeAlbum(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=128)
    slug = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_album'


class EglisebethnoeAnnonce(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_annonce'


class EglisebethnoeAudio(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    audio = models.CharField(max_length=100)
    slug = models.CharField(max_length=150)
    titre = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_audio'


class EglisebethnoeAudioducd(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    audio_cd = models.ForeignKey(EglisebethnoeAudio, models.DO_NOTHING)
    cd = models.ForeignKey('EglisebethnoeCd', models.DO_NOTHING)
    contient = models.ForeignKey(EglisebethnoeAudio, models.DO_NOTHING, db_column='Contient_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_audioducd'


class EglisebethnoeCd(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titre = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_cd'


class EglisebethnoeChapitreLien(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content = models.TextField()
    title = models.CharField(max_length=64)
    slug = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_chapitre_lien'


class EglisebethnoeConfessiondefoie(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    content = models.TextField()
    logo = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_confessiondefoie'


class EglisebethnoeContact(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nom = models.CharField(max_length=64)
    prenom = models.CharField(max_length=64)
    email = models.CharField(max_length=254)
    telephone = models.CharField(max_length=10)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_contact'


class EglisebethnoeCultehebdo(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    content = models.TextField()
    video_url = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_cultehebdo'


class EglisebethnoeDirigenteglisebethnoe(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nom = models.CharField(max_length=150)
    photo = models.ForeignKey('EglisebethnoeImage', models.DO_NOTHING, unique=True)
    lien = models.CharField(max_length=200)
    role = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_dirigenteglisebethnoe'


class EglisebethnoeEcoles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField()
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_ecoles'


class EglisebethnoeEvenement(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titre = models.CharField(max_length=128)
    content = models.TextField()
    album = models.ForeignKey(EglisebethnoeAlbum, models.DO_NOTHING, unique=True)
    type_evenments = models.CharField(max_length=2)
    slug = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_evenement'


class EglisebethnoeFondecran(models.Model):
    image_ptr = models.ForeignKey('EglisebethnoeImage', models.DO_NOTHING, primary_key=True)
    afficher = models.CharField(max_length=3)
    caption = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_fondecran'


class EglisebethnoeImage(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    photo = models.CharField(max_length=100)
    title = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_image'


class EglisebethnoeImagecarrousel(models.Model):
    image_ptr = models.ForeignKey(EglisebethnoeImage, models.DO_NOTHING, primary_key=True)
    afficher = models.CharField(max_length=3)
    caption = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_imagecarrousel'


class EglisebethnoeImageevenement(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    image = models.CharField(max_length=100)
    titre_image = models.CharField(max_length=128)
    slug = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_imageevenement'


class EglisebethnoeIndexeglisebethnoe(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title1 = models.CharField(max_length=64)
    content = models.TextField()
    video_url = models.CharField(max_length=200)
    title2 = models.CharField(max_length=64)
    fond_ecran = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_indexeglisebethnoe'


class EglisebethnoeLienC(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=200)
    slug = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_lien_c'


class EglisebethnoeLiende(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    chapitre_lien = models.ForeignKey(EglisebethnoeChapitreLien, models.DO_NOTHING)
    lie_a = models.ForeignKey(EglisebethnoeLienC, models.DO_NOTHING)
    url_p = models.ForeignKey(EglisebethnoeLienC, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_liende'


class EglisebethnoePhotode(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    album = models.ForeignKey(EglisebethnoeAlbum, models.DO_NOTHING)
    image_evenement = models.ForeignKey(EglisebethnoeImageevenement, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_photode'


class EglisebethnoePost(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField()
    image = models.CharField(max_length=100)
    content_rich = models.TextField()
    slug = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_post'


class EglisebethnoePriere(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=64)
    content = models.TextField()
    created_at = models.DateTimeField()
    image = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=64)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_priere'


class EglisebethnoeTextdirigenteglisebethnoe(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titre = models.CharField(max_length=50)
    texte = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'EgliseBethnoe_textdirigenteglisebethnoe'


class EnseignementsbibliquesAuteur(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'EnseignementsBibliques_auteur'


class EnseignementsbibliquesEglisepartenaire(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titre = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.CharField(max_length=50)
    media = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'EnseignementsBibliques_eglisepartenaire'


class EnseignementsbibliquesEnseignementbiblique(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    type_media = models.CharField(max_length=2)
    content = models.TextField()
    titre = models.CharField(max_length=250)
    slug = models.CharField(max_length=50)
    media = models.CharField(max_length=100)
    titre_media = models.CharField(max_length=250)
    auteur = models.ForeignKey(EnseignementsbibliquesAuteur, models.DO_NOTHING)
    theme = models.ForeignKey('EnseignementsbibliquesTheme', models.DO_NOTHING)
    image = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'EnseignementsBibliques_enseignementbiblique'


class EnseignementsbibliquesSection(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titre = models.CharField(max_length=250)
    content = models.TextField()
    media = models.CharField(max_length=100)
    onglet = models.CharField(max_length=6)
    logo = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'EnseignementsBibliques_section'


class EnseignementsbibliquesTheme(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titre = models.CharField(max_length=250)
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'EnseignementsBibliques_theme'


class EtudesbibliquesEtudebiblique(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content = models.TextField()
    titre = models.CharField(max_length=250)
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'EtudesBibliques_etudebiblique'


class EtudesbibliquesIntrofuctionetudebiblique(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content = models.TextField()
    titre = models.CharField(max_length=250)
    slug = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'EtudesBibliques_introfuctionetudebiblique'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
