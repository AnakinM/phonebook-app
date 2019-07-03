from django.urls import path

from .views import (
    contact_list_view,
    contact_detail_view,
    contact_add_view,
    contact_update_view,
    contact_delete_view,
)

urlpatterns = [
    path('', contact_list_view),
    path('contact/<int:id>/', contact_detail_view),
    path('contact/new/', contact_add_view),
    path('contact/<int:id>/edit', contact_update_view),
    path('contact/<int:id>/delete', contact_delete_view),
]