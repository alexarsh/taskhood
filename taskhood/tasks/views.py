from django.shortcuts import render_to_response


def welcome(request):
    return render_to_response("welcome.html", locals())
