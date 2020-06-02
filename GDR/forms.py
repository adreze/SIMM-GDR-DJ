from django import forms
#from .models import User
from django.utils.translation import gettext_lazy as _
from GDR.models import StudentPC, Install


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



# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#         labels = {
#             'username': _('Utilisateur'),
#             'password': _('Mot de passe'),
#         }
#         # error_messages = {
#         #     'username': {
#         #         'badusername': _('Mauvais utilisateur'),
#         #     },
#         # }
