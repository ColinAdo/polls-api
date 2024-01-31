from django.urls import path
from .views import PollList, PollDetail, ChoiceList, CreateVote

urlpatterns = [
    path("polls/", PollList.as_view(), name="poll_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="poll_detail"),
    path("choices/", ChoiceList.as_view(), name="choice_list"),
    path("vote/", CreateVote.as_view(), name="create_vote"),
]
