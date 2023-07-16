from datetime import datetime
from django.db.models import Q
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
        query = Q(Q(event=self.object.pk))
        events_booked = UserBooked.objects.filter(query).first()
        context['events_booked'] = events_booked
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
        query = Q(resident=user) | Q(event=event)
        events_booked = UserBooked.objects.filter(query).first()
        events_booked.delete()
        return redirect('newsline')


