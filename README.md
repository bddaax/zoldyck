## [E-Commerce app for PBP 2024 / 2025](../)

# ZOLDYCK


Zoldyck is an advanced application that connects you with premium detective services, offering a range of investigative solutions tailored to your unique needs. Leveraging the extraordinary skills and extensive experience of each member of the Zoldyck family, this app enables you to tackle complex issues with high efficiency and accuracy.

Each Zoldyck family member possesses specialized expertise, making them a master in their respective fields. This provides you with access to a variety of detective services, from in-depth investigations to covert surveillance, and from rapid case resolutions to strategic sabotage. Zoldyck delivers solutions crafted to solve mysteries and uncover truths in the most effective way.

Zoldyck is the ideal choice for those seeking not only reliable but also innovative detective services, bringing a cutting-edge and trustworthy approach to the world of investigations.

## Deployment

Experience Zoldyck in action by visiting our live application: [Explore Zoldyck App](http://brenda-po-zoldycks.pbp.cs.ui.ac.id). Dive into the world of detective services and see how our app can assist you with your investigative needs.

<br>
<br>
<hr>

# Tugas 3

# Langkah-langkah Pengimplementasian
### 1. Persiapan dan langkah awal sebelum mengerjakan Tugas 3

Langkah pertama adalah membuat file `base.html` dalam direktori `templates`. Untuk memulai, jalankan perintah berikut di terminal atau command prompt:

```bash
touch base.html
vi base.html
```

Perintah ini akan membuat dan membuka file `base.html`, lalu kita dapat mengisi file `base.html` dengan kode berikut

```pyhon
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
  </head>

  <body>
    {% block content %} {% endblock content %}
  </body>
</html>
```

Baris-baris yang dikurung dalam `{% ... %} ` disebut dengan template tags Django. Baris-baris inilah yang akan berfungsi untuk memuat data secara dinamis dari Django ke HTML.

Kemudian, Buka `settings.py` yang ada pada direktori proyek dan carilah baris yang mengandung variabel `TEMPLATES`. Tambahkan kode pada bagian `DIRS` dengan potongan kode berikut agar berkas `base.html` terdeteksi sebagai berkas template.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Tambahkan konten baris ini
        'APP_DIRS': True,
        ...
    }
]
```

Pada subdirektori `templates` yang ada pada direktori `main`, tambahkan kode berikut pada awal dan akhir berkas `main.html`

```python
{% extends 'base.html' %}
 {% block content %}
...
...
{% endblock content %}
 ```

Tambahkan baris `import uuid ` pada bagian atas berkas `models.py`, kemudian lakukan migrasi model dengan menjalankan perintah berikut

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 2. Membuat input form untuk menambahkan objek model pada app sebelumnya

Buat berkas baru pada direktori `main` dengan nama `forms.py` untuk membuat struktur form yang dapat menerima data Object Entry baru. Tambahkan kode berikut ke dalam berkas `forms.py`.

```python
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = [ ] # Isi dengan input yang akan dimasukkan saat meng-entry objek baru 
```

Kemudian buka berkas `views.py` yang ada pada direktori `main`, kemudian tambahkan beberapa import baru pada bagian paling atas

```python
from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import Product
```

Masih di berkas yang sama, buat fungsi baru dengan nama `create_product_form` yang menerima parameter `request`. Tambahkan potongan kode di bawah ini untuk menghasilkan form yang dapat menambahkan data Object Entry secara otomatis ketika data di-submit dari form.

```python
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
```

Tambahkan import `create_product_form` pada berkas `urls.py` yang ada pada direktori `main` dan tambahkan path URL ke dalam variabel `urlpatterns` pada `urls.py` di `main` untuk mengakses fungsi yang sudah di-import.

```python
urlpatterns = [
   ...
   path('create-mood-entry', create_mood_entry, name='create_mood_entry'),
]
```

Kemudian, buat berkas baru dengan nama `create_product_form.html` pada direktori `main/templates` dan isi dengan kode berikut

```python
{% extends 'base.html' %}
{% block content %}
<h1>Add New Product</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}  <!-- Displays form fields as a table -->
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Product" />
      </td>
    </tr>
  </table>
</form>

{% endblock content %}
```

### 2.  Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.

Buka `views.py` yang ada pada direktori `main` dan tambahkan `import HttpResponse dan Serializer` pada bagian paling atas.

```python
from django.http import HttpResponse
from django.core import serializers
```

Buatlah dua fungsi baru yang menerima parameter `request` dengan nama `show_xml` dan `show_jason` dan buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada Products, dan tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dan parameter `content_type="application/xml"`.

```python
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Tambahkan import fungsi `show_xml` dan `show_json` pada berkas `urls.py`, dan tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor

