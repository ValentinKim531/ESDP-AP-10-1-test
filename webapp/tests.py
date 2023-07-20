from django.urls import reverse
from django.utils import timezone
from .models import Events, TypeEvents
from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Account


class EventDetailViewTest(TestCase):
    def setUp(self):
        type_events = TypeEvents.objects.create(events_name='Test Type Event')
        self.event = Events.objects.create(
            name='Test Event',
            number_of_seats=50,
            description='Test event description',
            events_at=timezone.now(),
            price=10.00,
            type_events=type_events
        )

    def test_get_context_data(self):
        url = reverse('events_detail', kwargs={'pk': self.event.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['event'], self.event)

        total_seats = self.event.number_of_seats
        booked_seats = self.event.resident_booked.count()
        available_seats = total_seats - booked_seats

        self.assertEqual(response.context['available_seats'], available_seats)

    def test_template_used(self):
        url = reverse('events_detail', kwargs={'pk': self.event.pk})
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'event_detail.html')


class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


class ProfileDetailViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser@example.com', email='testuser@example.com',
                                                         password='12345')
        self.account = Account.objects.create(first_name='John', last_name='Doe')

    def test_profile_detail_view(self):
        url = reverse('account_detail', kwargs={'pk': self.account.pk})
        self.client.login(email=self.user.email, password='12345')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile_detail.html')
        self.assertContains(response, self.account.first_name)
        self.assertContains(response, self.account.last_name)


class NewslineViewTestCase(TestCase):
    def test_auth_required(self):
        response = self.client.get(reverse('newsline'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))