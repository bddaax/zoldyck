from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def welcome(request):
    if request.method == 'POST':
        # Simpan nama ke dalam session dari input di halaman welcome
        request.session['name'] = request.POST.get('name')
        return redirect('main:show_model')
    return render(request, 'welcome.html')

def show_model(request):
    # Ambil nama dari session
    name = request.session.get('name', 'Guest')

    # Query dari database untuk model Product
    model = Product.objects.all()

    # Data lengkap layanan detektif keluarga Zoldyck
    example_services = [
        {
            "name": "Zeno Zoldyck",
            "service": "Dragon's Insight - Investigasi Mendalam",
            "description": "Zeno menggunakan kemampuan Nen tingkat tinggi untuk menyelesaikan investigasi kompleks dengan pendekatan analitis yang mendalam dan cepat.",
            "experience": "Zeno telah memecahkan lebih dari 50 kasus besar, termasuk investigasi lintas negara yang melibatkan organisasi kriminal besar.",
            "price": 12000000,
            "rating": 4.9,
            "category": "Investigasi Mendalam",
            "stock": 2,
            "additional_experience": "Zeno sering dipanggil untuk menangani kasus yang melibatkan organisasi kejahatan internasional dan memiliki reputasi sebagai penyelidik yang tak terkalahkan.",
        },
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

    context = {
        'name': name,
        'nama_saya': 'Brenda Po Lok Fahida',
        'kelas': 'PBP D',
        'npm': '2306152304',
        'app_name': 'Zoldyck Detective Services',
        'services': example_services,
        'products': model, 
    }

    return render(request, 'main.html', context)

def create_product_form(request):
    if request.method == 'POST':
        form = ProductEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_model')  # Redirect to model list page after saving
    else:
        form = ProductEntryForm()  # Display an empty form on GET request

    context = {'form': form}
    return render(request, 'create_product_form.html', context)

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