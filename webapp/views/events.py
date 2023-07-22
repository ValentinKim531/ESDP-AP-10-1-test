from datetime import datetime
from django.utils import timezone
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, TemplateView

from webapp.forms import EventsForm
from webapp.models import Events, UserBooked


class EventDetailView(DetailView):
    model = Events
    template_name = 'event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_seats = self.object.number_of_seats
        booked_seats = self.object.resident_booked.count()
        available_seats = total_seats - booked_seats
        context['available_seats'] = available_seats
        context['booked'] = False
        if self.request.user in self.object.resident_booked.all():
            user_booked = UserBooked.objects.get(event=self.object, resident=self.request.user)
            if user_booked.date_of_payment:
                context['user_payment'] = True
            context['booked'] = True
        data = timezone.now()
        if self.object.start_register_at and self.object.end_register_at:
            if data <= self.object.end_register_at and data >= self.object.start_register_at:
                context['data'] = True
        elif self.object.start_register_at:
            if data <= self.object.events_at and data >= self.object.start_register_at:
                context['data'] = True
        elif self.object.end_register_at:
            if data <= self.object.end_register_at:
                context['data'] = True
        else:
            if data <= self.object.events_at:
                context['data'] = True
        return context


class EventsCreateView(CreateView):
    template_name = 'create_events.html'
    model = Events
    form_class = EventsForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            gallery = form.save(commit=False)
            gallery.author = self.request.user
            form.save()
            return redirect('/newsline')
        context = {'form': form}
        return self.render_to_response(context)


class EventsUpdateView(UpdateView):
    template_name = 'events_update.html'
    model = Events
    form_class = EventsForm
    success_url = '/newsline'


class EventsBookedView(TemplateView):
    template_name = 'newsline.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        event = get_object_or_404(Events, pk=kwargs.get("pk"))
        UserBooked.objects.create(resident=user, event=event, booking_date=datetime.now())
        return redirect('newsline')


class EventsBookedDeleteView(TemplateView):
    template_name = 'event_detail.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        event = get_object_or_404(Events, pk=kwargs.get("pk"))
        events_booked = UserBooked.objects.filter(resident=user, event=event)
        events_booked.delete()
        return redirect('newsline')


class EventResidentBookingView(TemplateView):
    def get(self, request, *args, **kwargs):
        resident_booked = get_object_or_404(UserBooked, pk=kwargs.get("pk"))
        resident_booked.date_of_payment = timezone.now()
        resident_booked.save()
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


class EventsRegisterView(TemplateView):
    template_name = 'event_register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        event = get_object_or_404(Events, pk=kwargs.get("pk"))
        context['resident_booked_list'] = UserBooked.objects.filter(event=event)
        context['event'] = event
        return context
