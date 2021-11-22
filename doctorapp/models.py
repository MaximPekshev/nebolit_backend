from django.db import models

class PhoneCheck(models.Model):

	phone = models.CharField(max_length = 11, verbose_name = 'Телефон')
	code = models.CharField(max_length = 4, verbose_name = 'Код')
	cleared = models.BooleanField(verbose_name='Погашен', default=False)

	def __str__(self):
		return '{}'.format(self.id)


	class Meta:
	    verbose_name = 'Проверка телефонов'
	    verbose_name_plural = 'Проверка телефона'



