from django.shortcuts import render
from .models import FirmwareCategory
from django.contrib.auth.decorators import login_required

@login_required
def firmware_category_list(request):
    categories = FirmwareCategory.objects.all()
    return render(request, 'firmware_category/firmware_category_list.html', {'categories': categories})
