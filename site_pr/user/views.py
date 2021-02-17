from django.shortcuts import render, redirect
from .forms import SignUpForm, SingInFrom
from django.contrib.auth import login


def signin(request):
    if request.method == 'POST':
        form = SingInFrom(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = SingInFrom()
    return render(request, 'signin.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return redirect('/site/')
            # return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = SignUpForm()

    return render(request, 'signup.html', {'user_form': user_form})

