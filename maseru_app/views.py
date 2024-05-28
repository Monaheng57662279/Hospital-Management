from django.shortcuts import render
from maseru_app.models import MaseruStaffModel
from django.contrib import messages
from maseru_app.forms import StaffForms

def ShowStaff(request):
    showall = MaseruStaffModel.objects.all()
    return render(request, 'index.html', {'data': showall})

def InsertStaff(request):
    if request.method=="POST":
        if request.POST.get('name') and request.POST.get('age'):
            saverecord=MaseruStaffModel()
            saverecord.salary=request.POST.get('salary')
            saverecord.name=request.POST.get('name')
            saverecord.age=request.POST.get('age')
            saverecord.save()
            messages.success(request, 'staff' +saverecord.name+ ' is saved successfully...!')
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')

def EditStaff(request, id):
    editStaffobj=MaseruStaffModel.objects.get(id=id)
    return render(request, 'edit.html', {"MaseruStaffModel": editStaffobj})

def UpdateStaff(request, id):
    updateStaff=MaseruStaffModel.objects.get(id=id)
    form=StaffForms(request.POST, instance=updateStaff)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record Updated Successfully...!')
        return render(request, 'edit.html', {"MaseruStaffModel": updateStaff})
    
def DeleStaff(request, id):
    deleStaff=MaseruStaffModel.objects.get(id=id)
    deleStaff.delete()
    showdata=MaseruStaffModel.objects.all()
    return render(request, "index.html", {"data":showdata})


