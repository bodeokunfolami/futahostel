from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import RegistrationForm, LogInForm, StudentProfileForm
from . models import StudentProfile
from hostels.models import Hostel, HostelApplication
from hostels.forms import HostelAppForm

def register(request):
    if request.user.is_authenticated:
        return redirect(reverse('users:dashboard'))
    form = RegistrationForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data['password'])
      user.save()
      messages.success(request, 'Registration Successful')
      url = reverse('users:login') + '?status=1'
      return redirect(url)
    return render(request, 'users/register.html', context)

def login_view(request):
    if request.user.is_authenticated:
        return redirect(reverse('users:dashboard'))
    next = request.GET.get('next')
    status = request.GET.get('status')
    form = LogInForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            try:
                student_profile = StudentProfile.objects.get(user=user)
            except StudentProfile.DoesNotExist:
                messages.info(request, 'You must complete your profile before you can apply for hostel')
                return redirect(reverse('users:edit_profile'))
            if status:
                messages.info(request, 'You must complete your profile before you can apply for hostel')
                return redirect(reverse('users:edit_profile'))
            if next:
                return redirect(next)
            return redirect(reverse('users:dashboard'))
    return render(request, 'users/login.html', context)

@login_required
def dashboard(request):
    profile = request.user.profile
    try:
        application = HostelApplication.objects.get(student=profile)
    except HostelApplication.DoesNotExist:
        application = None
    try:
        profile = StudentProfile.objects.get(user=request.user)
    except StudentProfile.DoesNotExist:
        profile = None
    context = {
        'profile': profile,
        'application': application
    }
    return render(request, 'users/dashboard.html', context)

@login_required
def hostel_app(request):
    profile = request.user.profile
    hostels = Hostel.objects.filter(hostel_type=profile.gender)
    context = {
        'hostels': hostels
    }
    return render(request, 'users/hostel_app.html', context)

@login_required
def hostel_app_detail(request, id=None):
    profile = request.user.profile
    initial_data = {
        'profile_id': profile.id
    }
    form = HostelAppForm(request.POST or None, initial=initial_data)
    hostel = get_object_or_404(Hostel, id=id)
    context = {
        'hostel': hostel,
        'form': form
    }
    if form.is_valid():
        apps = HostelApplication.objects.filter(student=profile)
        if apps.exists():
            messages.info(request, 'You cannot sumbit another application')
            return redirect(hostel.get_absolute_url())
        bed_spaces = int(form.cleaned_data['bed_spaces'])
        HostelApplication.objects.create(
            beds=bed_spaces,
            student=profile,
            hostel=hostel
        )
        messages.success(request, 'Your application has been submited')
        return redirect(hostel.get_absolute_url())


    return render(request, 'users/hostel_detail.html', context)


@login_required
def edit_pofile(request):
    try:
        student_profile = StudentProfile.objects.get(user=request.user)
        form = StudentProfileForm(request.POST or None, request.FILES or None, instance=student_profile)
    except:
        form = StudentProfileForm(request.POST or None)

    context = {
        'profile_form': form
    }
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        messages.success(request, 'Your profile was updated successfully')
        return redirect(reverse('users:edit_profile'))
    return render(request, 'users/edit_profile.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, 'You logged out')
    return redirect(reverse('users:login'))