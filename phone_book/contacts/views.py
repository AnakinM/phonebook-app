from django.http import HttpResponse
from django.shortcuts import render

# Show all contacts
def contact_list_view(request):
    return HttpResponse("<h1>Contact List View</h1>")

# Show specific contact
def contact_detail_view(request, id):
    return HttpResponse("<h1>Contact Detail View</h1>")

# Add new contact
def contact_add_view(request):
    return HttpResponse("<h1>Contact Add View</h1>")

# Edit contact
def contact_update_view(request, id):
    return HttpResponse("<h1>Contact Update View</h1>")

# Delete contact
def contact_delete_view(request, id):
    return HttpResponse("<h1>Contact Delete View</h1>")


