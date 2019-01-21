from django.urls import path
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet, ChoiceList, CreateVote, UserCreate, LoginView
#from .apiviews import PollList, PollDetail, ChoiceList, CreateVote
#from .views import polls_list, polls_detail



router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')



#nested structure

urlpatterns = [
path('login/', LoginView.as_view(), name='login'),
path('users/', UserCreate.as_view(), name='user_create'),
path('polls/<int:pk>/choices/', ChoiceList.as_view(), name='choice_list'),
path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name='create_vote'),
# path('polls/', PollList.as_view(), name='polls_list'),
# path('polls/<int:pk>/', PollDetail.as_view(), name='polls_detail'),
]


urlpatterns += router.urls
