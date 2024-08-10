from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def odd_or_even(request, num):
    try:
        num = int(num)
        if num % 2 == 0:
            return HttpResponse(f"Your number {num} is even")
        else:
            return HttpResponse(f"Your number {num} is odd")
    except:
        return ValueError("wrong input")
    