from django.shortcuts import render
from django.db import transaction

from .models import Counter


def count_view(request):
	with transaction.atomic():
		counter, _ = Counter.objects.select_for_update().get_or_create(pk=1)
		counter.value += 1
		counter.save(update_fields=['value'])

	return render(request, 'counter/count.html', {'count': counter.value})
