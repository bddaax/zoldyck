from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152304',
        'name': 'Brenda Po Lok Fahida',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)