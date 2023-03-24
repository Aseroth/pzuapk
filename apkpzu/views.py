from django.shortcuts import render

def apk_list(request):
    return render(request, 'apk/apk_list.html', {})

# Create your views here.
