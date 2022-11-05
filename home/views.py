from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html",{"key1":228,"key2":"number"})
def home1(request):
    return render(request,"index1.html")
def home2(request):
    return render(request,"index2.html")
def home3(request):
    return render(request,"index3.html")
def reviews(request):
    return render(request,"reviews.html")             