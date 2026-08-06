from django.urls import path
from . import views

urlpatterns = [
  path("quotes/", views.QuoteListCreate.as_view(), name = "quote-view-create")
]
