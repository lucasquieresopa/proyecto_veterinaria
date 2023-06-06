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

@login_required
def booking(request):
    weekdays = validWeekday(22)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        if service == None:
            messages.error(request, 'Debe seleccionar un servicio')
        return redirect('booking')
        
        request.session['day'] = day
        request.session['service'] = service

        return redirect('bookingSubmit')
    return render(request, 'booking.html', {'weekdays':weekdays, 'validateWeekdays':validateWeekdays})

@login_required
def bookingSubmit(request):
    user = request.user
    times = [
        "Mañana","Tarde"
    ]
    today = datetime.now()
    minDate = today.strftime("%Y-%m-%d")
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime("%Y-%m-%d")
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')
    # si no lo eligieron antes el turno
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get('time') 
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and  day >= minDate:
                if date != 'Sunday':
                    if Appointment.objects.filter(day=day).count() < 10:
                        if Appointment.objects.filter(day=day, time=time).count() < 10:
                            AppointmentForm = Appointment.objects.get_or_create(
                                user=user,
                                day=day,
                                time=time,
                            )
                            messages.success(request, 'Espere la confirmación de su turno por mail')
                            return redirect('home')
                        else:
                            messages.success(request, 'El horario ya está reservado')
                    else:
                        messages.success(request, 'El día está completo')
                else:   
                    messages.success(request, 'El día no está disponible')
            else:
                messages.success(request, 'La fecha no está disponible en el periodo de tiempo')
        else:
            messages.success(request, 'Debe seleccionar un servicio')
    return render(request, 'bookingSubmit.html', {'times':hour})



@login_required
def userPanel(request):
    user = request.user
    appointments = Appointment.objects.filter(user=user).order_by('day','time')
    return render(request, 'userPanel.html', {'user':user ,'appointments':appointments})



@login_required
def userUpdate(request,id):
    appointment = Appointment.objects.get(pk=id)
    userdatepicked = appointment.day

    today = datetime.now()
    minDate = today.strftime("%Y-%m-%d")

    #24 hr statemente
    delta24 = (userdatepicked).strftime("%Y-%m-%d") >= (today + timedelta(days=1)).strftime("%Y-%m-%d")
    #calling validay function loop day want in the next 21 days
    weekdays = validWeekday(22)

    #ONly show the days  that are not full
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        
                                                            
        request.session['day'] = day
        request.session['service'] = service

        return redirect('userUpdateSubmit', id=id)
    return render(request, 'userUpdate.html', {'weekdays':weekdays, 'validateWeekdays':validateWeekdays,'delta24':delta24, 'id':id})

@login_required
def userUpdateSubmit(request,id):
    user = request.user
    times = [
        "3 PM","3:30 PM","4 PM","4:30 PM","5 PM","5:30 PM","6 PM","6:30 PM","7 PM","7:30 PM","8 PM"
    ]
    today = datetime.now()
    minDate = today.strftime("%Y-%m-%d")
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime("%Y-%m-%d")
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')
    # si no lo eligieron antes el turno
    hour = checkEditTime(times, day,id)
    userSelectedTime = appointment.time
    if request.method == 'POST':
        time = request.POST.get('time') 
        date = dayToWeekday(day)

        if service != None:
            if day <= maxDate and  day >= minDate:
                if date == 'Monday' or date == 'Saturday' or date == 'Wednesday':
                    if Appointment.objects.filter(day=day).count() < 11:
                        if Appointment.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            AppointmentForm = Appointment.objects.filter(pk=id).update(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                            )
                            messages.success(request, "Appointment Edited!")
                            return redirect('home')
                        else:
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                    messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")
        return redirect('userPanel')


    return render(request, 'userUpdateSubmit.html', {
        'times':hour,
        'id': id,
    })

@login_required
def staffPanel(request):
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=360)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    #Only show the Appointments 21 days from today
    items = Appointment.objects.filter(day__range=[minDate, maxDate]).order_by('day','time')
    if request.method == 'POST':
        description = request.POST.get('description')
        redirect('staffPanel')

    return render(request, 'staffPanel.html', {
        'items':items,
    })


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
   
    messages.success(request, "Turno confirmado!") 
    asunto = "Turno para veterinaria"
    mensaje = " Nos complace informarte que tu turno agendado con el veterinario ha sido aceptado. Esperamos atenderte en la fecha y " + appointment.description + ".Si tienes alguna pregunta o requerimiento especial, no dudes en hacérnoslo saber. ¡Te esperamos con gusto!"
    remitente = 'megat01e28@gmail.com'
    destinatario=appointment.user.email
    
 
    mail = EmailMessage(
                                    asunto, 
                                 mensaje, 
                                    remitente,
                                    [destinatario]
            )
    mail.send()  


    return redirect('staffPanel')




def cancelAppointment(request, id):
    appointment = Appointment.objects.get(pk=id)
    appointment.status = "Cancelado"
    appointment.mandado = "1"
    appointment.save()
    messages.success(request, "Turno cancelado!")

    asunto = "Turno para veterinaria"
    
    mensaje = "Lamentamos informarte que tu turno agendado con el veterinario ha sido cancelado por " + appointment.description +". Por favor, ponte en contacto con nosotros para reprogramar una nueva cita. Agradecemos tu comprensión y estamos a tu disposición para cualquier consulta adicional."
    remitente = 'megat01e28@gmail.com'
    destinatario=appointment.user.email
    
  
    mail = EmailMessage(
                                    asunto, 
                                     mensaje, 
                                    remitente,
                                    [destinatario]
            )
    mail.send()  
    return redirect('staffPanel')

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
        dog = request.POST.get('dog')
        print(dog)
       
        if date > strtoday :
            # Guardar la cita en la base de datos
                AppointmentForm = Appointment.objects.get_or_create(
                                user=user,
                                day=date,
                                time=time,
                                dog=dog,
                            )
        
            # Redirigir a una página de éxito o a otra vista
                messages.success(request, 'turno a confirmar por la veterinaria')
                return redirect('home')
        else:
                messages.success(request, 'Horario no disponible. Por favor elija otro')
       



    
    return render(request, 'calendar.html')






def enviar_correo_aceptacion(destinatario):
    asunto = 'Aceptación de turno'
    mensaje = 'Su turno ha sido aceptado. ¡Esperamos verte pronto!'
    remitente = 'megat01e01'
    send_mail(asunto, mensaje, remitente, [destinatario])


def save_description(request, id):
    
    if request.method == 'POST':
        description = request.POST.get('description')

        
        

        if description != None:
            # Guardar la cita en la base de datos
            AppointmentForm = Appointment.objects.filter(pk=id).update(
                                description=description,
            )
        
            # Redirigir a una página de éxito o a otra vista
            messages.success(request, 'Mensaje guardado correctamente')
            return redirect('staffPanel')
        else:
                messages.success(request, 'Escribe el mensaje antes de guardar')
       



    
    return render(request, 'staffPanel.html')

def desbloquear(request, id):
    appointment = Appointment.objects.get(pk=id)
    appointment.mandado = "2"
    appointment.save()
    
    return redirect('staffPanel')

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
            return redirect('staffPanel')
        else:
                messages.success(request, 'Escribe el mensaje antes de guardar')
       



    
    return render(request, 'staffPanel.html')