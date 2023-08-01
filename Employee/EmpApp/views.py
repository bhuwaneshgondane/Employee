from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import EmployeeM
import logging

logger = logging.getLogger("django")
# Create your views here.
def addView(request):
    template_name = "EmpApp/add.html"
    form = EmployeeForm()
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Record is added")
            return redirect('show')
    context = {'form': form }
    return render(request, template_name, context)


def showView(request):
    template_name = "EmpApp/show.html"
    object = EmployeeM.objects.all()
    logger.info("All records are shown")
    context = {'object': object }
    return render(request, template_name, context)

def updateView(request,pk):
    template_name = "EmpApp/update.html"
    obj = EmployeeM.objects.get(pk=pk)
    form = EmployeeForm(instance=obj)
    if request.method == "POST":
        form = EmployeeForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            logger.info("Record is updated")
            return redirect('show')
    context = {'form': form}
    return render(request, template_name, context)


def deleteView(request,pk):
    obj = EmployeeM.objects.get(pk=pk)
    template_name = 'EmpApp/delete.html'
    if request.method == "POST":
        obj.delete()
        logger.info("Record is deleted")
        return redirect('show')
    return render(request, template_name)