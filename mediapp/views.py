from django.shortcuts import render, redirect, get_object_or_404

from mediapp.models import Appointment, contact


# Create your views here.

def home(request):
    return render(request,'index.html')

def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def departments(request):
    return render(request,'departments.html')

def doctors(request):
    return render(request,'doctors.html')

def appoint(request):
   if request.method == 'POST':
       myappointments = Appointment(
           name=request.POST['name'],
           email=request.POST['email'],
           phone=request.POST['phone'],
           date=request.POST['date'],
           department=request.POST['department'],
           doctor=request.POST['doctor'],
           message=request.POST['message']
       )

       myappointments.save()
       return redirect('/show')

   else:

      return render(request,'appointment.html')







def cont(request):
   if request.method == 'POST':
       mycontact = contact(
           name=request.POST['name'],
           email=request.POST['email'],
           subject=request.POST['subject'],
           message=request.POST['message']

       )

       mycontact.save()
       return redirect('/contact')

   else:

      return render(request,'contact.html')

def show(request):
    return render(request,'show.html')

def show(request):
    all = Appointment.objects.all()
    return render(request,'show.html',{'all':all})

def delete(request,id):
    deleteappointment = Appointment.objects.get(id=id)
    deleteappointment.delete()
    return redirect('/show')



def edit(request,id):
    appointment = get_object_or_404(Appointment,id=id)
    if request.method == 'POST':
        appointment.name = request.POST['name']
        appointment.email = request.POST['email']
        appointment.phone = request.POST['phone']
        appointment.date = request.POST['date']
        appointment.department = request.POST['department']
        appointment.doctor = request.POST['doctor']
        appointment.message = request.POST['message']
        appointment.save()
        return redirect('/show')
    else:return render(request,'edit.html',{'appointment':appointment})


