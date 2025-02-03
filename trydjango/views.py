""""
To render HTML Webpages
"""
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
import random

def home_view(request):
    """ Here take in a request and return Html as a response"""
    name="SANJEEVANI"
    number = random.randint(100, 200)
    # HTML_STRING= f"""<H1>Hello {name} - {number} !!!</H1>"""
    
    # first method to render from templates 
    HTML_STRING = render_to_string("home-view.html")     
    
    # second method to render from templates 
    temp = get_template("home-view.html")
    temp_string = temp.render()
    
    return HttpResponse(temp_string)