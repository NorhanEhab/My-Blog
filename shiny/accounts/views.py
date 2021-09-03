from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         if form.is_valid():
             user = form.save()
             login(request, user)
             return redirect('articles:list')
    else:
        form = UserCreationForm()
    # this return works if the method used is get which returns the signup page
    # also works if the inputs added by the user are invalid should return to the same page
    # to add valid ones
    return render(request, 'accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user) # so if you logged in with the admin credentials you would
            # have access to the administration site
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                 return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
            logout(request)
            return redirect('articles:list')
