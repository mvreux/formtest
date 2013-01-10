from django import forms
from django.utils.translation import ugettext_lazy as _
import myform.models
from formtest.fields import SecretWordField, CaptchaField
from django_extensions.tests.models import Secret

class ChickenForm(forms.Form):
    CHOICES = (
                ('other_side', _('To go on the other side!')),
                ('female', _('Because he saw some hot chick')),
                ('derp', _('Because he\'s an idiot')),
               )
    title = forms.CharField(label=_('The title of the entry'), max_length=10)
    nbChicks = forms.IntegerField(label=_('Number of chickens crossing the road'))
    animal = forms.CharField(label=_('Animal'), max_length=200)
    species = forms.CharField(label=_('Species'), max_length=200)
    why = forms.ChoiceField(label=_('Why did the chicken cross the road?'), choices=CHOICES, widget=forms.RadioSelect)
    secret = SecretWordField(label=_(u'Secret:'))
    captcha = CaptchaField(label=_('Are you human?'))

