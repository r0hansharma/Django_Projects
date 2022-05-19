#from django.shortcuts import render

# Create your views from django.http import HttpResponse

#def index(request) :    # 'request' name is convention. It can be some other name too.
#    return render(request, 'index.html')

from django.shortcuts import render
from django.http import HttpResponse
clicked=0
nam='rohan'
fruits=['mango','banana','apple','guava']

def index(request) :
    global clicked

    my_dict = { 'inject_var' : clicked}
    clicked ++
    return render(request,'index.html',context=my_dict)

def help(request) :
    return render(request, 'help.html')

def name(request) :
    name_1 = { 'name_3' : nam }
    return render(request, 'index.html', context=name_1)

def loop(request) :
    loop_1 = { 'fruit' : fruits}
    return render(request, 'index.html',context=loop_1)
