from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(fecha_publicado__lte=timezone.now()).order_by('fecha_creado')
    return render(request, 'blog/post_list.html', {'posts': posts})

