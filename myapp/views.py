from django.shortcuts import render

def DisplayMyPage(request):
    return render(request, 'myapp/mypage.html', {'welcome_text' : 'hello_world'})
