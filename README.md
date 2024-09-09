## [E-Commerce app for PBP 2024 / 2025](../)

# ZOLDYCK


Zoldyck is an advanced application that connects you with premium detective services, offering a range of investigative solutions tailored to your unique needs. Leveraging the extraordinary skills and extensive experience of each member of the Zoldyck family, this app enables you to tackle complex issues with high efficiency and accuracy.

Each Zoldyck family member possesses specialized expertise, making them a master in their respective fields. This provides you with access to a variety of detective services, from in-depth investigations to covert surveillance, and from rapid case resolutions to strategic sabotage. Zoldyck delivers solutions crafted to solve mysteries and uncover truths in the most effective way.

Zoldyck is the ideal choice for those seeking not only reliable but also innovative detective services, bringing a cutting-edge and trustworthy approach to the world of investigations.

## Deployment

Experience Zoldyck in action by visiting our live application: [Explore Zoldyck App](http://brenda-po-zoldyck.pbp.cs.ui.ac.id). Dive into the world of detective services and see how our app can assist you with your investigative needs.




# [Langkah-langkah Pengimplementasian]
### 1. Membuat sebuah proyek Django baru

Langkah pertama adalah inisialisasi proyek Django baru. Untuk memulai, jalankan perintah berikut di terminal atau command prompt:

```bash
django-admin startproject nama_proyek
```

Perintah ini akan membuat struktur direktori dasar yang dibutuhkan untuk proyek Django, termasuk folder proyek utama dan berkas konfigurasi penting seperti `manage.py`, `settings.py`, `urls.py`, dan `wsgi.py`. Struktur dasar ini akan membantu dalam pengaturan dan pengembangan aplikasi Django.

### 2. Membuat aplikasi dengan nama `main` pada proyek tersebut

Setelah proyek Django dibuat, langkah selanjutnya adalah membuat aplikasi di dalam proyek tersebut. Aplikasi ini akan berisi semua logika dan fitur yang akan dikembangkan. Jalankan perintah berikut untuk membuat aplikasi baru dengan nama "main":

```bash
python manage.py startapp main
```

Perintah ini akan menghasilkan folder `main/` yang berisi berkas-berkas seperti `models.py`, `views.py`, `urls.py`, dan `admin.py`. Aplikasi ini akan menjadi unit kerja utama untuk fitur-fitur yang ingin kamu implementasikan dalam proyek.

### 3. Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`

Untuk memastikan aplikasi "main" dapat dijalankan, kamu perlu menambahkan routing dalam berkas `urls.py` di direktori proyek. Tambahkan rute berikut untuk mengarahkan permintaan ke aplikasi "main":

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Mengarahkan rute ke aplikasi 'main'
]
```

Dengan menambahkan baris `path('', include('main.urls'))`, kamu mengarahkan semua permintaan ke aplikasi `main`, sehingga aplikasi ini bisa diakses melalui URL root dari proyek.

### 4. Membuat model pada aplikasi `main` dengan nama `Product` dan atribut wajib

Di dalam aplikasi "main", buatlah model `Product` yang akan mewakili entitas produk. Buka berkas `models.py` di folder `main/` dan definisikan model tersebut dengan atribut yang wajib seperti `name`, `price`, dan `description`:

```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name
```

- `name`: Nama produk dengan panjang maksimum 255 karakter.
- `price`: Harga produk yang disimpan dalam format desimal dengan maksimal 10 digit dan 2 digit desimal.
- `description`: Deskripsi produk dalam format teks panjang.

Model ini digunakan untuk menyimpan data produk ke dalam database.

### 5. Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML

Untuk menampilkan informasi di web, buat fungsi dalam berkas `views.py` di aplikasi `main`. Fungsi ini akan merender template HTML dengan nama aplikasi, nama kamu, dan kelas:

```python
from django.shortcuts import render

def home(request):
    context = {
        'app_name': 'Zoldyck',
        'your_name': 'Brenda',
        'class_name': 'Platform-Based Programming'
    }
    return render(request, 'home.html', context)
```

Fungsi `home` ini akan menggunakan `render` untuk menghasilkan halaman HTML dari template `home.html`, menyertakan konteks yang berisi nama aplikasi, nama kamu, dan kelas.

### 6. Membuat sebuah routing pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`

Di dalam folder `main/`, buka atau buat berkas `urls.py`. Tambahkan rute baru untuk memetakan URL ke fungsi `home` yang telah dibuat:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Dengan menambahkan `path('', views.home, name='home')`, URL root dari aplikasi `main` akan diarahkan ke fungsi `home`, memungkinkan pengguna mengakses halaman tersebut.

### 7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet

Setelah aplikasi siap, langkah berikutnya adalah melakukan deployment ke Pacil Web Service (PWS). Proses ini melibatkan mengunggah proyek ke server PWS. Langkah-langkah umum meliputi:

1. **Persiapkan berkas yang diperlukan**: Pastikan berkas `requirements.txt` berisi semua dependensi proyek dengan perintah:
   ```bash
   pip freeze > requirements.txt
   ```
2. **Buat berkas `Procfile`** di direktori utama proyek dengan konten:
   ```text
   web: gunicorn nama_proyek.wsgi
   ```
3. **Ikuti panduan PWS** untuk mengunggah dan mengonfigurasi proyek, yang biasanya mencakup pembuatan aplikasi baru di PWS dan pengaturan konfigurasi.

### 8. Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-deploy

Terakhir, buat berkas `README.md` di direktori proyek. Berisi deskripsi proyek, langkah-langkah implementasi, serta tautan menuju aplikasi yang sudah di-deploy. Format berkas `README.md` sebagai berikut:

```markdown
# Zoldyck: Platform-Based Programming Project

## Deskripsi Proyek
Zoldyck adalah aplikasi inovatif yang menawarkan berbagai layanan detektif. Aplikasi ini dirancang untuk membantu pengguna menemukan solusi untuk berbagai masalah investigasi.

## Langkah Pengimplementasian
Langkah-langkah rinci untuk pengaturan dan deployment proyek dapat ditemukan di atas.

## Deployment
Akses versi live dari aplikasi di sini: [Zoldyck App](http://brenda-po-zoldyck.pbp.cs.ui.ac.id).
```

Dengan mengikuti langkah-langkah di atas, kamu akan dapat mengimplementasikan dan mendokumentasikan proyek Django dengan detail yang diperlukan.

<br>
<br>
REV: Sat 07 Sep 2024 21:00
<hr>
