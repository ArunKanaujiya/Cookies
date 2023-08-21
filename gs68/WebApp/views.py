from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response=render(request,'myapp/setcookie.html')
    response.set_cookie('name','arun',max_age=50)
    return response


def getcookie(request):
    name=request.COOKIES.get('name','without value')
    return render(request,'myapp/getcookie.html',{'name':name})

def delcookie(request):
    response=render(request,'myapp/delcookie.html')
    response.delete_cookie('name')
    return response

