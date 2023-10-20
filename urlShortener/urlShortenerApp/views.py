import random, requests
from django.shortcuts import redirect, render
from django.http import HttpResponseNotFound, HttpResponseServerError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import UrlShortener


## LANDING PAGE
def index(request):
    return render(request, 'index.html')


## VIEW TO CREATE NEW SHORT URL
@api_view(['POST'])
def makeUrlShort(request):
    data = request.data
    s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!*^$-_"
    shortUrl = ("".join(random.sample(s, 6)))
    original_url = data['url']

    urlValid = validateUrl(original_url)
    
    if urlValid is False:
        return HttpResponseServerError("INVALID URL: Please verify the url you submitted is active.")
    
    # ## SAVE THE NEW SHORTENED URL TO THE DB WITH THE ORIGINAL URL
    newShortUrl = UrlShortener(original_url=original_url, shortened_url=shortUrl)
    newShortUrl.save()

    short_url = "http://localhost:8000/"+shortUrl
    return Response({'originalUrl': original_url, 'shortUrl': short_url})

## REDIRECT URL BASED ON SHORT URL
@api_view(['GET'])
def redirectUrl(request, shortUrl):
    data = request.data
    try:
        urlObject = UrlShortener.objects.get(shortened_url=shortUrl)
    except:
        return HttpResponseNotFound("Short URL not found.")
    return redirect(urlObject.original_url)


## PREVENTS SHORTENING OF FAKE URLS
def validateUrl(url):
    print(url)
    try:
        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False