from django.shortcuts import render
from rest_framework.views import APIView
import pyshorteners

# Create your views here.
class UrlShortener(APIView):
    def post(self, request):
        long_url = request.data['url']
        shortener = pyshorteners.Shortener()
        shortened_url = shortener.tinyurl.short(url)
        return shortened_url


