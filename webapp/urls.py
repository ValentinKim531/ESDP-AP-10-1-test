from django.urls import path
from webapp.views.events import EventDetailView, EventsBookedView, EventsBookedDeleteView
from webapp.views.news import NewsCreateView, NewsDetail, NewsUpdateView, NewsDeleteView
from webapp.views.index import index
from webapp.views.newsline import NewslineView
from webapp.views.admin_request import AdminRequestListView, AdminRequestDetailView, AdminRequestCreateView, \
    AdminRequestUpdateView, AdminRequestDeleteView, AdminResponseView
from webapp.views.profile import ProfileListView, ProfileDetailView, json_accounts

urlpatterns = [
    path('', index, name='index'),
    path('newsline/', NewslineView.as_view(), name="newsline"),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('news/update/<int:pk>/', NewsUpdateView.as_view(), name='news_update'),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/confirm_delete/<int:pk>/', NewsDeleteView.as_view(), name='news_confirm_delete'),
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
    path('events_booked/<int:pk>', EventsBookedView.as_view(), name='events_booked'),
    path('events_booked_delete/<int:pk>', EventsBookedDeleteView.as_view(), name='events_booked_delete'),
    path('json-accounts/', json_accounts, name='json_accounts'),
]
