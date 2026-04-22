import pytest

from .models import Counter


@pytest.mark.django_db
def test_count_route_increments_counter(client):
	response_one = client.get('/count')

	assert response_one.status_code == 200
	assert Counter.objects.get(pk=1).value == 1

	response_two = client.get('/count')

	assert response_two.status_code == 200
	assert Counter.objects.get(pk=1).value == 2


@pytest.mark.django_db
def test_count_route_renders_template_and_value(client):
	response = client.get('/count')
	html = response.content.decode()

	assert response.status_code == 200
	assert any(t.name == 'counter/count.html' for t in response.templates)
	assert 'Visit Counter' in html
	assert '>1<' in html
