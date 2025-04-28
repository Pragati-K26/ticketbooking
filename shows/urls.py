from django.urls import path
from .views import ShowListView, BookTicketView, BookingHistoryView

urlpatterns = [
    path('', ShowListView.as_view(), name='show_list'),
    path('book/<int:pk>/', BookTicketView.as_view(), name='book_ticket'),  # Using 'pk' as the primary key
    path('history/', BookingHistoryView.as_view(), name='booking_history'),
]
