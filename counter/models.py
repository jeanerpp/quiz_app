from django.db import models


class Counter(models.Model):
	value = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"Counter(value={self.value})"
