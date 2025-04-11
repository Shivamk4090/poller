from django.urls import path
from .views import Home, CreatePoll, PollListView, PollDetailView, PollResultView, vote

urlpatterns =[
    path('', PollListView.as_view(), name='home'),

    path('create-poll', CreatePoll.as_view(), name='create_poll'),
 
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_detail'),

    path('poll/<int:pk>/result/', PollResultView.as_view(), name='poll_result'),
    
    path('poll/<int:poll_id>/vote/', vote, name='vote'),
]