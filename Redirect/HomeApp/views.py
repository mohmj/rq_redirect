from django.shortcuts import *
from django.http import HttpRequest

def welcome_redirect(request):
    siteName=request.GET.get("siteName") or "hi"
    # return render(request,"welcome_redirect.html",{"siteName":siteName})
    return redirect("https://google.com")