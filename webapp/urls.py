from django.urls import path
from webapp.views.events import EventDetailView, EventsCreateView, EventsUpdateView
from webapp.views.newsline import NewslineView
from webapp.views.profile import ProfileListView, ProfileDetailView
from webapp.views.admin_request import AdminRequestListView, AdminRequestDetailView, AdminRequestCreateView, \
    AdminRequestUpdateView, AdminRequestDeleteView, AdminResponseView

urlpatterns = [
    path('newsline/', NewslineView.as_view(), name="newsline"),
    path('accounts/', ProfileListView.as_view(), name='account_list'),
    path('accounts/<int:pk>/', ProfileDetailView.as_view(), name='account_detail'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='events_detail'),
    path('events/create/', EventsCreateView.as_view(), name='events_create'),
    path('events/update/<int:pk>/', EventsUpdateView.as_view(), name='events_update'),
    path('requests/', AdminRequestListView.as_view(), name='request_list'),
    path('requests/<int:pk>', AdminRequestDetailView.as_view(), name='request_detail'),
    path('requests/create/', AdminRequestCreateView.as_view(), name='request_create'),
    path('requests/update/<int:pk>', AdminRequestUpdateView.as_view(), name='request_update'),
    path('requests/delete/<int:pk>', AdminRequestDeleteView.as_view(), name='request_delete'),
    path('requests/response/<int:pk>', AdminResponseView.as_view(), name='request_response'),
]
