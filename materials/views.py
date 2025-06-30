from django.shortcuts import render
from .models import Material
from django.contrib.auth.decorators import login_required

@login_required
def material_list(request):
    materials = Material.objects.all().order_by('-created_at')
    return render(request, 'materials/material_list.html', {
        'materials': materials
    })
