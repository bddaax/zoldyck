## [E-Commerce app for PBP 2024 / 2025](../)

# ZOLDYCK


Zoldyck is an advanced application that connects you with premium detective services, offering a range of investigative solutions tailored to your unique needs. Leveraging the extraordinary skills and extensive experience of each member of the Zoldyck family, this app enables you to tackle complex issues with high efficiency and accuracy.

Each Zoldyck family member possesses specialized expertise, making them a master in their respective fields. This provides you with access to a variety of detective services, from in-depth investigations to covert surveillance, and from rapid case resolutions to strategic sabotage. Zoldyck delivers solutions crafted to solve mysteries and uncover truths in the most effective way.

Zoldyck is the ideal choice for those seeking not only reliable but also innovative detective services, bringing a cutting-edge and trustworthy approach to the world of investigations.

## Deployment

Experience Zoldyck in action by visiting our live application: [Explore Zoldyck App](http://brenda-po-zoldyck.pbp.cs.ui.ac.id). Dive into the world of detective services and see how our app can assist you with your investigative needs.

<br>
<br>
<hr>

# Langkah-langkah Pengimplementasian
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
<hr>

# PERTANYAAN

### Fungsi Git

Git berfungsi sebagai sistem kontrol versi yang sangat penting dalam pengembangan perangkat lunak. Dengan Git, pengembang dapat melacak setiap perubahan yang dilakukan pada kode sumber secara terperinci. Hal ini memungkinkan mereka untuk melihat riwayat lengkap perubahan, termasuk siapa yang membuat perubahan, kapan perubahan tersebut dibuat, dan alasan di balik perubahan itu. Git mendukung kerja tim dengan menyediakan fitur cabang (branch) yang memungkinkan pengembang untuk mengerjakan fitur baru atau perbaikan bug secara terpisah dari kode utama (master branch). Cabang-cabang ini dapat digabungkan (merged) kembali ke kode utama dengan aman setelah fitur atau perbaikan selesai dan diuji. Selain itu, Git memudahkan proses rollback, yaitu mengembalikan kode ke versi sebelumnya jika terjadi kesalahan atau masalah, yang membantu meminimalkan risiko dan kerusakan pada proyek. Dengan fitur seperti konflik penyatuan (merge conflicts) yang terkelola dengan baik dan kemampuan untuk membandingkan versi kode, Git membantu menjaga integritas kode dan memastikan kolaborasi yang efisien di antara tim pengembang dalam proyek yang kompleks dan dinamis.

### Mengapa Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Django sering dipilih sebagai framework pengenalan dalam pembelajaran pengembangan perangkat lunak karena beberapa alasan utama. Pertama, Django dirancang untuk mendukung pengembangan cepat (rapid development) dengan mengutamakan efisiensi dan produktivitas. Framework ini mengikuti arsitektur Model-View-Template (MVT), yang memisahkan tanggung jawab dalam pengembangan aplikasi web sehingga pemula dapat lebih mudah memahami konsep dasar seperti routing, templating, dan manajemen basis data tanpa terjebak dalam kode yang berlebihan. Django juga menyediakan berbagai fitur bawaan yang mempermudah pengelolaan aplikasi, seperti sistem autentikasi pengguna, antarmuka admin yang otomatis, dan sistem migrasi basis data. Dokumentasi Django yang lengkap dan komunitas yang aktif menyediakan banyak sumber daya belajar, tutorial, dan forum dukungan, membuatnya lebih mudah bagi pemula untuk mendapatkan bantuan dan memahami framework ini. Selain itu, Django mengutamakan keamanan dengan fitur-fitur seperti perlindungan terhadap serangan Cross-Site Request Forgery (CSRF) dan SQL Injection, yang mengajarkan praktik keamanan yang penting dalam pengembangan web.

### Mengapa Model pada Django Disebut ORM (Object-Relational Mapping)?

Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena ia menyediakan cara untuk memetakan objek Python ke dalam struktur tabel basis data relasional secara langsung. ORM memungkinkan pengembang untuk bekerja dengan database menggunakan objek Python, tanpa harus menulis kueri SQL yang kompleks dan rawan kesalahan secara langsung. Dengan ORM, setiap model Django diwakili sebagai kelas Python, dan atribut dari kelas tersebut otomatis dipetakan ke kolom dalam tabel basis data. Fitur ini mengabstraksi detail teknis dari interaksi dengan basis data, membuat pengelolaan data menjadi lebih sederhana dan kode lebih mudah dipahami dan dirawat. ORM juga menyediakan fitur untuk migrasi basis data, yang memungkinkan perubahan pada model kode untuk diterapkan ke struktur basis data dengan mudah. Dengan cara ini, ORM memastikan konsistensi antara model kode dan tabel basis data, serta mengurangi potensi kesalahan dalam pengelolaan data. Secara keseluruhan, ORM mempermudah pengembang untuk bekerja dengan data dalam format yang lebih intuitif dan terintegrasi dengan bahasa pemrograman Python.



<br>
<br>
REV: Sat 07 Sep 2024 21:00
<hr>
