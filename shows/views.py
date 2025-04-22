from django.shortcuts import render, redirect, get_object_or_404
from .models import Show, Booking
from django.contrib.auth.decorators import login_required

def show_list(request):
    shows = Show.objects.all()
    return render(request, 'show_list.html', {'shows': shows})

@login_required
def book_ticket(request, show_id):
    show = get_object_or_404(Show, pk=show_id)
    if request.method == 'POST':
        tickets = int(request.POST['tickets'])
        if show.available_seats >= tickets:
            Booking.objects.create(user=request.user, show=show, num_tickets=tickets)
            show.available_seats -= tickets
            show.save()
            return redirect('booking_history')
    return render(request, 'book_ticket.html', {'show': show})

@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_history.html', {'bookings': bookings})
