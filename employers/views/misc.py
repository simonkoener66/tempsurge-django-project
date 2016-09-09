from django.shortcuts import render
from accounts.decorators import group_required


@group_required('employers')
def dashboard(request):
    return render(request, 'employers/dashboard.html', {})