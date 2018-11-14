from tastypie.resources import ModelResource
from api.models import ProgramRequest


class ProgramRequestResource(ModelResource):
	class Meta:
		queryset = ProgramRequest.objects.all()
		resource_name = 'program_request'