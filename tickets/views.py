from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from django.utils import timezone
from .forms import TicketForm, CommentForm
from .models import Ticket

# Create your views here.
def all_tickets(request):
    tickets = Ticket.objects.all()
    return render(request, "all_tickets.html", {"tickets": tickets})


def single_ticket(request, ticket_id):
    tickets = Ticket.objects.filter(id=ticket_id)
    return render(request, "single_ticket.html", {"tickets": tickets})
    

@login_required
def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        # If there is a feature, it goes to checkout then redirects to new_feature
        if form.is_valid() and 'feature' in request.POST['ticket_type']:

            request.session['title']       = form.cleaned_data['title']
            request.session['description'] = form.cleaned_data['description']
            request.session['priority']    = form.cleaned_data['priority']
            request.session['ticket_type'] = form.cleaned_data['ticket_type']
            
            return redirect('checkout')
        # If there is a Bug, a new ticket is created
        elif form.is_valid():
            form = form.save(commit=False)
            form.date_added = timezone.now()
            form.created_by = request.user.username
            form.save()
            messages.success(request, "Your ticket has successfully been created.")
            return redirect(reverse('index'))
    else:
        form = TicketForm()
    return render(request, 'add_ticket.html', {'form': form})



def add_feature(request):
    
    title       = request.session['title']
    description = request.session['description']
    priority    = request.session['priority']
    ticket_type = request.session['ticket_type']
    
    info = {'title': title,
            'description': description,
            'priority': priority,
            'ticket_type': ticket_type
    }
    
    if request.GET & TicketForm.base_fields.keys():
                form = TicketForm(request.GET)
    else:
        if request.method == 'POST':
            form = TicketForm(info, request.POST)
            # if the form is valid, the ticket is created. 
            if form.is_valid():
                form = form.save(commit=False)
                form.date_added = timezone.now()
                form.created_by = request.user.username
                form.save()
            # Then the entered data is removed from session.
                request.session['title'] = ''
                request.session['description'] = ''
                request.session['priority'] = ''
                request.session['ticket_type'] = ''
                    
                messages.success(request, "Your ticket has successfully been created. $30 will be charged to your card.")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to take payment.")
                return redirect(reverse('index'))
        else:
            form = TicketForm()
        return render(request, 'add_feature.html', {'form': form})


def add_comment(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user.username
            comment.created_date = timezone.now()
            comment.ticket = ticket
            comment.save()
            return redirect('ticket', ticket_id=ticket.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form})