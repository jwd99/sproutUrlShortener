from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import urlShortener
from .serializers import urlSerializer

import random

@api_view(['POST'])
def makeUrlShort(request):
    data = request.data

    newShortUrl = urlShortener(original_url)