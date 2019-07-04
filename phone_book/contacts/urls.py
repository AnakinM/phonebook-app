from django.urls import path

from .views import (
    contact_list_view,
    contact_detail_view,
    contact_add_view,
    contact_update_view,
    contact_delete_view,
    search_view,
    set_email,
    set_phone,
)

urlpatterns = [
    path('', contact_list_view, name="contact-list"),
    path('search/', search_view, name="search-contact"),
    path('contact/<int:id>/', contact_detail_view, name="contact-details"),
    path('contact/<int:id>/email', set_email, name="set-email"),
    path('contact/<int:id>/phone', set_phone, name="set-phone"),
    path('contact/new/', contact_add_view, name="new-contact"),
    path('contact/<int:id>/edit', contact_update_view, name="edit-contact"),
    path('contact/<int:id>/delete', contact_delete_view, name="delete-contact"),
]
