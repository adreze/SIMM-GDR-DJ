from django import forms
#from .models import User
from django.utils.translation import gettext_lazy as _
from GDR.models import StudentPC, Install, Reinstall, Replacement


class DateInput(forms.DateInput):
    input_type = 'date'


class PcStudentsForm(forms.ModelForm):
    class Meta:
        model = StudentPC
        fields = ('person', 'computer', 'dateplanned', 'dcu', 'appext', 'adminblank', 'lduninstall', 'comments')
        labels = {
            'person': _('Personne'),
            'computer': _('Ordinateur'),
            'dateplanned': _('Date prévue'),
            'dcu': _('Dell Command Update'),
            'appext': _('Applications et extensions'),
            'adminblank': _('Pass admin à blanc'),
            'lduninstall': _('Désinstallation de LanDesk'),
            'comments': _('Commentaires')
        }
        widgets = {
            'dateplanned': DateInput(),
        }



class InstallForm(forms.ModelForm):
    class Meta:
        model = Install
        fields = ('person', 'computer', 'dateplanned', 'dcu', 'gds', 'appext', 'printers', 'gdp', 'backup', 'invoice', 'apex','comments')
        labels = {
            'person': _('Personne'),
            'computer': _('Ordinateur'),
            'dateplanned': _('Date prévue'),
            'dcu': _('Dell Command Update'),
            'gds': _('Gestion de stock'),
            'appext': _('Applications et extensions'),
            'printers': _('Imprimantes'),
            'gdp': _('Gestion de parc'),
            'backup': _('Backup'),
            'invoice': _('Facturation'),
            'apex': _('Apex'),
            'comments': _('Commentaires')
        }
        widgets = {
            'dateplanned': DateInput(),
        }



class ReinstallForm(forms.ModelForm):
    class Meta:
        model = Reinstall
        fields = ('person', 'computer', 'dateplanned', 'dcu', 'datatransfert', 'appext', 'printers', 'backup','comments')
        labels = {
            'person': _('Personne'),
            'computer': _('Ordinateur'),
            'dateplanned': _('Date prévue'),
            'dcu': _('Dell Command Update'),
            'datatransfert': _('Transfert des données'),
            'appext': _('Applications et extensions'),
            'printers': _('Imprimantes'),
            'backup': _('Backup'),
            'comments': _('Commentaires')
        }
        widgets = {
            'dateplanned': DateInput(),
        }


class ReplacementForm(forms.ModelForm):
    class Meta:
        model = Replacement
        fields = ('person', 'computer', 'dateplanned', 'dcu', 'gds', 'datatransfert', 'appext', 'printers', 'gdp', 'backupnew', 'backupold', 'invoice', 'apex', 'comments')
        labels = {
            'person': _('Personne'),
            'computer': _('Ordinateur'),
            'dateplanned': _('Date prévue'),
            'dcu': _('Dell Command Update'),
            'gds': _('Gestion de Stock'),
            'datatransfert': _('Transfert des données'),
            'appext': _('Applications et extensions'),
            'printers': _('Imprimantes'),
            'gdp': _('Gestion de parc'),
            'backupnew': _('Backup (nouveau PC)'),
            'backupold': _('Backup (Ancien PC)'),
            'invoice': _('Facturation'),
            'apex': _('Apex'),
            'comments': _('Commentaires'),
        }
        widgets = {
            'dateplanned': DateInput(),
        }


