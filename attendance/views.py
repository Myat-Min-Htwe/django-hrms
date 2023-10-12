from django.shortcuts import render,redirect
from .models import EmployeeAttendance
from .forms import AttendanceForm
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def search_by(request):
    search = request.GET.get('search')
    if search:
        attendance = EmployeeAttendance.objects.filter(
            Q(name__icontains=search) | 
            Q(date__icontains=search) |
            Q(is_present__icontains=search) |
            Q(check_in_time__icontains=search) |
            Q(check_out_time__icontains=search)
        )
    else:
        attendance = EmployeeAttendance.objects.all()
    
    return render(request,'attendance_list.html',{'attendance':attendance})
    

def order_by(request):
    order = request.GET.get('order')
    attendance = EmployeeAttendance.objects.all().order_by("-"+ order)
    order_selected = {str(order): 'btn-primary text-white'}
    context = {'attendance': attendance, 'order_selected': order_selected}
    
    return render(request, 'attendance_list.html', context)




@login_required(login_url='login')
def attendance_list(request):
    if request.method == "GET":
        attendanceList = EmployeeAttendance.objects.all()
        paginator = Paginator(attendanceList,3)
        page_number =request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'attendance_list.html',{'page_obj':page_obj})
        
        #return render(request, 'attendance_list.html',{"attendanceList":attendanceList})
    
@permission_required('attendance.view_employeeattendance',login_url='login')
def attendance_detail(request,pk):
    if request.method == "GET":
        attendance = EmployeeAttendance.objects.get(id=pk)
        return render(request, 'attendance_detail.html',{"attendance":attendance})

@permission_required('attendance.add_employeeattendance',login_url='login')
def attendance_create(request):
    if request.method == "GET":
        form = AttendanceForm()
        return render(request,'attendance_create.html',{'form':form})
    
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            date = form.cleaned_data.get('date')
            is_present = form.cleaned_data.get('is_present')
            check_in_time = form.cleaned_data.get('check_in_time')
            check_out_time = form.cleaned_data.get('check_out_time')

            attendanceCreate = EmployeeAttendance.objects.create(
                name = name,
                date = date,
                is_present = is_present,
                check_in_time = check_in_time,
                check_out_time = check_out_time
            )
            attendanceCreate.save()
            return redirect('attendancelist')
        
@permission_required('attendance.change_employeeattendance',login_url='login')
def attendance_update(request,pk):
    attendance = EmployeeAttendance.objects.get(id=pk)

    if request.method == "GET":
        values = {
            'name': attendance.name,
            'date': attendance.date,
            'is_present': attendance.is_present,
            'check_in_time': attendance.check_in_time,
            'check_out_time': attendance.check_out_time
        }

        form = AttendanceForm(initial=values)
        context = {'form':form,'attendance':attendance}
        return render(request,'attendance_update.html',context)
    
    elif request.method == "POST":
        form = AttendanceForm(request.POST)
        
        if form.is_valid():
            attendance.name = form.cleaned_data.get('name')
            attendance.date = form.cleaned_data.get('date')
            attendance.is_present = form.cleaned_data.get('is_present')
            attendance.check_in_time = form.cleaned_data.get('check_in_time')
            attendance.check_out_time = form.cleaned_data.get('check_out_time')

            attendance.save()
            return redirect('attendancelist')
        

@permission_required('attendance.delete_employeeattendance',login_url='login')
def attendance_delete(request,pk):
    if request.method == "GET":
        attendance = EmployeeAttendance.objects.get(id=pk)
        return render(request, 'attendance_delete.html',{'attendance':attendance})
    
    if request.method == "POST":
        attendance = EmployeeAttendance.objects.filter(id=pk)
        attendance.delete()
        return redirect('attendancelist')