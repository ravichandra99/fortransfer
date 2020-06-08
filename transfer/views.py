from django.shortcuts import render,redirect
from django.http import HttpResponse
from transfer.forms import BaseForm,OTPAuthenticationForm
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from transfer.models import JustBase
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.
class index(FormView):
	template_name = 'index.html'
	form_class = BaseForm

	def form_valid(self, form):
		instance = form.save()
		return redirect('transfer:detail', pk=instance.id)
	
	

class detail(DetailView):
	model = JustBase

class update(UpdateView):
	model = JustBase
	fields = '__all__'

	def form_valid(self, form):
		instance = form.save()
		return redirect('transfer:detail', pk=instance.id)

def thanks(request,pk):
	o = JustBase.objects.get(id = pk)
	email = o.email
	sotp = random.randrange(100000,999999)
	request.session['otp'] = sotp
	form = OTPAuthenticationForm()
	send_mail(
    'Subject here',
    'Here is the OTP {}'.format(sotp),
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,)
	context = {'form':form,'sotp':sotp}
	return render(request,'thanks.html',context)

	






