from django.urls import path
from webapp.views.events import EventDetailView, EventsBookedView, EventsBookedDeleteView
from webapp.views.news import NewsCreateView, NewsDetail, NewsUpdateView, NewsDeleteView
from webapp.views.index import index
from webapp.views.newsline import NewslineView
from webapp.views.profile import ProfileListView, ProfileDetailView, json_accounts
from webapp.views.vote import VoteCreateView, VoteListCreateView, VoteOptionCreateView, VotelineView, VoteDetailView, \
    VoteBookedView

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
    path('events_booked/<int:pk>', EventsBookedView.as_view(), name='events_booked'),
    path('events_booked_delete/<int:pk>', EventsBookedDeleteView.as_view(), name='events_booked_delete'),
    path('json-accounts/', json_accounts, name='json_accounts'),
    path('vote_list/create', VoteCreateView.as_view(), name='vote_create_view'),
    path('vote/list', VoteListCreateView.as_view(), name='vote_list_create_view'),
    path('vote/option', VoteOptionCreateView.as_view(), name='vote_option_create_view'),
    path('voteline/', VotelineView.as_view(), name='voteline'),
    path('vote/detail/<int:pk>/', VoteDetailView.as_view(), name='vote_detail'),
    path('vote/user/options/<int:pk>/', VoteBookedView.as_view(), name='vote_user_options'),
]