```python
...
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'),
...
```

Buatlah kembali dua fungsi baru yang menerima parameter `request` dan `id` dengan nama `show_xml_by_id` dan `show_json_by_id` dan buatlah sebuah variabel di dalam fungsi tersebut yang menyimpan hasil query dari seluruh data yang ada pada Products, dan tambahkan return function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter content_type dengan value `"application/xml"` (untuk format XML) atau `"application/json"` (untuk format JSON).

```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Tambahkan import fungsi `show_xml_by_id` dan `show_json_by_id` pada berkas `urls.py`, dan tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor

```python
...
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
...
```

<br>
<br>
<hr>

# PERTANYAAN

### 1. Mengapa Kita Memerlukan Data Delivery dalam Pengimplementasian Sebuah Platform?

Data delivery adalah proses pengiriman data dari satu bagian sistem ke bagian lain atau dari server ke klien. Dalam pengimplementasian sebuah platform, terutama platform berbasis web atau aplikasi mobile, data delivery sangat penting karena:

- **Integrasi Sistem:** Data delivery memastikan bahwa berbagai komponen dari sistem yang berbeda (misalnya, backend dan frontend) dapat berkomunikasi dan berbagi data secara efisien.
- **Pengalaman Pengguna:** Pengiriman data yang cepat dan akurat meningkatkan pengalaman pengguna. Misalnya, aplikasi web yang responsif harus dapat mengirimkan dan menerima data dengan cepat untuk memastikan interaksi yang lancar.
- **Konsistensi Data:** Data delivery yang baik membantu menjaga konsistensi data di seluruh aplikasi, menghindari inkonsistensi dan konflik yang mungkin muncul ketika data diperbarui di berbagai tempat.
- **Keamanan:** Data delivery juga mencakup aspek keamanan, seperti enkripsi data saat transit, untuk melindungi informasi sensitif dari akses yang tidak sah.

### 2. XML vs. JSON: Mana yang Lebih Baik?

**XML (Extensible Markup Language)** dan **JSON (JavaScript Object Notation)** adalah dua format data yang sering digunakan untuk pertukaran data. Berikut perbandingannya:

- **JSON**:
  - **Keringkasan dan Kesederhanaan:** JSON lebih ringkas dan lebih mudah dibaca oleh manusia dan mesin dibandingkan XML. Formatnya yang sederhana membuatnya lebih efisien dalam penggunaan bandwidth.
  - **Kompatibilitas dengan JavaScript:** JSON dirancang untuk bekerja dengan JavaScript, menjadikannya pilihan yang alami untuk aplikasi web yang menggunakan JavaScript.
  - **Kinerja:** JSON umumnya lebih cepat dalam parsing dan pemrosesan karena struktur datanya yang lebih sederhana dibandingkan XML.

- **XML**:
  - **Fleksibilitas dan Ekstensi:** XML menawarkan lebih banyak fleksibilitas dalam hal mendefinisikan skema data dan bisa lebih mudah diubah untuk mendukung hierarki data yang kompleks.
  - **Dukungan Metadata:** XML mendukung metadata yang lebih kaya dan dapat menyertakan atribut pada elemen data.

**Mengapa JSON Lebih Populer?**
- **Kinerja dan Ukuran:** JSON lebih ringkas dan lebih cepat diproses, sehingga lebih efisien dalam hal penggunaan bandwidth dan waktu pemrosesan.
- **Kemudahan Penggunaan:** JSON lebih mudah dibaca dan ditulis dibandingkan XML, terutama bagi pengembang yang bekerja dengan JavaScript.
- **Kompatibilitas:** JSON lebih cocok untuk aplikasi web modern dan API karena kemudahan integrasinya dengan JavaScript dan format data yang lebih sederhana.

### 3. Fungsi dari Method `is_valid()` pada Form Django

Method `is_valid()` dalam form Django digunakan untuk memvalidasi data yang dikirimkan melalui form. Berikut penjelasannya:

- **Validasi Data:** `is_valid()` memeriksa apakah data yang dikirimkan oleh pengguna memenuhi semua aturan validasi yang ditentukan dalam form. Ini termasuk memeriksa apakah semua field yang diperlukan diisi, apakah data sesuai dengan tipe yang diharapkan, dan apakah data mematuhi aturan validasi khusus (misalnya, format email yang benar).
- **Pengembalian Status:** Jika data valid, `is_valid()` mengembalikan `True`, dan data dapat diakses melalui `form.cleaned_data`. Jika tidak valid, mengembalikan `False`, dan Anda dapat mengakses pesan kesalahan melalui `form.errors`.

### 4. Pentingnya `csrf_token` pada Form Django

**CSRF (Cross-Site Request Forgery)** adalah jenis serangan di mana penyerang dapat melakukan aksi di atas nama pengguna yang sudah masuk tanpa sepengetahuan pengguna tersebut. CSRF token adalah mekanisme keamanan yang melindungi aplikasi web dari serangan ini dengan memastikan bahwa setiap permintaan yang dilakukan kepada server berasal dari sumber yang sah.

- **Fungsi `csrf_token`:** `csrf_token` adalah token unik yang dihasilkan untuk setiap sesi pengguna. Saat form disubmit, token ini harus dikirim bersama permintaan. Server memeriksa token tersebut untuk memastikan bahwa permintaan berasal dari aplikasi web yang sah dan bukan dari sumber eksternal.
- **Risiko Tanpa `csrf_token`:** Jika `csrf_token` tidak disertakan, penyerang dapat membuat form yang tampaknya sah dan mengirimkan permintaan berbahaya yang dilakukan atas nama pengguna yang sah. Ini dapat mengakibatkan perubahan data, penghapusan data, atau tindakan lainnya yang tidak diinginkan.

**Cara Penyerang Memanfaatkan Ketidakhadiran `csrf_token`:**
- **Meniru Formulir:** Penyerang dapat membuat halaman web palsu yang meniru form asli dan mengirimkan permintaan ke server dengan menggunakan cookies dari pengguna yang sah.
- **Eksploitasi:** Dengan mengeksploitasi ketidakhadiran `csrf_token`, penyerang dapat melakukan aksi tanpa izin, seperti mengubah pengaturan pengguna atau melakukan transaksi yang tidak sah.

Menambahkan `csrf_token` ke form Django membantu memastikan bahwa permintaan yang diterima server adalah permintaan yang sah dan mencegah berbagai jenis serangan CSRF.

<br>
<br>
<hr>

# Tugas 2 

# Langkah-langkah Pengimplementasian
### 1. Membuat sebuah proyek Django baru

Langkah pertama adalah inisialisasi proyek Django baru. Untuk memulai, jalankan perintah berikut di terminal atau command prompt:

```bash
django-admin startproject nama_proyek .
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

