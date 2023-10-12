from django.shortcuts import render,redirect

from .models import Payrow
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def search_by(request):
    search = request.GET.get('search')
    if search:
        payrows = Payrow.objects.filter(
            Q(name__icontains=search) |
            Q(pay_date__icontains=search) |
            Q(base_salary__icontains=search) |
            Q(overtime__icontains=search) |
            Q(bonus__icontains=search) |
            Q(paystub__icontains=search)
        )
    else:
        payrows = Payrow.objects.all()
    return render(request,'payrowList.html',{"payrows":payrows})


def order_by(request):
    order = request.GET.get('order')
    payrows = Payrow.objects.all().order_by("-"+ order)
    order_selected = {str(order): 'btn-primary text-white'}
    context = {'payrows':payrows,'order_selected':order_selected}
    return render(request,'payrowList.html',context)



@login_required(login_url='login')
def payrow_list(request):
    if request.method == "GET":
        payrows = Payrow.objects.all()
        paginator = Paginator(payrows,3)
        page_number =request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'payrowList.html',{'page_obj':page_obj})
    
        #return render(request,'payrowList.html',{"payrows":payrows})
    
@permission_required('payrow.view_payrow',login_url='login')
def payrow_detail(request,pk):
    if request.method == "GET":
        payrows = Payrow.objects.get(id=pk)
        return render(request,'payrowDetail.html',{"payrows":payrows,"paystub_image":payrows.paystub})
    
@permission_required('payrow.add_payrow',login_url='login')
def payrow_create(request):
    if request.method == "GET":
        payrows = Payrow()
        return render(request,'payrowCreate.html',{"payrows":payrows})
    if request.method == "POST" and request.FILES['paystub']:
        name = request.POST.get('name')
        pay_date = request.POST.get('pay_date')
        base_salary = request.POST.get('base_salary')
        overtime = request.POST.get('overtime')
        bonus = request.POST.get('bonus')
        paystub = request.FILES.get('paystub')

        payrows = Payrow.objects.create(
            name = name,
            pay_date = pay_date,
            base_salary = base_salary,
            overtime = overtime,
            bonus = bonus,
            paystub = paystub
        )

        payrows.save()
        return redirect('/payrow/list/')
    
@permission_required('payrow.change_payrow',login_url='login')
def payrow_update(request,pk):
    payrows = Payrow.objects.get(id=pk)

    if request.method == "GET":
        payrows.pay_date = str(payrows.pay_date)
        return render(request,'payrowUpdate.html',{"payrows":payrows,"paystub_image":payrows.paystub})
    
    elif request.method == "POST":
        payrows.name = request.POST.get('name')
        payrows.pay_date = request.POST.get('pay_date')
        payrows.base_salary = request.POST.get('base_salary')
        payrows.overtime = request.POST.get('overtime')
        payrows.bonus = request.POST.get('bonus')
        if request.FILES.get('paystub'):
            payrows.paystub = request.FILES.get('paystub')

        payrows.save()
        return redirect('/payrow/list/')
    
@permission_required('payrow.delete_payrow',login_url='login')
def payrow_delete(request,pk):
    if request.method == "GET":
        payrows = Payrow.objects.get(id=pk)
        return render(request,'payrowDelete.html',{"payrows":payrows,"paystub_image":payrows.paystub})
    
    if request.method == "POST":
        payrows = Payrow.objects.filter(id=pk)
        payrows.delete()
        return redirect('/payrow/list/')
    


def loginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('attendancelist')
        else:
            return render(request,'login.html',{'error_message':'incorrect !'})
    
    else:
        return render(request,'login.html')
    


def logoutView(request):
    logout(request)
    return redirect('/login')