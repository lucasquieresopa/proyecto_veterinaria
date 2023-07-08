from django.shortcuts import render, redirect
#from .forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserModificationForm, CustomResetPasswordForm, CustomPasswordChangeForm
# from django.views import generic
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from .models import Appointment
from django.utils.crypto import get_random_string
from django.core.mail import EmailMessage
from accounts.models import CustomUser 
from dogs.models import *
from django.views.generic import View
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.core.mail import send_mail
from .forms import MiVariableForm
from django.contrib.auth.decorators import login_required
from pages.email_sending import send_mail_to_user
from .forms import EmailForm, ReprogramEmailForm

@login_required
def shifts_panel_view(request):
    today = datetime.today()
    new_date = today.replace(year=2023, month=1, day=1)
    minDate = today.strftime('%Y-%m-%d')
    minNewDate = new_date.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=360)
    deltatimeold = today - timedelta(days=1)
    strdeltatimeold = deltatimeold.strftime('%Y-%m-%d')
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    maxOldDate = strdeltatimeold
    #Only show the Appointments 21 days from today
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day','time')
    items_old = Appointment.objects.filter(day__range=[minNewDate, maxOldDate]).order_by('day','time')
    if request.method == 'POST':
        description = request.POST.get('description')
        redirect('shifts_panel')

    return render(request, 'shifts_panel.html', {
        'items':items,'items_old':items_old,
    })

def shift_delete(request, shift_id):
    """borrado de turno"""
    shift = Appointment.objects.get(pk=shift_id)
    shift.delete()
    return redirect('shifts_panel')


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y

def validWeekday(days):
    #Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays
    
def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if Appointment.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays

def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x

def checkEditTime(times, day, id):
    #Only show the time of the day that has not been selected before:
    x = []
    appointment = Appointment.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if Appointment.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x



def confirmAppointment(request, id):
    appointment = Appointment.objects.get(pk=id)
    appointment.status = "Confirmado"
    appointment.mandado = "1"
    appointment.save()

    return redirect('shifts_panel')




def cancelAppointment(request, id):
    appointment = Appointment.objects.get(pk=id)
    appointment.status = "Cancelado"
    appointment.mandado = "1"
    appointment.save() 
    return redirect('shifts_panel')



@login_required
def views_calendar(request, id):    
    
    user_owner = CustomUser.objects.get(pk=id)
    dogs = user_owner.dog_set.all()

    context = {
        'user': user_owner,
        'dogs_shown': dogs.filter(hidden=False),
    }
    
    
    return render(request, 'calendar.html',context)



@login_required
def save_appointment(request,id):
    user = request.user
    today = datetime.now()
    strtoday = today.strftime("%Y-%m-%d")
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        #dog = request.POST.get('dog')
        dog_id = request.POST.get('dog')
        if  dog_id != "null":
            dog = user.dog_set.get(pk=dog_id)
   
        #print(dog)
       
        if date > strtoday :
            # Guardar la cita en la base de datos
            if  dog_id != "null":
                AppointmentForm = Appointment.objects.get_or_create(
                                user=user,
                                day=date,
                                time=time,
                                dog=dog,
                            )
            else: 
                AppointmentForm = Appointment.objects.get_or_create(
                                user=user,
                                day=date,
                                time=time,
                                
                            )

        
            # Redirigir a una página de éxito o a otra vista
                #messages.success(request, 'turno a confirmar por la veterinaria')
            return redirect('shift_succeed')
        else:
                messages.success(request, 'Horario no disponible. Por favor elija otro')
                return redirect('calendar', id)
       
    return render(request, 'calendar.html')


def shift_peticion_succeed(request):
    return render(request, 'shift_succeed.html')




def save_descriptionMandado(request, id):
    
    if request.method == 'POST':
        description = request.POST.get('description')
        appointment = Appointment.objects.get(pk=id)
        appointment.mandado = "3"
        appointment.save()    

        if description != None:
            # Guardar la cita en la base de datos
            AppointmentForm = Appointment.objects.filter(pk=id).update(
                                description=description,
            )
        
            # Redirigir a una página de éxito o a otra vista
            messages.success(request, 'Mensaje guardado correctamente')
            return redirect('shifts_panel')
        else:
                messages.success(request, 'Escribe el mensaje antes de guardar')
       
    return render(request, 'shifts_panel.html')



