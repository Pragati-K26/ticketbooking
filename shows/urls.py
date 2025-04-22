from django.urls import path
from .views import show_list, book_ticket, booking_history

urlpatterns = [
    path('', show_list, name='show_list'),
    path('book/<int:show_id>/', book_ticket, name='book_ticket'),
    path('history/', booking_history, name='booking_history'),
]
