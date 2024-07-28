from django.urls import reverse
import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from students.models import Course, Student


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):

        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_course(api_client, course_factory):

    course = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course.id})
    response = api_client.get(url)
    assert response.data['id'] == course.id
    assert response.data['name'] == course.name
    assert response.status_code == 200

@pytest.mark.django_db
def test_list_courses(api_client, course_factory):
    url = reverse('courses-list')
    courses = course_factory(_quantity=3)
    response = api_client.get(url)
    for i, c in enumerate(response.data):
        assert c['id'] == courses[i].id
        assert c['name'] == courses[i].name
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_course(api_client):
    url = reverse('courses-list')
    response = api_client.post(url, data={'name': 'test'}, format='json')
    assert response.data['name'] == 'test'
    assert response.status_code == 201

@pytest.mark.django_db
def test_update_course(api_client, course_factory):

    course = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course.id})
    if course.name == 'test':
        course.name = 'test2'
        course.save()
    response = api_client.patch(url, data={'name': 'test'}, format='json')
    assert response.data['name'] == 'test'
    assert response.status_code == 200

@pytest.mark.django_db
def test_delete_course(api_client, course_factory):
    course = course_factory()
    url = reverse('courses-detail', kwargs={'pk': course.id})
    response = api_client.delete(url)
    assert response.status_code == 204

@pytest.mark.django_db
def test_filter_course_by_id(api_client, course_factory):

    course = course_factory()
    url = reverse('courses-list')
    response = api_client.get(url, data={'id': course.id}, format='json')
    assert response.data[0]['id'] == course.id
    assert response.status_code == 200

@pytest.mark.django_db
def test_filter_course_by_name(api_client, course_factory):
    url = reverse('courses-list')
    course = course_factory()
    response = api_client.get(url, data={'name': course.name}, format='json')
    assert response.data[0]['name'] == course.name
    assert response.status_code == 200
