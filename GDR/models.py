from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    roles = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    team = models.CharField(max_length=200)

# simm_user, person, computer, dateplanned, dcu , gds, appext, printers, gdp, backup, invoice, apex, type, byteam, comments
class Installations(models.Model):
    simm_user = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    computer = models.CharField(max_length=200)
    dateplanned = models.DateTimeField('date prevue')
    #dcu = models.

# simm_user, person, computer, dateplanned, dcu , datatransfert, appext, printers, backup, type, byteam, comments
class Reinstallations(models.Model):
    simm_user = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    computer = models.CharField(max_length=200)
    dateplanned = models.DateTimeField('date prevue')

# simm_user, person, oldcomputer, newcomputer, dateplanned, dcu , gds, datatransfert, appext, printers, gdp, backupnew backupold, invoice, apex type, byteam, comments

class Remplacements(models.Model):
    simm_user = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    computer = models.CharField(max_length=200)
    dateplanned = models.DateTimeField('date prevue')


# simm_user, person, computer, dateplanned, dcu, appext, adminblank, lduninstall, type , byteam, comments

class StudentsPC(models.Model):
    simm_user = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    computer = models.CharField(max_length=200)
    dateplanned = models.DateTimeField('date prevue')