from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'skintone/home.html')


def coding(request):
    return render(request, 'skintone/coding.html')


def readmore(request):
    return render(request, 'skintone/readmore.html')


def robust(request):
    return render(request, 'skintone/robust.html')


def thankyou(request):
    return render(request, 'skintone/thankyou.html')