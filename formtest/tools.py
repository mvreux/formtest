from django.http import HttpResponse
from string import maketrans

def json_response(x):
    import json
    return HttpResponse(json.dumps(x, ensure_ascii=False, sort_keys=True, indent=2),
                        content_type='application/json; charset=UTF-8')
            
            
            
            