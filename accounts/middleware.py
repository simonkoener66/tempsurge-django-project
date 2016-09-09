from django.core.urlresolvers import resolve
from django.contrib.auth.models import User


class ImpersonateMiddleware(object):
    """
    User impersonation by admin

    Usage:

    log in: http://localhost/?__impersonate=[USERID]
    log out (back to admin): http://localhost/?__unimpersonate=True
    """

    def process_request(self, request):
        if request.user.is_superuser and "__impersonate" in request.GET:
            request.session['impersonate_id'] = int(request.GET["__impersonate"])
        elif "__unimpersonate" in request.GET:
            del request.session['impersonate_id']

        if request.user.is_superuser and 'impersonate_id' in request.session:
            request.user = User.objects.get(id=request.session['impersonate_id'])


class ViewNameMiddleware(object):
    """
    So something like {% if request.url_name == "agencies.views.misc.dashboard" %} or {% if request.url_name == "agencies_dashboard" %} becomes possible in templates
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        url_name = resolve(request.path).url_name
        request.url_name = url_name