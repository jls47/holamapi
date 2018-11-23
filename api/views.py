from django.shortcuts import render
from api.models import ProgramRequest
from django import forms
from .forms import ProgramRequestForm
# Create your views here.

#is setting a variable name equal to ID a bad idea?
def id_view(request, id):
	obj = ProgramRequest.objects.get(id = id)
	return render(request, 'api/status.html', {"object": obj})

def get_request_form(request):
	if request.method == "POST":
		form = ProgramRequestForm(request.POST)
		print('AAA')
		if form.is_valid():
			model_instance = form.save()
			model_instance.time = timezone.now()
			model_instance.update()
			print("Save successful")
			return HttpResponseRedirect('/api/%s' % model_instance.id)
	else:
		print('AAAAAA')
		form = ProgramRequestForm(initial={'program': ProgramRequest.program, 'region': ProgramRequest.region, 'language': ProgramRequest.language, 'email': ProgramRequest.email, 'id': ProgramRequest.id, 'status': ProgramRequest.status, 'time': ProgramRequest.time})
	return render(request, 'api/make_request.html', {'form': form})

def get_requests(request):
	requests = ProgramRequest.objects.all()
	return render(request, 'api/seeall.html', {'requests': requests, 'title': 'All Requests'})

def edit_request(request, id):
	obj = ProgramRequest.objects.get(id = id)
	if request.method == 'POST':
		form = ProgramRequestForm(request.POST, instance=obj)
		if form.is_valid():
			model_instance = form.save()
			model_instance.save()
			return HTTpResponseRedirect('/api/%s' % id)
	else:
		request = ProgramRequest.objects.get(id = id)
	return render(request, 'api/edit_request.html', {'form': form})