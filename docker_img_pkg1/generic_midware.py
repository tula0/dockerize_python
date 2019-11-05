
__all__=['simple_app','validator_app']

from wsgiref import simple_server
from wsgiref import validate


#server
def simple_app(envirion,start_response):
    status='200 OK'
    headers=[('ContentType','text/plain')]
    start_response(status,headers)
#validator
validator_app= validate.validator(simple_app)

#starrt httpd
with simple_server.make_server('',8000,validator_app) as  httpd:
    print('Serving on port 8000....')
    httpd.serve_forever()

