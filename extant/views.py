from django.shortcuts import render,redirect
from datetime import datetime
from .models import ExtantModel
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def search_by(request):
    search = request.GET.get('search')
    if search:
        extants = ExtantModel.objects.filter(
            Q(name__icontains=search) |
            Q(department__icontains=search) |
            Q(phone_number__icontains=search) |
            Q(address__icontains=search) |
            Q(salary__icontains=search) |
            Q(hire_date__icontains=search)
        )
    else:
        extants = ExtantModel.objects.all()
    return render(request,'extant_list.html',{"extants":extants})


def order_by(request):
    order = request.GET.get('order')
    extants = ExtantModel.objects.all().order_by("-"+ order)
    order_selected = {str(order): 'btn-primary text-white'}
    context = {'extants':extants,'order_selected':order_selected}
    
    return render(request,'extant_list.html',context)



@login_required(login_url='login')
def extant_list(request):
    if request.method == "GET":
        extants = ExtantModel.objects.all()

        paginator = Paginator(extants,3)#show 3 contacts per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        return render(request,'extant_list.html',{'page_obj':page_obj})
        #return render(request, 'extant_list.html',{'extants':extants})
    
@permission_required('extant.view_extantmodel',login_url='login')
def extant_detail(request,pk):
    if request.method == "GET":
        extants = ExtantModel.objects.get(id=pk)
        return render(request,'extant_detail.html',{"extants":extants})
    
@permission_required('extant.add_extantmodel',login_url='login')
def extant_create(request):
    if request.method == "GET":
        extants = ExtantModel()
        return render(request,'extant_create.html',{'extants':extants})
    
    if request.method == "POST":
        name = request.POST.get('name')
        department = request.POST.get('department')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        salary = request.POST.get('salary')
        hire_date = request.POST.get('hire_date')

        extants = ExtantModel.objects.create(
            name = name,
            department = department,
            phone_number = phone_number,
            address = address,
            salary = salary,
            hire_date = hire_date
        )

        extants.save()
        return redirect('list')
    
@permission_required('extant.change_extantmodel',login_url='login')
def extant_update(request,pk):
    extants = ExtantModel.objects.get(id=pk)

    if request.method == "GET":
        extants.hire_date = datetime.strftime(extants.hire_date, '%Y-%m-%d')
        return render(request,'extant_update.html',{"extants":extants})
    
    elif request.method == "POST":
        extants.name = request.POST.get('name')
        extants.department = request.POST.get('department')
        extants.phone_number = request.POST.get('phone_number')
        extants.address = request.POST.get('address')
        extants.salary = request.POST.get('salary')
        extants.hire_date = request.POST.get('hire_date')

        extants.save()
        return redirect('list')
    
@permission_required('extant.delete_extantmodel',login_url='login')
def extant_delete(request,pk):
    if request.method == "GET":
        extants = ExtantModel.objects.get(id=pk)
        return render(request,'extant_delete.html',{"extants":extants})
    
    if request.method == "POST":
        extants = ExtantModel.objects.filter(id=pk)
        extants.delete()
        return redirect('list')