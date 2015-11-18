from django.shortcuts import render, get_object_or_404
from myapp import models

def DisplayMyPage(request):
    return render(request, 'myapp/mypage.html', {'welcome_text' : 'hello_world'})

def DisplayMyPageWithParameter(request, my_parameter,  my_parameter2):
    welcome_text1 = my_parameter
    welcome_text2 = my_parameter2
    return render(request, 'myapp/mypage.html', {'welcome_text' : welcome_text1 + welcome_text2})

def post_list(request):
    post_list = models.post.objects.all()
    return render(request, 'myapp/post_list.html', {'post_list' : post_list})

def post_view(request, post_id):
    post = get_object_or_404(models.post, pk=post_id)
    return render(request, 'myapp/post_view.html', {'post' : post})
