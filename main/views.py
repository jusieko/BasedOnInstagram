from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Comment
from django.shortcuts import redirect
from main.forms import CommentForm


def index(request):
    if request.method == 'GET':
        form = CommentForm()
        images = Image.objects.all().order_by('-id')[:3]

        comments = Comment.objects.all()
        return render(request, 'index.html', {
            'images': images,
            'comments': comments,
            'form': form
        })
    else:
        form = CommentForm(request.POST)

        form.instance.username = request.user.username
        form.instance.photo_id = request.POST['txt']

        if form.is_valid():

            form.save()

            return redirect('/')
        else:
            return HttpResponse(form
                                )