### 7. Melakukan Deployment ke PWS terhadap Aplikasi yang Sudah Dibuat

Setelah aplikasi Django selesai dikembangkan, langkah berikutnya adalah melakukan deployment ke server PWS agar aplikasi dapat diakses oleh publik melalui Internet. Berikut langkah-langkah untuk melakukan deployment:

1. **Menambahkan URL Deployment pada ALLOWED_HOSTS**  
   Pada proyek Django kamu, buka berkas `settings.py`, dan tambahkan URL deployment PWS ke dalam daftar `ALLOWED_HOSTS`. Format URL deployment adalah `<username-sso>-<nama-proyek>.pbp.cs.ui.ac.id`. Jika username kamu mengandung titik (.), gantilah titik tersebut dengan tanda hubung (-). Misalnya, jika username kamu adalah "pak.bepe24" dan nama proyek "mentalhealthtracker", maka URL deployment menjadi `pak-bepe24-mentalhealthtracker.pbp.cs.ui.ac.id`. Tambahkan URL tersebut ke dalam `ALLOWED_HOSTS` seperti contoh berikut:
   ```python
   ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<URL deployment PWS kamu>"]
   ```
   Simpan perubahan ini dan lakukan `git add`, `git commit`, dan `git push` ke repositori GitHub kamu.

2. **Menjalankan Perintah Project Command**  
   Setelah perubahan sudah dipush ke GitHub, kembali ke halaman PWS dan jalankan perintah yang terdapat di bagian *Project Command* untuk melakukan deployment. Saat menjalankan perintah ini, akan muncul prompt yang meminta *username* dan *password*. Masukkan *credentials* yang kamu simpan sebelumnya.

3. **Mengubah Nama Branch ke Main**  
   Pastikan nama branch utamamu adalah `main` dengan menjalankan perintah berikut:
   ```bash
   git branch -M main
   ```

