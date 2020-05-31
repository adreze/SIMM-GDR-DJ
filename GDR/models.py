from django.db import models

# Create your models here.
TEAMS = (
    ('CE', 'SIMM-Centre'),
    ('ME', 'SIMM-Mercier'),
    ('MO', 'SIMM-MO'),
)


TYPES = (
    ('Ins', 'Installation'),
    ('Reins', 'Réinstallation'),
    ('Rep', 'Remplacement'),
    ('Stud', 'Pc étudiant'),
)


class Install(models.Model):

    simmuser = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    computer = models.CharField(max_length=200)
    dateplanned = models.DateField('date prevue')
    dcu = models.BooleanField(default=False)
    gds = models.BooleanField(default=False)
    appext = models.BooleanField(default=False)
    printers = models.BooleanField(default=False)
    gdp = models.BooleanField(default=False)
    backup = models.BooleanField(default=False)
    invoice = models.BooleanField(default=False)
    apex = models.BooleanField(default=False)
    type = models.CharField(max_length=200, choices=TYPES)
    byteam = models.CharField(max_length=20, choices=TEAMS)
    comments = models.CharField(max_length=200)


def __str__(self):
    return self.get_type_display()


class Reinstall(models.Model):
    simmuser = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    computer = models.CharField(max_length=200)
    dateplanned = models.DateField('date prevue')
    dcu = models.BooleanField(default=False)
    datatransfert = models.BooleanField(default=False)
    appext = models.BooleanField(default=False)
    printers = models.BooleanField(default=False)
    backup = models.BooleanField(default=False)
    type = models.CharField(max_length=200, choices=TYPES)
    byteam = models.CharField(max_length=20, choices=TEAMS)
    comments = models.CharField(max_length=200)


class Replacement(models.Model):
    simmuser = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    computer = models.CharField(max_length=200)
    dateplanned = models.DateField('date prevue')
    dcu = models.BooleanField(default=False)
    gds = models.BooleanField(default=False)
    datatransfert = models.BooleanField(default=False)
    appext = models.BooleanField(default=False)
    printers = models.BooleanField(default=False)
    gdp = models.BooleanField(default=False)
    backupnew = models.BooleanField(default=False)
    backupold = models.BooleanField(default=False)
    invoice = models.BooleanField(default=False)
    apex = models.BooleanField(default=False)
    type = models.CharField(max_length=200, choices=TYPES)
    byteam = models.CharField(max_length=20, choices=TEAMS)
    comments = models.CharField(max_length=200)


class StudentPC(models.Model):
    simmuser = models.CharField(max_length=200)
    person = models.CharField(max_length=200)
    computer = models.CharField(max_length=200)
    dateplanned = models.DateField('date prevue')
    dcu = models.BooleanField(default=False)
    appext = models.BooleanField(default=False)
    adminblank = models.BooleanField(default=False)
    lduninstall = models.BooleanField(default=False)
    type = models.CharField(max_length=200, choices=TYPES)
    byteam = models.CharField(max_length=20, choices=TEAMS)
    comments = models.CharField(max_length=200)