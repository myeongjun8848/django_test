from django.shortcuts import render

def DisplayMyPage(request):
    return render(request, 'myapp/mypage.html', {'welcome_text' : 'hello_world'})

def DisplayMyPageWithParameter(request, my_parameter):
    welcome_text = my_parameter
    return render(request, 'myapp/mypage.html', {'welcome_text' : welcome_text})