def send_confirmation_message_view(request, id):
    
    shift = Appointment.objects.get(pk=id)

    if request.POST:
        form = EmailForm(request.POST)
        if form.is_valid():
            shift.description = form.cleaned_data['message']
            if shift.dog == None:
                        send_mail_to_user('Turno aceptado', 
                         f"El turno pedido para su perro el día {shift.day}, horario {shift.time} fue aceptado \nMensaje de la veterinaria: {form.cleaned_data['message']}",
                        "ohmydog@gmail.com", 
                        [shift.user.email])
            else:  
                       send_mail_to_user('Turno aceptado', 
                         f"El turno pedido para el perro {shift.dog}  el día {shift.day}, horario {shift.time} fue aceptado \nMensaje de la veterinaria: {form.cleaned_data['message']}",
                        "ohmydog@gmail.com", 
                        [shift.user.email])
            shift.save()
            return redirect('confirmation_mail_sent', id)
    else:
        form = EmailForm()

    context = {
        'message_form' : form,
    }
        
    return render(request, 'send_confirmation.html', context)



def send_rejection_message_view(request, id):

    shift = Appointment.objects.get(pk=id)

    if request.POST:
        form = EmailForm(request.POST)
        if form.is_valid():
            shift.description = form.cleaned_data['message']
            if shift.dog == None:
                    send_mail_to_user('Turno rechazado', 
                        f"El turno pedido para su perro el día {shift.day}, horario {shift.time} fue rechazado \nMotivo: {form.cleaned_data['message']}",
                        "ohmydog@gmail.com", 
                        [shift.user.email])
            else:
                send_mail_to_user('Turno rechazado', 
                        f"El turno pedido para el perro {shift.dog} el día {shift.day}, horario {shift.time} fue rechazado \nMotivo: {form.cleaned_data['message']}",
                        "ohmydog@gmail.com", 
                        [shift.user.email])  


            
           
            shift.save()
            return redirect('rejection_mail_sent', id)
    else:
        form = EmailForm()

    context = {
        'message_form' : form,
    }
        
    return render(request, 'send_rejection.html', context)


def confirmation_mail_sent(request, id):
    appointment = Appointment.objects.get(pk=id)
    appointment.status = "Confirmado"
    appointment.mandado = "1"
    appointment.save()

    return render(request, 'mail_sent_successfully.html')

def rejection_mail_sent(request, id):
    appointment = Appointment.objects.get(pk=id)
    appointment.status = "Cancelado"
    appointment.mandado = "1"
    appointment.save()
 
    return render(request, 'mail_sent_successfully.html')



def modificate_action(request, id):
    appointment = Appointment.objects.get(pk=id)
    appointment.status = "Pendiente"
    appointment.save()
 
    return redirect('shifts_panel')


def reprogram_view(request, id):

    shift = Appointment.objects.get(pk=id)

    if request.POST:
        form = ReprogramEmailForm(request.POST)
        if form.is_valid():
            #shift = form.save(commit=False)
            print(form.cleaned_data['message'])
            shift.description = form.cleaned_data['message']
            if shift.dog == None:
                    send_mail_to_user('Turno reprogramado', 
                    f"El turno pedido para su perro el día {shift.day}, horario {shift.time} fue reprogramado para el día {form.cleaned_data['date_of_shift']}, horario {form.cleaned_data['hour']} \n\nEquipo de Oh My Dog!",
                    "ohmydog@gmail.com", 
                    [shift.user.email])
            else:
                send_mail_to_user('Turno reprogramado', 
                    f"El turno pedido para el perro {shift.dog} el día {shift.day}, horario {shift.time} fue reprogramado para el día {form.cleaned_data['date_of_shift']}, horario {form.cleaned_data['hour']} \n\nEquipo de Oh My Dog!",
                    "ohmydog@gmail.com", 
                    [shift.user.email])

            shift.day = form.cleaned_data['date_of_shift']
            shift.status = "Reprogramado"
            shift.time =  form.cleaned_data['hour']
            
            shift.save()
            return redirect('reprogram_mail_sent', id)
    else:
        form = ReprogramEmailForm()

    context = {
        'message_form' : form,
    }
        
    return render(request, 'send_reprogram.html', context)


def reprogram_mail_sent(request, id):
    return render(request, 'mail_sent_successfully.html')



@login_required
def shifts_panel_user_view(request,id):
    # creo que el codigo siguiente hace que se muestren solo los turnos 
    # entre hoy y 360 días 

    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=360)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Appointments 21 days from today
    items = Appointment.objects.filter(user=id,day__range=[minDate, maxDate]).order_by('day','time')


    return render(request, 'shifts_panel_user.html', {
        'items':items,
    })
