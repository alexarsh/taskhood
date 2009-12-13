from django.shortcuts import render_to_response


def index(request):
    return render_to_response("index.html", locals())
           #load index.html from templates folder
           #this view creates an array of variables avialable in HTML
        
def main(request):
    return render_to_response("main.html", locals())