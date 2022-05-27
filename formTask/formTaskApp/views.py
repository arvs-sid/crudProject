from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from .forms import formDetails
from .models import basicForm

# Create your views here.

def formFunc(request):
    context = {}
    formTemplate = formDetails(request.POST)
    if formTemplate.is_valid():
        formTemplate.save()
        return redirect("/viewList")
    context['formDetails']= formTemplate
    return render(request,'formTaskApp/index.html',context)

def viewlist(request):
    context = {}
    viewListData = basicForm.objects.all()
    context['viewListData'] = viewListData
    return render(request,'formTaskApp/viewList.html',context)

def delete(request,id):
    obj = get_object_or_404(basicForm,id=id)
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/viewList")

def update(request,id):
    context ={}
    # a=basicForm.objects.get(name=listName)
    updateDetails=get_object_or_404(basicForm,id=id)
    if request.POST.get('Name') !=None and request.POST.get('Phone Number') !=None:
        updateDetails.name=request.POST.get('Name')
        updateDetails.phoneNumber=request.POST.get('Phone Number')
        updateDetails.save()
        return redirect('/viewList')
    context["updateform"] = updateDetails
    return render(request, "formTaskApp/update.html", context)
    # obj = get_object_or_404(basicForm, name = listName)
    # form = formDetails(request.POST,instance = obj)
    
    # if request.POST.get('name') !=None and request.POST.get('phoneNumber') !=None:
    #     a.name=request.POST.get('name')
    #     a.phoneNumber=request.POST.get('phoneNumber')
    #     a.save()
    #     return redirect('/viewList')
    # # elif request.POST.get('name') !=None:
    # #     a.name=request.POST.get('name')
    # #     a.save()
    # #     return redirect('/viewList')
    # # elif request.POST.get('phoneNumber') !=None:
    # #     a.phoneNumber=request.POST.get('phoneNumber')
    # #     a.save()
    # #     return redirect('/viewList')
    # else:
    #     obj = get_object_or_404(basicForm, name = listName)
    #     form = formDetails(request.POST,instance = obj)
    #     context["updateform"] = form
    #     return render(request, "formTaskApp/update.html", context)

   