from django.forms import Widget
from django.utils import translation
from django.utils.safestring import mark_safe
from django.conf import settings

class Recaptcha(Widget):
    
    recaptcha_challenge_name = 'recaptcha_challenge_field'
    recaptcha_response_name = 'recaptcha_response_field'
    
    def render(self, name, value, attrs=None):
        output = """
            <script type="text/javascript" src="http://www.google.com/recaptcha/api/challenge?k=%(RECAPTCHA_PUBLIC_KEY)s&lang=%(lang)s"></script>
            <noscript>
                <iframe src="http://www.google.com/recaptcha/api/noscript?k=%(RECAPTCHA_PUBLIC_KEY)s&lang=%(lang)s" height="300" width="500"></iframe><br/>
                <textarea name="%(recaptcha_challenge_name)s" rows="3" cols="40"></textarea>
                <input type="hidden" name="%(recaptcha_response_name)s" value="manual_challenge" />
            </noscript>
        """ % {
                  'RECAPTCHA_PUBLIC_KEY' : settings.RECAPTCHA_PUBLIC_KEY,
                  'lang' : translation.get_language(),
                  'recaptcha_challenge_name': self.recaptcha_challenge_name,
                  'recaptcha_response_name' : self.recaptcha_response_name,
              }
        
        #print output
        
        return mark_safe(output)
    
    def value_from_datadict(self, data, files, name):
        return {'recaptcha_challenge_name' : data.get(self.recaptcha_challenge_name, None), 'recaptcha_response_name' : data.get(self.recaptcha_response_name, None),}
        