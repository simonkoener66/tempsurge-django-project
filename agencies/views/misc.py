from django.shortcuts import render
from accounts.decorators import group_required


@group_required('agencies')
def dashboard(request):
    return render(request, 'agencies/dashboard.html', {})