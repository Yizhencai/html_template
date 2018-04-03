from django.shortcuts import render
from django.http import HttpResponse


def index(requests):
    return render(requests, 'main/index.html')

def contact(requests):
    return render(requests, 'main/contact.html')

def about(requests):
    return render(requests, 'main/about.html')

def portfolio_detail(requests):
    return render(requests, 'main/portfolio_detail.html')

def work(requests):
    return render(requests, 'main/work.html')
