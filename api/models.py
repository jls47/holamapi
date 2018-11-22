from django.db import models
import random
# Create your models here.

class ProgramRequest(models.Model):
	PROGRAM_CHOICES = (
		('exscrape', 'excursions'),
		('portscrape', 'ports'),
	)
	REGION_CHOICES = (
		('Ports',(
			('alaska', 'Alaska'),
			('asia', 'Asia'),
			('australia-south-pacific', 'Australia & South Pacific'),
			('canada-new-england', 'Canada & New England'),
			('caribbean', 'Caribbean'),
			('cuba', 'Cuba'),
			('europe', 'Europe'),
			('grand-voyages', 'Grand Voyages'),
			('hawaii-tahiti', 'Hawaii & Tahiti'),
			('mediterranean', 'Mediterranean'),
			('mexico', 'Mexico'),
			('northern-europe', 'Northern Europe'),
			('pacific-coast', 'Pacific Coast'),
			('panama-canal', 'Panama Canal'),
			('south-america-antarctica', 'South America & Antarctica'),
			('transatlantic', 'Transatlantic'),
		)
		),
		('Excursions',(
			('alaska', 'Alaska & Yukon'),
			('asia', 'Asia'),
			('australia-south-pacific', 'Australia & South Pacific'),
			('denali-1-day-at-denali', 'Alaska Denali, 1 Day at Denali'),
			('denali-2-days-at-denali', 'Alaska Denali, 2 Days at Denali'),
			('denali-3-days-at-denali', 'Alaska Denali, 3 Days at Denali'),
			('denali-yukon-2-days-at-denali', 'Alaska Denali + Yukon - 2 Days At Denali'),
			('denali-yukon-3-days-at-denali', 'Alaska Denali + Yukon - 3 Days At Denali'),
			('glacier-bay-national-park', 'Alaska/Glacier Bay National Park'),
			('hubbard-glacier', 'Alaska/Hubbard Glacier'),
			('tracy-arm-sawyer-glacier', 'Alaska Tracy Arm / Sawyer Glacier'),
			('canada-new-england', 'Canada & New England'),
			('caribbean-eastern', 'Caribbean Eastern'),
			('caribbean-southern', 'Caribbean Southern'),
			('caribbean-tropical', 'Caribbean Tropical'),
			('caribbean-western', 'Caribbean Western'),
			('caribbean', 'Caribbean'),
			('cuba', 'Cuba'),
			('caribbean-cuba', 'Caribbean/Cuba'),
			('caribbean-panama-canal', 'Caribbean/Panama Canal'),
			('europe', 'Europe'),
			('grand-asia-australia', 'Grand Asia & Australia'),
			('grand-south-america-antarctica', 'Grand South America & Antarctica'),
			('hawaii-tahiti', 'Hawaii & Tahiti'),
			('mediterranean', 'Mediterranean'),
			('mexico', 'Mexico'),
			('northern-europe', 'Northern Europe'),
			('pacific-coast', 'Pacific Coast'),
			('panama-canal', 'Panama Canal'),
			('south-america-antarctica', 'South America & Antarctica'),
			('south-america', 'South America'),
			('south-america-antarctica', ''),
			('transatlantic', 'Transatlantic'),
			('world-cruise', 'World Cruise'),
			)
		)
	)
	
	LANG_CHOICES = (
		('en_US', 'English'),
		('es_ES', 'Spanish'),
		('de_DE', 'German'),
		('nl_NL', 'Dutch'),
	)

	program = models.CharField(
		choices=PROGRAM_CHOICES,
		default='exscrape',
		max_length=100
	)

	region = models.CharField(
		choices=REGION_CHOICES,
		max_length=100
	)

	language = models.CharField(
		choices = LANG_CHOICES,
		max_length=100
	)
	
	status = models.CharField(
		choices = (
			('ns', 'Not started (do not touch)'),
			('ip', 'In progress'),
			('fn', 'Finished'),
			('x', 'Canceled')
		),
		default='ns',
		max_length=100
	)
	
	email = models.EmailField(
		max_length=254
	)

	id = models.CharField(
		primary_key =True,
		max_length = 4,
		default=random.randint(0, 9999)
	)

	time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s, %s, %s, %s, %s, %s, %s' % (self.program, self.region, self.language, self.email, self.id, self.status, self.time)