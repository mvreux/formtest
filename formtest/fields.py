from django.forms import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from django.core import validators
from formtest.widgets import Recaptcha
from recaptcha.client import captcha
import pprint

class SecretWordField(forms.Field):
    default_error_messages = { 'bad_word': _(u'That\'s not the right word, bro!') }
    secret_word = 'secret'
    
    def validate(self, value):
        super(SecretWordField, self).validate(value)
        if value != self.secret_word:
            raise ValidationError(self.default_error_messages['bad_word'])
        
class CaptchaField(forms.Field):
    
   default_error_messages = { 'invalid_answer' : _(u'The confirmation code is invalid!') }
   widget = Recaptcha
   
   def validate(self, value):
       captchaResponse = captcha.submit(value['recaptcha_challenge_name'], 
                                        value['recaptcha_response_name'], 
                                        settings.RECAPTCHA_PRIVATE_KEY, 
                                        '')
       if not captchaResponse.is_valid:
           raise ValidationError(self.default_error_messages['invalid_answer'])