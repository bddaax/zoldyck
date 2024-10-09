import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import strip_tags

from django.shortcuts import render, redirect, reverse, get_object_or_404
from main.forms import ProductEntryForm
from .models import Product

from django.http import HttpResponse
from django.core import serializers

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@login_required(login_url='/login')
def show_model(request):
    products = Product.objects.filter(user=request.user)
    context = {
        'products': products,
        'nama_saya': 'Brenda Po Lok Fahida',
        'kelas': 'PBP D',
        'npm': '2306152304',
        'app_name': 'Zoldyck Detective Services',
        'user': request.user,
        'last_login': request.COOKIES.get('last_login', 'No login record found'),
    }
    return render(request, 'main.html', context)

def create_product_form(request):
    if request.method == "POST":
        form = ProductEntryForm(request.POST, request.FILES)
        print("Form is valid:", form.is_valid())
        if not form.is_valid():
            print("Form errors:", form.errors)
            print("Files in request:", request.FILES)

        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_model')
    else:
        form = ProductEntryForm()

    context = {'form': form}
    return render(request, 'create_product_form.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_model"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")     


def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductEntryForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('main:product_detail', product_id=product.id)
    else:
        form = ProductEntryForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id) 
    product.delete()
    return redirect('main:show_model')

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product}) 

@csrf_exempt
@require_POST
def add_product_ajax(request):
    try:
        # Log the incoming data
        print("Received POST data:", request.POST)
        print("Received FILES:", request.FILES)

        name = strip_tags(request.POST.get("name"))
        price = strip_tags(request.POST.get("price"))
        description = request.POST.get("description")
        service = request.POST.get("service")
        experience = request.POST.get("experience")
        rating = request.POST.get("rating")
        stock = request.POST.get("stock")
        photo = request.FILES.get("photo")
        user = request.user

        new_product = Product(
            name=name,
            price=price,
            description=description,
            service=service,
            experience=experience,
            rating=rating,
            stock=stock,
            user=user
        )

        new_product.save() 

        if photo:
            new_product.photo = photo
            new_product.save()

        # Return the new product data as JSON
        return HttpResponse(
            serializers.serialize('json', [new_product]),
            content_type='application/json',
        )
    
    except Exception as e:
            print("Error:", str(e))
            return HttpResponse(str(e), status=500)