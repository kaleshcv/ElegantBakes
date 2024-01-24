from django.shortcuts import render

# Create your views here.


def homePage(request):

    return render(request, 'index.html')

def contactSubmit(request):
    if request.method == "POST":
        cname = request.POST.get("name")
        cphone = request.POST.get("phone")
        cemail = request.POST.get("email")
        cbusiness = request.POST.get("business")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

    else:
        pass
    