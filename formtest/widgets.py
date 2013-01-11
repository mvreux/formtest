from django.forms import Widget
from django.utils import translation
from django.utils.safestring import mark_safe
from django.conf import settings
from django.template.loader import render_to_string

class Recaptcha(Widget):
    
    recaptcha_challenge_name = 'recaptcha_challenge_field'
    recaptcha_response_name = 'recaptcha_response_field'
    
    def render(self, name, value, attrs=None):
        output = render_to_string('recaptcha.html', 
              {
                  'RECAPTCHA_PUBLIC_KEY' : settings.RECAPTCHA_PUBLIC_KEY,
                  'lang' : translation.get_language(),
                  'recaptcha_challenge_name': self.recaptcha_challenge_name,
                  'recaptcha_response_name' : self.recaptcha_response_name,
              })
        
        return mark_safe(output)
    
    def value_from_datadict(self, data, files, name):
        return {'recaptcha_challenge_name' : data.get(self.recaptcha_challenge_name, None), 'recaptcha_response_name' : data.get(self.recaptcha_response_name, None),}
        