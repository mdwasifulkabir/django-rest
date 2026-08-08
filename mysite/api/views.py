from django.shortcuts import render
from rest_framework import generics
from .models import Quote
from .serializers import QuoteSerializer

# Create your views here.
class QuoteListCreate(generics.ListCreateAPIView):
  queryset = Quote.objects.all()
  serializer_class = QuoteSerializer

class QuoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Quote.objects.all()
  serializer_class = QuoteSerializer
  lookup_field = "pk"