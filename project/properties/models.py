from django.db import models
from user.models import User
# Create your models here.

class Properties(models.Model):
	id = models.AutoField(primary_key=True)
	building_name = models.CharField(max_length=40)
	coordinates = models.CharField(max_length=50)
	sq_ft = models.FloatField()
	bedrooms = models.FloatField()
	bathrooms = models.FloatField()
	address = models.CharField(max_length=50)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zipcode = models.IntegerField()
	past_price = models.FloatField()
	current_price = models.FloatField()
	status = models.CharField(max_length=10)
	date_upload = models.DateField()

	def __str__(self):
		return self.building_name


class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	content = models.CharField(max_length=200)
	datetime = models.DateTimeField()
	prop = models.ForeignKey(Properties, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.content


class UserProp(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	prop = models.ForeignKey(Properties, on_delete=models.CASCADE)

print('models finish, properties')