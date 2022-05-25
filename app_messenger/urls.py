from django.urls import path

from .views import UserProfileView, UserDetailView, SendMessagesView, MessagesView, UserSearchView, \
    UpdateDeleteMessageView, SheduledMessageView

urlpatterns = [
    # path('main/', MainView().as_view()),
    path('user/profile/', UserProfileView().as_view(), name = 'user profile'),
    path('user/detail/<int:id>/', UserDetailView().as_view(), name = 'user detail(for other users(from user_id))'),
    path('user/search/', UserSearchView().as_view(), name = 'search users from name and username'),
    path('messages/send/<int:recepient_id>/', SendMessagesView().as_view(), name = 'send message(message or files(from recepient_id))'),
    path('messages/<int:recepient_id>/', MessagesView().as_view(), name = 'all messages(from recepient_id)'),
    path('messages/put_delete/<int:id>/', UpdateDeleteMessageView.as_view(), name = 'put or delete message(from message_id)'),
    path('messages/scheduled_messages/<int:s_recepient_id>/', SheduledMessageView.as_view(), name = 'Sheduld messages')
    # path('about_us/', AboutUsView().as_view()),
]