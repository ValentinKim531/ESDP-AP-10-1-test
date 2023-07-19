from django.urls import reverse
from django.utils import timezone
from .models import Events, TypeEvents
from django.test import TestCase


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
