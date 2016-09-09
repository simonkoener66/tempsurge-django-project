from django.template.response import TemplateResponse


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# def tempsurge_redirect(request, app='tempsurge', connotation='info', title='', message='', url=''):
#     return TemplateResponse(request, 'tempsurge/redirect.html', {
#         'app': app,
#         'connotation': connotation,
#         'title': title,
#         'message': message,
#         'url': url
#     })