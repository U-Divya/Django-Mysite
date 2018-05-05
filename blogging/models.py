from django.db import models

# Create your models here.
class Blog(models.Model):
	title=models.CharField(max_length=100)
	author=models.CharField(max_length=100)
	published=models.DateField()
	content=models.TextField(blank=True)
	status=models.CharField(max_length=20,blank=True,choices=(('Y','Yes'),('n','No')),default=('y','Yes'))
	def __str__(self):
		return self.title

	#One to many

class Other(models.Model):
	blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
	published_in=models.CharField(max_length=30)
	def __str__(self):
		return self.published_in

	#One to One

class Other1(models.Model):
	blog=models.OneToOneField(Blog,on_delete=models.CASCADE)
	modified_in=models.CharField(max_length=20)
	def __str__(self):
		return self.modified_in

	#many to many

class Other2(models.Model):
	blog=models.ManyToManyField(Blog)
	allpublished_in=models.CharField(max_length=10)
	def __str__(self):
		return self.allpublished_in