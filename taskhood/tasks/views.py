from django.shortcuts import render_to_response
from google.appengine.api import users
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    return render_to_response("index.html", locals())
           #load index.html from templates folder
           #this view creates an array of variables avialable in HTML
  
def login(request):
    user = users.get_current_user()
    if user:
        return render_to_response("main.html", locals())
    else:    
        return HttpResponseRedirect(users.create_login_url("/main"))
      
def main(request):
    return render_to_response("main.html", locals())