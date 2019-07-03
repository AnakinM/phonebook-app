from django.http import HttpResponse
from django.shortcuts import render
from .models import Person

# Show all contacts
def contact_list_view(request):
    # What I did here is that I put myself a challenge to fit in, suggested in task, database models.
    # Normally I couldn't access Phone and Email fields from Person object, as
    # foreign key of Person is in both Phone and Email, not the other way (Phone and Email as
    # foreign keys being in Person). So I followed relationship "backward" like you can see down here.
    # As list of contacts is small, this loop don't steal much execution time. Yet, I'd take a different 
    # approach in designing database models to avoid making such loops.

    contacts = Person.objects.all() 
    for contact in contacts:
        contact.phone = contact.phone_set.get(person=contact).phone
        contact.email = contact.email_set.get(person=contact).email
    
    template = "contacts/list.html"
    context = {"contacts": contacts}
    return render(request, template, context)

# Show specific contact
def contact_detail_view(request, id):
    contact = Person.objects.get(pk=id)
    contact.phone = contact.phone_set.get(person=contact).phone
    contact.email = contact.email_set.get(person=contact).email
    template = "contact/details.html"
    context = {"contact": contact}
    return render(request, template, context)

# Add new contact
def contact_add_view(request):
    return HttpResponse("<h1>Contact Add View</h1>")

# Edit contact
def contact_update_view(request, id):
    return HttpResponse("<h1>Contact Update View</h1>")

# Delete contact
def contact_delete_view(request, id):
    return HttpResponse("<h1>Contact Delete View</h1>")


