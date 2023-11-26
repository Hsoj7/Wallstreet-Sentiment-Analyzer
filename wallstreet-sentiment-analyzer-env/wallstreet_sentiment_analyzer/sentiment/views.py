from django.http import HttpResponse
from django.template import loader


def get_sentiment(request):
    template = loader.get_template('get-sentiment.html')
    return HttpResponse(template.render())
