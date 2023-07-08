from datetime import timedelta, datetime
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Guards
from .forms import GuardsRegisterForm, GuardsRegisterModificationForm   

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def guard_registration_view(request):
    """definición del comportamiento de la pantalla de registro de clientes"""

    user = request.user

    if request.POST:
        
        form = GuardsRegisterForm(request.POST,user=user)

        if form.is_valid():
            guard = form.save(commit=False)
        
            guard.save()
            
    

            return redirect('guard_succeed')
        
        else:
            context = {
                'guard_form' : form
            }
    else:
        form = GuardsRegisterForm(user=user)

        context = {
                'guard_form' : form
                }
        
    return render(request, 'guard_form.html', context)







def guard_register_succeed(request):
    return render(request, 'guard_succeed.html')

@login_required
def guard_register_modification(request, guard_id):

    guard = Guards.objects.get(id=guard_id)

    if request.POST:
        form = GuardsRegisterModificationForm( request.POST, instance=guard,user=request.user)
        if form.is_valid():
            form.save()
            return redirect('guard_register_modification_succeed', guard_id)
    else:
        form = GuardsRegisterModificationForm(
            initial = {
                'vet': guard.vet,
                'address': guard.address,
                'date_of_guards': guard.date_of_guards,
                
                
            },
            instance=guard,
            user=request.user,
        )
        form = GuardsRegisterModificationForm(user=request.user,instance=guard)
    
    context = {
        'guard_register_modification_form': form,
    }

    return render(request, 'guard_register_modification_form.html', context)


@login_required
def guard_register_modification_succeed(request, guard_id):
    return render(request, 'guard_register_modification_succeed.html', {'guard_id': guard_id})


def guards_calendar(request):

    
    guards = Guards.objects.all

    context = {
        'guards': guards,
    }

    return render(request, 'guards_calendar.html', context)

def guard_detail(request, guard_id):
    
        guard = Guards.objects.get(id=guard_id)
    
        context = {
            'guard': guard,
        }
    
        return render(request, 'guard_detail.html', context)


def guard_delete(request, guard_id):
    """borrado de guardia"""
    guard = Guards.objects.get(pk=guard_id)
    guard.delete()
    return redirect('guards_calendar')

