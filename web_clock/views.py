from datetime import datetime
from django.shortcuts import render


def index(request):
    return render(request, 'web_clock/web_clock.html', {'current_time': str(datetime.now())})
