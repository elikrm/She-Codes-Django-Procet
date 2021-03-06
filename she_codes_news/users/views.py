# from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.http import HttpResponse

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'
    def success(self):
        request = self.request
        return HttpResponse('successfully uploaded')   

class ViewProfile(generic.DetailView):
    model = CustomUser
    template_name = 'ProfileInfo/Profile.html'
    context_object_name = 'ProfileInfo'
    def get_object(self):
        return CustomUser.objects.all()
   