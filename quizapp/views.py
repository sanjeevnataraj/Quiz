from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from .forms import RegistrationPageForm
from .models import User
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib import messages



# Create your views here.


def homepage(request,*args,**kwargs):
    print(request,args,kwargs)
    return render(request,'home.html',{})

class LoginPage(TemplateView):
    template_name = "login.html"
    def get(self,request,*args,**kwargs):
        return super().get(self,request,*args,**kwargs)
    
    def post(self,request,*args,**kwargs):
        return super().post(self,request,*args,**kwargs)

class RegistrationPage(CreateView):
    form_class = RegistrationPageForm
    model = User
    template_name = 'signup.html'
    success_url = reverse_lazy('quizapp:login')

    def form_valid(self,form):
        context = self.get_context_data()
        if form.is_valid():
            form = form.save(commit=False)
            form.set_password(self.request.POST.get('password'))
            form.save()
            messages.success(self.request, 'User Added successfully')
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render(self.request, 'signup.html', context)

    def get_context_data(self, **kwargs):
        context = super(RegistrationPage, self).get_context_data(**kwargs)
        if self.request.method == "GET":
            context['form'] = RegistrationPageForm()
        else:
            context['form'] = RegistrationPageForm(self.request.POST)
        return context
         