from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# types of msgs
'''
   messages.debug
   messages.info
   messages.success
   messages.warning
   messages.error

'''

# Create your views here.


def register(request):
    # passing form as context, the value we passsed here is this instnce form of usercreationfor
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your Account is now created, You are able to Log In Now!')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
