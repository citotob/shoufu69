from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm




class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')
    template_name = 'signup.html'

def logout(request):
    auth.logout(request)
    return redirect('home')

class UpdateProfile(generic.UpdateView):
    model = User
    success_url = reverse_lazy('home')
    fields=['username','email', 'first_name', 'last_name']
    template_name = 'profile.html'

@login_required(login_url='signin')
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        #form.is_superuser =  False
        #form.is_staff = False
        #form.is_active = True
        if form.is_valid() :
            form.save()
            #print("Profile Succeed")
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        #print("Profile Failed")
    else :
        form = UserUpdateForm(instance=request.user)
    
    context = {'form' : form}
    return render(request, 'profile.html', context)
