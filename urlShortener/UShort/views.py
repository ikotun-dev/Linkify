from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pyshorteners

# Create your views here.
class UrlShortener(APIView):
    def post(self, request):
        long_url = request.data['url']
        if long_url : 
            shortener = pyshorteners.Shortener()
            shortened_url = shortener.tinyurl.short(url)
            return Response({'short_url' : shortened_url}, status=status.HTTP_200_OK)
        else :
            return Response({'error': 'Missing long_url parameter'}, status=status.HTTP_401_UNAUTHORIZED)
            

