from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework.views import APIView

# Create your views here.
class QuoteListCreate(generics.ListCreateAPIView):
  queryset = Quote.objects.all()
  serializer_class = QuoteSerializer

  def delete(self, request, *args, **kwargs):
    Quote.objects.all().delete()
    return Response(status = "status.HTTP_204_NO_CONTENT")

class QuoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
  queryset = Quote.objects.all()
  serializer_class = QuoteSerializer
  lookup_field = "pk"

class QuoteList(APIView):
  def get(self, request, format=None):
    quote = request.query_params.get("quote", "")

    if quote:
      quotes = Quote.objects.filter(quote__icontains=quote)
    else:
      quotes = Quote.objects.all()

    serializer = QuoteSerializer(quotes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)