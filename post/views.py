from django.shortcuts import render, get_object_or_404, redirect

def home_page_view(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)
