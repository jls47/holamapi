__author__ = 'admin'
from django.utils.text import format_lazy, slugify
from django import forms
from django.utils.translation import pgettext_lazy
from .models import ProgramRequest
from random import randint
import datetime


#self.program, self.region, self.language, self.email, self.id, self.status, self.time
class ProgramRequestForm(forms.ModelForm):
	class Meta:
		model = ProgramRequest
		fields = ('program', 'region', 'language', 'email', 'id', 'status')
		model.id = randint(0, 9999)

	def save(self):
		instance = super(ProgramRequestForm, self).save(commit=False)
		instance.save()

		return instance

class RequestEditForm(forms.ModelForm):
	class Meta:
		model = ProgramRequest
		fields = ('program', 'region', 'language', 'email', 'status')

	def save(self):
		instance = super(RequestEditForm, self).save(commit=False)
		instance.save()

		return instance