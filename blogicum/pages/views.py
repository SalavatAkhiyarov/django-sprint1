from django.shortcuts import render


def about(request):
    template_name = 'pages/about.html'
    return render(request, 'pages/about.html')


def rules(request):
    return render(request, 'pages/rules.html')
