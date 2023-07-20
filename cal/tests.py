from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.utils.datetime_safe import date

from cal.views import CalendarView


class CalendarViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.maxDiff = None

    def test_get_context_data(self):
        url = reverse('calendar')
        request = self.factory.get(url)
        view = CalendarView.as_view()

        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, ['calendar.html', 'webapp/events_list.html'])

        # Проверка наличия ожидаемых ключей в контексте
        self.assertIn('cal', response.context_data)
        self.assertIn('prev_month', response.context_data)
        self.assertIn('next_month', response.context_data)
        self.assertIn('events_today', response.context_data)

    def test_get_date(self):
        view = CalendarView()

        # Тестирование без передачи значения месяца
        self.assertEqual(view.get_date(None), date.today())

        # Тестирование с передачей значения месяца
        test_month = '2023-07'
        expected_date = date(2023, 7, 1)
        self.assertEqual(view.get_date(test_month), expected_date)

    def test_prev_month(self):
        view = CalendarView()
        test_date = date(2023, 7, 1)

        # Получение предыдущего месяца
        prev_month = view.prev_month(test_date)
        expected_month = 'month=2023-6'
        self.assertEqual(prev_month, expected_month)

    def test_next_month(self):
        view = CalendarView()
        test_date = date(2023, 7, 1)

        # Получение следующего месяца
        next_month = view.next_month(test_date)
        expected_month = 'month=2023-8'
        self.assertEqual(next_month, expected_month)
