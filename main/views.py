import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from .models import Product

from django.http import HttpResponse
from django.core import serializers

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def show_model(request):
   # Query dari database untuk model Product
    model = Product.objects.filter(user=request.user)

    # Data lengkap layanan detektif keluarga Zoldyck
    example_services = [
        {
            "name": "Silva Zoldyck",
            "service": "Powerful Case Resolution - Pemecahan Kasus Berisiko Tinggi",
            "description": "Silva berspesialisasi dalam menangani kasus yang berisiko tinggi, sering kali melibatkan konflik kekerasan dan ancaman serius.",
            "experience": "Silva telah terlibat dalam penyelesaian lebih dari 40 kasus yang melibatkan ancaman terhadap nyawa dan keamanan tinggi.",
            "price": 15000000,
            "rating": 4.8,
            "category": "Pemecahan Kasus Berisiko Tinggi",
            "stock": 1,
            "additional_experience": "Dengan kekuatan fisik yang luar biasa dan kemampuan Nen yang mematikan, Silva adalah pilihan utama untuk kasus-kasus yang memerlukan konfrontasi langsung.",
        },
        {
            "name": "Illumi Zoldyck",
            "service": "Stealthy Surveillance - Pengawasan Rahasia",
            "description": "Illumi ahli dalam pengawasan diam-diam dan infiltrasi, memungkinkan dia untuk memata-matai target tanpa terdeteksi.",
            "experience": "Illumi telah berhasil melakukan lebih dari 60 operasi pengintaian rahasia tanpa pernah terdeteksi.",
            "price": 10000000,
            "rating": 4.7,
            "category": "Pengawasan Rahasia",
            "stock": 3,
            "additional_experience": "Dengan kemampuannya mengendalikan orang lain melalui manipulasi Nen, Illumi dapat memperoleh informasi langsung dari target atau lingkungan mereka.",
        },
        {
            "name": "Killua Zoldyck",
            "service": "Quick Investigation - Penyelesaian Kasus Kilat",
            "description": "Dengan kecepatan dan kecerdasannya, Killua menawarkan penyelesaian kasus dalam waktu yang sangat singkat, ideal untuk investigasi cepat.",
            "experience": "Killua telah menyelesaikan lebih dari 100 investigasi dalam waktu kurang dari 24 jam, memanfaatkan kecepatan dan kecerdasan strategisnya.",
            "price": 8000000,
            "rating": 4.9,
            "category": "Investigasi Cepat",
            "stock": 5,
            "additional_experience": "Kecepatan luar biasa Killua dalam melakukan investigasi membuatnya sangat cocok untuk kasus darurat yang membutuhkan solusi segera.",
        },
        {
            "name": "Kikyo Zoldyck",
            "service": "Strategic Sabotage - Sabotase dan Infiltrasi",
            "description": "Kikyo menawarkan layanan sabotase strategis, dengan kemampuan menyusup dan menghancurkan operasi target secara diam-diam.",
            "experience": "Kikyo telah berhasil melakukan lebih dari 30 operasi sabotase strategis, menghancurkan operasi musuh tanpa meninggalkan jejak.",
            "price": 10000000,
            "rating": 4.5,
            "category": "Sabotase dan Infiltrasi",
            "stock": 2,
            "additional_experience": "Kikyo memiliki keahlian luar biasa dalam perencanaan jangka panjang dan infiltrasi diam-diam, ideal untuk misi yang memerlukan kehati-hatian ekstrem.",
        },
        {
            "name": "Milluki Zoldyck",
            "service": "Tech Surveillance and Hacking - Pengawasan Teknis dan Peretasan",
            "description": "Milluki menawarkan layanan pengawasan teknologi dan peretasan. Dia bisa meretas sistem keamanan atau memantau aktivitas digital target.",
            "experience": "Milluki telah meretas lebih dari 30 sistem keamanan tingkat tinggi dan membantu mengumpulkan bukti dalam investigasi yang memerlukan analisis digital.",
            "price": 8000000,
            "rating": 4.7,
            "category": "Pengawasan Teknis/Peretasan",
            "stock": 4,
            "additional_experience": "Meskipun jarang terlibat langsung di lapangan, Milluki menyediakan dukungan teknis yang sangat diperlukan dalam kasus-kasus yang melibatkan peretasan atau pelacakan digital.",
        },
        {
            "name": "Kalluto Zoldyck",
            "service": "Infiltration Expert - Penyusupan Tersembunyi",
            "description": "Kalluto ahli dalam seni infiltrasi, menggunakan teknik seni lipatan kertas untuk menyusup ke lingkungan yang tidak terdeteksi.",
            "experience": "Kalluto telah berhasil menyusup ke lebih dari 20 organisasi dan kelompok rahasia tanpa terdeteksi.",
            "price": 7500000,
            "rating": 4.6,
            "category": "Penyusupan Tersembunyi",
            "stock": 3,
            "additional_experience": "Kemampuan artistik dan keahlian Kalluto dalam seni lipatan kertas membuatnya menjadi infiltrator yang sangat sulit dideteksi, bahkan oleh target paling waspada sekalipun.",
        },
    ]

    # Tambahkan produk dari database ke layanan detektif
    for product in model:
        example_services.append({
            "name": product.name,
            "service": getattr(product, 'service', 'Tidak Ada Layanan'),
            "description": product.description,
            "experience": getattr(product, 'experience', 'Tidak Ada Pengalaman'),
            "price": product.price,
            "rating": getattr(product, 'rating', 'Tidak Ada Rating'),
            "category": getattr(product, 'category', 'Tidak Ada Kategori'),
            "stock": product.stock,
            "additional_experience": getattr(product, 'additional_experience', 'Tidak Ada Pengalaman Tambahan'),
        })

    context = {
        'nama_saya': 'Brenda Po Lok Fahida',
        'kelas': 'PBP D',
        'npm': '2306152304',
        'app_name': 'Zoldyck Detective Services',
        'services': example_services,
        'products': model, 
        'last_login': request.COOKIES['last_login'],
        'user': request.user,
    }

    return render(request, 'main.html', context)

def create_product_form(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_model')

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
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")                   