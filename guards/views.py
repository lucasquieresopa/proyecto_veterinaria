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
        form = GuardsRegisterModificationForm(request.POST, instance=guard,)
        if form.is_valid():
            form.save()
            return redirect('guard_register_modification_succeed')
    else:
        form = GuardsRegisterModificationForm(
            initial = {
                'vet': guard.vet,
                'address': guard.address,
                'date_of_guards': guard.date_of_guards,
                
                
            },
            instance=guard
        )
        form = GuardsRegisterModificationForm(instance=guard)
    
    context = {
        'guard_register_modification_form': form,
    }

    return render(request, 'guard_register_modification_form.html', context)


@login_required
def guard_register_modification_succeed(request):
    return render(request, 'guard_register_modification_succeed.html')


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