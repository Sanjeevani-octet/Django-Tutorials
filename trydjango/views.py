""""
To render HTML Webpages
"""
from django.http import HttpResponse
import random

def home_view(request):
    """ Here take in a request and return Html as a response"""
    name="SANJEEVANI"
    number = random.randint(100, 200)
    HTML_STRING= f"""<H1>Hello {name} - {number} !!!</H1>"""
    return HttpResponse(HTML_STRING)