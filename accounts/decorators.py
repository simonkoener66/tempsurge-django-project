from django.contrib.auth.decorators import user_passes_test


def group_required(*group_names):
    """
    Requires user account in at least one of the groups passed in.

    This decorator provides a @group_required decorator. You can pass in multiple groups, for example:

    @group_required('admins','editors')
    def myview(request, id):
    ...

    It is important to check that the user is first logged in, as anonymous users trigger an AttributeError when the groups filter is executed.

    To use it through urls.py

    urlpatterns = patterns('',
        url(r'^$',
            group_required(['root', 'manager'])(views.admin),
            name='admin'),
        ...
    """

    def in_groups(u):
        if u.is_authenticated():
            if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
                return True
        return False

    return user_passes_test(in_groups)