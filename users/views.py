from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

# Register View - CBV
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Automatically log the user in after registration
        return redirect(self.success_url)

# Custom Login View - CBV
class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('show_list')  # Redirect to 'show_list' after login

# Custom Logout View - CBV
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to login page after logout
