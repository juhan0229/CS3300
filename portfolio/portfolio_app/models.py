from django.db import models
from django.urls import reverse



# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(blank=True)
	#Define default String to return the name for representing the Model object."
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('project-detail', args=[str(self.id)])


class Portfolio(models.Model):
	title = models.CharField(max_length=200)
	contact_email = models.CharField(max_length=200)
	is_active = models.BooleanField(default=False)
	about = models.TextField(blank=True)

	# create one-to-one relationship with Student and Project
	# student = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
	projects = models.ManyToManyField('Project', blank=True)

	def get_absolute_url(self):
		return reverse('portfolio-detail', args=[str(self.id)])
	def __str__(self):
		return self.title

class Student(models.Model):
	#List of choices for major value in database, human readable name
	MAJOR = [
	('CSCI-BS', 'BS in Computer Science'),
	('CPEN-BS', 'BS in Computer Engineering'),
	('BIGD-BI', 'BI in Game Design and Development'),
	('BICS-BI', 'BI in Computer Science'),
	('BISC-BI', 'BI in Computer Security'),
	('CSCI-BA', 'BA in Computer Science'),
	('DASE-BS', 'BS in Data Analytics and Systems Engineering')
	]
	name = models.CharField(max_length=200)
	email = models.CharField("UCCS Email", max_length=200)
	major = models.CharField(max_length=200, choices=MAJOR)
	# create one-to-one relationship with Portfolio
	portfolio = models.OneToOneField('Portfolio', on_delete=models.CASCADE, null=True, blank=True)

	#Define default String to return the name for representing the Model object."
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('student-detail', args=[str(self.id)])



