from django.urls import path

from mypage import views
from mypage.views import MyProfileView, MyLessonView, MyLessonReviewView, MyHelpersView, MyEventView, MyMessageListView, \
    MyMessageDetailView, MyMessageWriteView, MyPayView, MyEventDeleteView, MyHelpersDeleteView, MyMessageSendListView, \
    MyMessageDeleteView, MyMessageSendDeleteView, MyLessonDeleteView

app_name = 'mypage'

urlpatterns = [
    # 프로필
    path('profile/', MyProfileView.as_view(), name='myprofile'),
    # 과외 매칭
    path('lesson/', MyLessonView.as_view(), name='mylesson_init'),
    path('lesson/<int:page>/', MyLessonView.as_view(), name='mylesson_page'),
    path('lesson/<str:keyword>/', MyLessonView.as_view(), name='mylesson_find'),
    path('lesson/tab/<str:status>/', MyLessonView.as_view(), name='mylesson_status'),
    path('lesson/delete/<int:helpers_id>/', MyLessonDeleteView.as_view(), name='mylesson_delete'),
    path('lesson/<str:keyword>/<int:page>/', MyLessonView.as_view(), name='mylesson_list'),
    # 과외 리뷰
    path('lesson-review/', MyLessonReviewView.as_view(), name='mylesson-review'),
    # 헬퍼스
    path('helpers/', MyHelpersView.as_view(), name='myhelpers_init'),
    path('helpers/<int:page>/', MyHelpersView.as_view(), name='myhelpers_page'),
    path('helpers/<str:keyword>/', MyHelpersView.as_view(), name='myhelpers_find'),
    path('helpers/tab/<str:status>/', MyHelpersView.as_view(), name='myhelpers_status'),
    path('helpers/delete/<int:helpers_id>/', MyHelpersDeleteView.as_view(), name='myhelpers_delete'),
    path('helpers/<str:keyword>/<int:page>/', MyHelpersView.as_view(), name='myhelpers_list'),
    # 이벤트
    path('event/', MyEventView.as_view(), name='myevent_init'),
    path('event/<int:page>/', MyEventView.as_view(), name='myevent_page'),
    path('event/<str:keyword>/', MyEventView.as_view(), name='myevent_find'),
    path('event/tab/<str:status>/', MyEventView.as_view(), name='myevent_status'),
    path('event/<int:page>/<str:keyword>/<str:status>/', MyEventView.as_view(), name='myevent_status_save'),
    path('event/delete/<int:event_id>/', MyEventDeleteView.as_view(), name='myevent_delete'),
    path('event/<str:keyword>/<int:page>/', MyEventView.as_view(), name='myevent_list'),
    # 쪽지
    path('message-list/', MyMessageListView.as_view(), name='message-list-init'),
    path('message-list/<str:keyword>/', MyMessageListView.as_view(), name='message-list'),
    path('message-list/<str:keyword>/<int:page>', MyMessageListView.as_view(), name='message-list-page'),
    path('message-send-list/', MyMessageSendListView.as_view(), name='message-send-list-init'),
    path('message-send-list/<str:keyword>/', MyMessageSendListView.as_view(), name='message-send-list'),
    path('message-send-list/<str:keyword>/<int:page>', MyMessageSendListView.as_view(), name='message-send-list-page'),
    path('message/delete/<int:id>', MyMessageDeleteView.as_view(), name='message-delete'),
    path('message/send/delete/<int:id>', MyMessageSendDeleteView.as_view(), name='message-send-delete'),
    path('message-detail/', MyMessageDetailView.as_view(), name='message-detail'),
    path('message-write/', MyMessageWriteView.as_view(), name='message-write'),
    # 결제
    path('pay/', MyPayView.as_view(), name='mypay'),
]