4. **Memeriksa Status Deployment**  
   Kembali ke halaman PWS dan pilih proyek yang baru saja kamu buat. Kamu akan melihat status deployment di halaman proyek. Jika statusnya "Building", artinya aplikasi masih dalam proses deployment. Jika statusnya "Running", aplikasi sudah berhasil dideploy dan dapat diakses di URL deployment. Kamu bisa menekan tombol "View Project" untuk mengakses aplikasi.

5. **Mengatasi Masalah HTTPS**  
   URL PWS hanya bisa diakses melalui protokol HTTP. Jika URL kamu secara otomatis menggunakan HTTPS, ubah secara manual menjadi HTTP. Jika masih mengalami masalah, coba akses URL deployment dalam *incognito mode*.

6. **Mengirim Perubahan ke PWS**  
   Jika ada perubahan pada proyek yang ingin kamu terapkan di PWS, cukup lakukan perintah `git push` sebagai berikut:
   ```bash
   git push pws main:master
   ```
   Tidak perlu menjalankan kembali perintah *Project Command*. Cukup lakukan `add`, `commit`, dan `push` untuk memperbarui deployment.

Dengan mengikuti langkah-langkah ini, aplikasi Django kamu dapat diakses secara online melalui Pacil Web Service (PWS). 

Ps : Pastikan juga untuk selalu melakukan push ke GitHub dan PWS apabila terdapat perubahan, agar tidak mengalami error (seperti saya :<)

### 8. Membuat sebuah `README.md` yang berisi tautan menuju aplikasi PWS yang sudah di-deploy

Terakhir, buat berkas `README.md` di direktori proyek. Berisi deskripsi proyek, langkah-langkah implementasi, serta tautan menuju aplikasi yang sudah di-deploy. 


Dengan mengikuti langkah-langkah di atas, kamu akan dapat mengimplementasikan dan mendokumentasikan proyek Django dengan detail yang diperlukan.

<br>
<br>
<hr>

# PERTANYAAN

### Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![22](https://github.com/user-attachments/assets/e779464a-cb8b-4f1b-9399-8c7fe99fa195)

Bagan alur request pada web aplikasi Django dimulai dari interaksi pengguna melalui browser, di mana client mengirimkan request HTTP ke server. Request ini bisa berupa berbagai jenis permintaan, seperti permintaan untuk mengakses halaman (GET) atau mengirim data (POST). Begitu request diterima oleh server, proses pengolahan dimulai di komponen **urls.py**. Pada tahap ini, Django menggunakan mekanisme routing untuk mencocokkan URL yang diminta dengan fungsi yang telah ditentukan dalam **views.py**. **URLs.py** berfungsi sebagai peta yang mengarahkan URL ke fungsi yang sesuai di views, memastikan bahwa setiap request dikirimkan ke bagian aplikasi yang benar untuk diproses lebih lanjut.

Selanjutnya, setelah URLs.py memetakan permintaan ke views yang sesuai, request tersebut diproses oleh fungsi yang ada di **views.py**. Views berperan sebagai pusat logika aplikasi. Di sini, logika bisnis diterapkan untuk menangani permintaan dari client. Jika view tersebut membutuhkan data dari database, maka ia akan berinteraksi dengan **models.py**. **Models.py** di Django bertindak sebagai ORM (Object-Relational Mapping) yang memetakan data dalam database ke objek Python. Dengan model ini, views dapat mengambil data dari database atau menyimpan data baru ke dalamnya tanpa harus menggunakan query SQL secara langsung. Hal ini sangat memudahkan pengelolaan data karena pengembang cukup berurusan dengan kode Python, sementara ORM menangani komunikasi dengan database di belakang layar.

Setelah logika diproses di views dan data yang diperlukan diambil dari models (jika diperlukan), langkah selanjutnya adalah merender tampilan untuk dikembalikan kepada client. Django menggunakan **template system** yang memungkinkan views untuk mengirim data ke berkas HTML dinamis yang ada di dalam folder **templates**. Template ini berisi markup HTML yang dapat diperkaya dengan data dinamis dari views menggunakan Django Template Language (DTL). Hasil akhirnya adalah halaman HTML yang dirender dan siap untuk ditampilkan kepada pengguna. Template ini tidak hanya menampilkan data statis tetapi juga dapat menyajikan informasi dinamis, seperti hasil pencarian, daftar produk, atau data lain yang relevan dengan permintaan pengguna.

