from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from main.models import Test
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import AuthenticationForm, authenticate
from django.contrib.auth import login, logout

from users.forms import SignUpForm, UpdateForm
from users.models import Saved, User


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account successfully created")
            return redirect('login')
        return render(request, 'registration/signup.html', {'form': form})




class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form':form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        return render(request, 'registration/login.html', {'form':form})




class ProfileView(View):
    def get(self, request, id):
        user = request.user
        saveds = Saved.objects.filter(author_id=id)
        my_quizzes = Test.objects.filter(author_id=user.id)

        context = {
        'saveds':saveds,
        'my_quizzes': my_quizzes,
        'user':user
        }

        return render(request, 'registration/profile.html', context)





class UpdateProfile(LoginRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UpdateForm(instance=user)
        return render(request, 'profile_update.html', {'form': form})

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = UpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', id=user.id)
        return render(request, 'profile_update.html', {'form': form})




class DeleteProfile(View):
    def get(self, request, id):
        user  = get_object_or_404(User, id=id)
        return render(request, 'profile_delete.html', {'user':user})
    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        if user:
            user.delete()
            return redirect('index')
        return render(request, 'profile_delete.html')


class LogoutView(View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        return render(request, 'log_out.html', {'user':user})

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        logout(request)
        return redirect('index')
