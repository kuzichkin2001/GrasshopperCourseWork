from django.db import models

# Create your models here.

class UserModel(models.Model):
	user_login = models.CharField(max_length=200, null=False)
	user_password = models.CharField(max_length=200, null=False)
	register_date = models.DateField(auto_now_add=True, null=False)
	first_name = models.CharField(max_length=200, null=False)
	second_name = models.CharField(max_length=200, null=False)
	middle_name = models.CharField(max_length=200)

	class Meta:
		def __str__(self):
			print(self.second_name + self.first_name + self.middle_name)

class HopperModel(models.Model):
	sprite = models.ImageField(height_field=image, width_field=image)
	step_forward = models.IntegerField(default=0)
	step_backward = models.IntegerField(default=0)

	class Meta:
		def __str__(self):
			print(self.step_forward + " steps forward and " + self.step_backward + " step backward.")