Setelah template dirender, Django mengembalikan **HTTP response** yang berisi halaman HTML kepada browser. Browser kemudian menampilkan halaman tersebut kepada pengguna sesuai dengan tampilan yang telah dirender oleh template. Seluruh proses ini berjalan dengan sangat terstruktur, di mana setiap komponen memiliki peran masing-masing: **URLs.py** mengarahkan request, **views.py** memproses logika dan berinteraksi dengan models, **models.py** mengelola data dalam database, dan **templates** merender halaman untuk ditampilkan kepada client. Struktur ini memastikan bahwa setiap request yang masuk dapat diproses dengan efisien dan respons yang dihasilkan dapat memenuhi kebutuhan pengguna secara dinamis.


### Fungsi Git

Git berfungsi sebagai sistem kontrol versi yang sangat penting dalam pengembangan perangkat lunak. Dengan Git, pengembang dapat melacak setiap perubahan yang dilakukan pada kode sumber secara terperinci. Hal ini memungkinkan mereka untuk melihat riwayat lengkap perubahan, termasuk siapa yang membuat perubahan, kapan perubahan tersebut dibuat, dan alasan di balik perubahan itu. Git mendukung kerja tim dengan menyediakan fitur cabang (branch) yang memungkinkan pengembang untuk mengerjakan fitur baru atau perbaikan bug secara terpisah dari kode utama (master branch). Cabang-cabang ini dapat digabungkan (merged) kembali ke kode utama dengan aman setelah fitur atau perbaikan selesai dan diuji. Selain itu, Git memudahkan proses rollback, yaitu mengembalikan kode ke versi sebelumnya jika terjadi kesalahan atau masalah, yang membantu meminimalkan risiko dan kerusakan pada proyek. Dengan fitur seperti konflik penyatuan (merge conflicts) yang terkelola dengan baik dan kemampuan untuk membandingkan versi kode, Git membantu menjaga integritas kode dan memastikan kolaborasi yang efisien di antara tim pengembang dalam proyek yang kompleks dan dinamis.

### Mengapa Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Django sering dipilih sebagai framework pengenalan dalam pembelajaran pengembangan perangkat lunak karena beberapa alasan utama. Pertama, Django dirancang untuk mendukung pengembangan cepat (rapid development) dengan mengutamakan efisiensi dan produktivitas. Framework ini mengikuti arsitektur Model-View-Template (MVT), yang memisahkan tanggung jawab dalam pengembangan aplikasi web sehingga pemula dapat lebih mudah memahami konsep dasar seperti routing, templating, dan manajemen basis data tanpa terjebak dalam kode yang berlebihan. Django juga menyediakan berbagai fitur bawaan yang mempermudah pengelolaan aplikasi, seperti sistem autentikasi pengguna, antarmuka admin yang otomatis, dan sistem migrasi basis data. Dokumentasi Django yang lengkap dan komunitas yang aktif menyediakan banyak sumber daya belajar, tutorial, dan forum dukungan, membuatnya lebih mudah bagi pemula untuk mendapatkan bantuan dan memahami framework ini. Selain itu, Django mengutamakan keamanan dengan fitur-fitur seperti perlindungan terhadap serangan Cross-Site Request Forgery (CSRF) dan SQL Injection, yang mengajarkan praktik keamanan yang penting dalam pengembangan web.

### Mengapa Model pada Django Disebut ORM (Object-Relational Mapping)?

Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena ia menyediakan cara untuk memetakan objek Python ke dalam struktur tabel basis data relasional secara langsung. ORM memungkinkan pengembang untuk bekerja dengan database menggunakan objek Python, tanpa harus menulis kueri SQL yang kompleks dan rawan kesalahan secara langsung. Dengan ORM, setiap model Django diwakili sebagai kelas Python, dan atribut dari kelas tersebut otomatis dipetakan ke kolom dalam tabel basis data. Fitur ini mengabstraksi detail teknis dari interaksi dengan basis data, membuat pengelolaan data menjadi lebih sederhana dan kode lebih mudah dipahami dan dirawat. ORM juga menyediakan fitur untuk migrasi basis data, yang memungkinkan perubahan pada model kode untuk diterapkan ke struktur basis data dengan mudah. Dengan cara ini, ORM memastikan konsistensi antara model kode dan tabel basis data, serta mengurangi potensi kesalahan dalam pengelolaan data. Secara keseluruhan, ORM mempermudah pengembang untuk bekerja dengan data dalam format yang lebih intuitif dan terintegrasi dengan bahasa pemrograman Python.



<br>
<br>
<hr>
