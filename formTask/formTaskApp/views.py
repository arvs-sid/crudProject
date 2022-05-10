from unicodedata import name
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .forms import formDetails
from .models import basicForm

# Create your views here.

def index(request):
    return HttpResponse("BasicForm")


def formFunc(request):
    context = {}
    formTemplate = formDetails(request.POST)
    if formTemplate.is_valid():
        formTemplate.save()
        return redirect("/viewList")
    context['formDetails']= formTemplate
    return render(request,'formTaskApp/createForm.html',context)

def viewlist(request):
    context = {}
    viewListData = basicForm.objects.all()
    context['viewListData'] = viewListData
    return render(request,'formTaskApp/viewList.html',context)

def delete(request,listName):
    context ={}
    obj = get_object_or_404(basicForm,name= listName)
    form = formDetails(request.POST,instance = obj)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/viewList")

def update(request,listName):
    context ={}
    a=basicForm.objects.get(name=listName)
    if request.POST.get('name') !=None and request.POST.get('phoneNumber') !=None:
        a.name=request.POST.get('name')
        a.phoneNumber=request.POST.get('phoneNumber')
        a.save()
        return redirect('/viewList')
    elif request.POST.get('name') !=None:
        a.name=request.POST.get('name')
        a.save()
        return redirect('/viewList')
    elif request.POST.get('phoneNumber') !=None:
        a.phoneNumber=request.POST.get('phoneNumber')
        a.save()
        return redirect('/viewList')
    else:
        obj = get_object_or_404(basicForm, name = listName)
        form = formDetails(request.POST,instance = obj)
        context["updateform"] = form
        return render(request, "formTaskApp/update.html", context)

    
    # print(obj.name)
    # for i in obj:
    #     print(i)
    
    # if form.is_valid():
    #     print("Hai")
    #     form.save()
    #     return redirect("/viewList")
    # context["updateform"] = form
    # return render(request, "formTaskApp/update.html", context)
