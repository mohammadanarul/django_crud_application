from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import post_model_form
def home_page_view(request):
    post = Post.objects.all()
    template_name = 'home.html'
    context = {'post': post,}
    return render(request, template_name, context)

def post_details_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    template_name = 'post/post_details.html'
    context = {'post': post,}
    return render(request, template_name, context)

def create_post(request):
    form = post_model_form()
    if request.method == 'POST':
        form = post_model_form(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = post_model_form()
    template_name = 'post/create_post.html'
    context = {'form': form}
    return render(request, template_name, context)

def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = post_model_form(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('/')
    template_name = 'post/update_post.html'
    context = {'form': form, 'post': post,}
    return render(request, template_name, context)

def delete_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect('/')
