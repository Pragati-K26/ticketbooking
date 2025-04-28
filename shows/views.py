from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Show, Booking
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

# Show List View - CBV
class ShowListView(ListView):
    model = Show
    template_name = 'show_list.html'
    context_object_name = 'shows'

# Book Ticket View - CBV
class BookTicketView(LoginRequiredMixin, DetailView, FormView):
    model = Show
    template_name = 'book_ticket.html'
    context_object_name = 'show'
   
    def form_valid(self, form):
        show = self.get_object()
        tickets = form.cleaned_data['tickets']
        if show.available_seats >= tickets:
            Booking.objects.create(user=self.request.user, show=show, num_tickets=tickets)
            show.available_seats -= tickets
            show.save()
            return redirect('booking_history')
        else:
            return HttpResponseForbidden("Not enough available seats.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show'] = self.get_object()
        return context

# Booking History View - CBV
class BookingHistoryView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking_history.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)
