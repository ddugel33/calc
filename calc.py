form cgi import parse_qs
from template import html

def application(environ, start_response):
    d=parse_qs(environ['QUERY_STRING'])
    f_num = d.get('f_num',[''])[0]
    s_num = d.get('s_num',[''])[0]

    sum = int(f_num) + int(s_num)
    mul = int(f_num) * int(s_num)

    response_body = html % {'sum':sum, 'mul':mul}

    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
