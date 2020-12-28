from django.shortcuts import render, redirect

def home_page_view(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)
