[E-Commerce app for PBP 2024 / 2025](../)


# ZOLDYCK


Zoldyck is an advanced application that connects you with premium detective services, offering a range of investigative solutions tailored to your unique needs. Leveraging the extraordinary skills and extensive experience of each member of the Zoldyck family, this app enables you to tackle complex issues with high efficiency and accuracy.

Each Zoldyck family member possesses specialized expertise, making them a master in their respective fields. This provides you with access to a variety of detective services, from in-depth investigations to covert surveillance, and from rapid case resolutions to strategic sabotage. Zoldyck delivers solutions crafted to solve mysteries and uncover truths in the most effective way.

Zoldyck is the ideal choice for those seeking not only reliable but also innovative detective services, bringing a cutting-edge and trustworthy approach to the world of investigations.

## Deployment

Experience Zoldyck in action by visiting our live application: [Explore Zoldyck App](http://brenda-po-zoldyck.pbp.cs.ui.ac.id). Dive into the world of detective services and see how our app can assist you with your investigative needs!


## Pertanyaan


<details>
  <summary><strong>Tugas 5</strong></summary>

## Langkah-langkah Pengimplementasian
### 1. Mengimplementasikan fungsi untuk menghapus dan mengedit product.

Buka `views.py` yang ada pada subdirektori `main`, dan buatlah fungsi baru bernama `edit_product` dan `delete_mod` yang menerima parameter `request` dan `id` dan tambahkan import pada bagian atas seperti berikut.

```python
from django.shortcuts import .., reverse
from django.http import .., HttpResponseRedirect

...

def edit_product(request, id):
    product = Product.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_model'))

    context = {'form': form}
    return render(request, "edit_product.html", context) 

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_model')) 
```

Lalu buatlah berkas HTML baru dengan nama `edit_product.html` pada subdirektori `main/templates`. 

```python
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="flex flex-col min-h-screen bg-gray-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Mood Entry</h1>
  
    <div class="bg-white rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
          {% csrf_token %}
          {% for field in form %}
              <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                      {{ field.label }}
                  </label>
                  <div class="w-full">
                      {{ field }}
                  </div>
                  {% if field.help_text %}
                      <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
              <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
                  Edit Product
              </button>
          </div>
      </form>
  </div>
  </div>
</div>
{% endblock %}
```

Buka `urls.py` yang berada pada direktori `main` dan import fungsi `edit_product` dan `delete_product` yang sudah dibuat dan tambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah di import.

```python
from main.views import ..., edit_mood, delete_mood

urlpatterns = [
    ...
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
]
```

Terakhir, bukalah berkas `main.html` yang ada pada folder `main/templates` dan ubahlah kode yang sudah ada menjadi seperti berikut agar terdapat tombol hapus untuk setiap produk.

```python
...
<tr>
    ...
    <td>
        <a href="{% url 'main:edit_mood' mood_entry.pk %}">
            <button>
                Edit
            </button>
        </a>
    </td>
    <td>
        <a href="{% url 'main:delete_mood' mood_entry.pk %}">
            <button>
                Delete
            </button>
        </a>
    </td>
</tr>
...
```

### 2. Membuat navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.

Buatlah berkas HTML baru dengan nama `navbar.html` pada folder `templates/` di root directory. 

```python
{% load static %}

<nav class="bg-black shadow-lg fixed top-0 left-0 z-40 w-screen">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex items-center">
        <!-- Nama Zoldyck -->
        <h1 class="text-white font-bold text-lg">Zoldyck</h1>
      </div>
      <!-- Navbar Links -->
      <ul class="hidden md:flex space-x-6">
        <li><a href="#" class="text-gray-300 text-sm hover:text-white transition duration-300">Home</a></li>
        <li><a href="#" class="text-gray-300 text-sm hover:text-white transition duration-300">Products</a></li>
        <li><a href="#" class="text-gray-300 text-sm hover:text-white transition duration-300">Cart</a></li>
        <li><a href="#" class="text-gray-300 text-sm hover:text-white transition duration-300">Contact</a></li>
      </ul>
      <!-- User Authentication Links -->
      <div class="hidden md:flex items-center space-x-4">
        {% if user.is_authenticated %}
          <!-- Welcome User and Logout Button -->
          <span class="text-gray-300 text-sm">Welcome, {{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="text-white bg-black hover:bg-gray-800 font-bold py-2 px-4 rounded transition duration-300">
            ⏻
          </a>
        {% else %}
          <!-- Login and Register Buttons -->
          <a href="{% url 'main:login' %}" class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>
      <!-- Mobile Menu Button -->
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button">
          <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Menu -->
  <div class="mobile-menu hidden md:hidden px-4 w-full">
    <ul class="space-y-1">
      <li><a href="#" class="block text-gray-300 hover:text-white py-2 px-4 rounded">Home</a></li>
      <li><a href="#" class="block text-gray-300 hover:text-white py-2 px-4 rounded">Products</a></li>
      <li><a href="#" class="block text-gray-300 hover:text-white py-2 px-4 rounded">Cart</a></li>
      <li><a href="#" class="block text-gray-300 hover:text-white py-2 px-4 rounded">Contact</a></li>
      {% if user.is_authenticated %}
        <li><span class="block text-gray-300 py-2 px-4">Welcome, {{ user.username }}</span></li>
        <li><a href="{% url 'main:logout' %}" class="block text-center text-white bg-black hover:bg-gray-800 font-bold py-2 px-4 rounded transition duration-300">
          ⏻
        </a></li>
      {% else %}
        <li><a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300">Login</a></li>
        <li><a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">Register</a></li>
      {% endif %}
    </ul>
  </div>

  <!-- Script for Mobile Menu Toggle -->
  <script>
    const btn = document.querySelector("button.mobile-menu-button");
    const menu = document.querySelector(".mobile-menu");

    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
    });
  </script>
</nav>
```

Kemudian, tautkan navbar tersebut ke dalam `main.html`, `create_mood_entry.html`, dan `edit_mood.html` yang berada di subdirektori `main/templates/` dengan menggunakan tags include:

```pyhton
{% extends 'base.html' %}
{% block content %}
{% include 'navbar.html' %}
...
{% endblock content%}
```

### 3. Kustomisasi halaman daftar product menjadi lebih menarik dan responsive.

Kustomisasi halaman login, register, dan tambah product semenarik mungkin.

**Login**
<img width="1440" alt="Screenshot 2024-10-02 at 11 24 42" src="https://github.com/user-attachments/assets/2cc0fa9a-2743-4f9f-9c0e-8aca55162033">


**Register**
<img width="1440" alt="Screenshot 2024-10-02 at 11 25 39" src="https://github.com/user-attachments/assets/f4fc1e0e-b5e9-4bff-b3c7-181a562bea9d">


**Daftar Produk**

Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
<img width="1440" alt="Screenshot 2024-10-02 at 11 28 06" src="https://github.com/user-attachments/assets/a2f15f2d-561f-4f22-8af2-e0da7eab307b">


Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card.
<img width="1440" alt="Screenshot 2024-10-02 at 11 29 31" src="https://github.com/user-attachments/assets/30c6a5d2-07c7-42b4-a966-226691fff6f4">


Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!
<img width="1440" alt="Screenshot 2024-10-02 at 11 31 20" src="https://github.com/user-attachments/assets/8c48b1bf-8eda-47b6-b6ed-06232462ecd0">


Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.

**Kondisi navbar untuk versi mobile:**
<img width="971" alt="Screenshot 2024-10-02 at 11 32 40" src="https://github.com/user-attachments/assets/c9c46728-a34d-4e81-a8fd-ec221d86bd62">
<img width="923" alt="Screenshot 2024-10-02 at 11 33 14" src="https://github.com/user-attachments/assets/3db92999-fe56-42d1-9ae2-84a32aba7087">


**Kondisi navbar untuk versi desktop:**
<img width="1440" alt="Screenshot 2024-10-02 at 11 31 57" src="https://github.com/user-attachments/assets/6428902a-b342-4a36-b22b-5921a20c0236">
<img width="1440" alt="Screenshot 2024-10-02 at 11 27 01" src="https://github.com/user-attachments/assets/63116829-7beb-40f9-879a-d0de2e6447a6">



<br>
<br>
<hr>

# PERTANYAAN

###  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!

Dalam CSS, urutan prioritas atau **CSS specificity** menentukan aturan mana yang akan diterapkan pada elemen HTML ketika ada beberapa selektor yang dapat berlaku. Setiap jenis selektor dalam CSS memiliki bobot atau nilai specific yang berbeda, dan aturan dengan specificitas yang lebih tinggi akan diutamakan. Urutan prioritas ini ditentukan oleh empat komponen utama:

1. **Inline styles**: Gaya yang langsung diterapkan di elemen HTML dengan menggunakan atribut `style`. Misalnya, `<div style="color: red;">`. Inline styles memiliki specificitas tertinggi dibandingkan selektor lain.

2. **ID selectors**: Selektor yang menggunakan ID elemen HTML dengan karakter `#` diikuti oleh nama ID, seperti `#my-id`. Selektor ID memiliki specificitas tinggi karena ID unik untuk setiap elemen.

3. **Class selectors, attribute selectors, dan pseudo-classes**: Selektor ini memiliki specificitas yang lebih rendah dibandingkan ID. Ini mencakup:
   - **Class selectors** menggunakan titik `.` diikuti nama kelas, seperti `.my-class`.
   - **Attribute selectors** menargetkan elemen dengan atribut tertentu, seperti `[type="text"]`.
   - **Pseudo-classes** menargetkan keadaan khusus elemen, seperti `:hover` atau `:nth-child(2)`.

4. **Type selectors dan pseudo-elements**: Ini adalah selektor dengan specificitas paling rendah. Mereka mencakup:
   - **Type selectors** (atau selektor elemen) menargetkan elemen HTML berdasarkan nama tag, seperti `div`, `p`, atau `h1`.
   - **Pseudo-elements** menargetkan bagian tertentu dari elemen, seperti `::before`, `::after`.


Cara Menghitung Specificity:

Specificity dinyatakan sebagai empat angka terpisah yang diurutkan secara hirarkis dari kiri ke kanan:

- Inline styles dihitung sebagai `1,0,0,0`.
- ID selectors dihitung sebagai `0,1,0,0`.
- Class selectors, attribute selectors, dan pseudo-classes dihitung sebagai `0,0,1,0`.
- Type selectors dan pseudo-elements dihitung sebagai `0,0,0,1`.

Contohnya:
- Inline style: `1,0,0,0`.
- `#my-id`: `0,1,0,0`.
- `.my-class`: `0,0,1,0`.
- `div`: `0,0,0,1`.

Jika ada beberapa aturan CSS yang berlaku untuk elemen yang sama, browser akan menerapkan aturan dengan nilai specificitas yang lebih tinggi.

Urutan Penerapan Aturan CSS (Specificity Cascade):
Jika beberapa aturan memiliki nilai specificitas yang sama, aturan yang muncul **paling akhir** dalam file CSS akan diterapkan. Jika ada beberapa aturan dengan specificitas yang berbeda, aturan dengan specificitas tertinggi akan diterapkan.

***Contoh:***
```html
<!DOCTYPE html>
<html>
<head>
  <style>
    #my-id { color: blue; }        /* ID selector */
    .my-class { color: green; }    /* Class selector */
    p { color: red; }              /* Type selector */
  </style>
</head>
<body>
  <p id="my-id" class="my-class">Hello World!</p>
</body>
</html>
```

Pada contoh di atas:
- `p` menggunakan type selector `p` dengan specificitas `0,0,0,1`.
- `.my-class` menggunakan class selector dengan specificitas `0,0,1,0`.
- `#my-id` menggunakan ID selector dengan specificitas `0,1,0,0`.

Karena specificitas ID lebih tinggi dibanding class dan type selectors, teks "Hello World!" akan berwarna **biru** meskipun ada aturan class dan type selector lainnya.

Urutan Tambahan: **!important**
Deklarasi `!important` dapat digunakan untuk memaksa aturan CSS agar memiliki prioritas tertinggi, terlepas dari specificitasnya. Namun, ini harus digunakan dengan hati-hati karena dapat membuat pengelolaan CSS lebih sulit.

***Contoh:***
```css
p { color: red !important; } /* This will override other selectors */
```

Pada kasus ini, meskipun ada aturan lain yang lebih spesifik, aturan dengan `!important` akan menang.

***Kesimpulan***
Urutan prioritas pengambilan CSS selector mengikuti specificitas yang dihitung berdasarkan:
1. Inline styles (specificitas tertinggi),
2. Selektor ID,
3. Selektor class, atribut, dan pseudo-classes,
4. Selektor elemen dan pseudo-elements (specificitas terendah).

Jika dua atau lebih selektor memiliki specificitas yang sama, aturan yang didefinisikan paling akhir dalam stylesheet akan diutamakan. `!important` akan mengesampingkan semua specificitas kecuali ada `!important` lain yang bersaing, di mana specificitas juga menjadi faktor pertimbangan.

<hr>


###  Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!

**Responsive design** adalah konsep penting dalam pengembangan aplikasi web karena memungkinkan tampilan dan fungsionalitas situs web untuk menyesuaikan secara otomatis dengan berbagai ukuran layar dan perangkat, seperti smartphone, tablet, dan desktop. Seiring dengan peningkatan akses web melalui perangkat mobile, memiliki desain yang responsif menjadi krusial untuk memberikan pengalaman pengguna yang optimal dan memastikan aplikasi web dapat diakses di mana saja dan kapan saja.

Berikut adalah beberapa alasan mengapa **responsive design** menjadi sangat penting:

1. **Peningkatan Pengalaman Pengguna (User Experience)**
   Responsive design memastikan bahwa pengguna mendapatkan tampilan dan fungsi yang sesuai dengan perangkat yang mereka gunakan. Navigasi yang lebih mudah, teks yang dapat dibaca, dan elemen interaktif yang tepat ukurannya membuat pengguna merasa nyaman dan tidak frustrasi, sehingga meningkatkan keterlibatan dan loyalitas pengguna.

2. **Fleksibilitas Lintas Perangkat**
   Dengan responsivitas, aplikasi web akan otomatis menyesuaikan tampilan dan tata letak ketika diakses dari perangkat yang berbeda, seperti laptop, tablet, atau ponsel. Ini meminimalkan kebutuhan untuk mengembangkan versi terpisah untuk perangkat mobile atau desktop, menghemat waktu dan biaya pengembangan.

3. **SEO dan Kinerja di Mesin Pencari**
   Mesin pencari seperti Google memberikan preferensi pada situs yang mobile-friendly. Dengan memiliki desain yang responsif, situs web akan mendapatkan peringkat lebih tinggi di hasil pencarian, terutama untuk pengguna yang mencari melalui perangkat mobile. Google juga menggunakan indeks mobile-first, artinya mereka terutama menilai versi mobile dari situs web.

4. **Mengakomodasi Perubahan Tren Pengguna**
   Pengguna internet saat ini mengakses konten melalui berbagai perangkat. Statistika menunjukkan bahwa jumlah pengguna internet mobile terus meningkat, sehingga desain yang hanya dioptimalkan untuk desktop akan kehilangan banyak pengunjung potensial. Desain responsif menjaga aplikasi tetap relevan seiring perubahan tren penggunaan.

5. **Efisiensi Pengembangan dan Pemeliharaan**
   Dengan hanya perlu memelihara satu versi kode yang berfungsi di semua perangkat, pengembang dapat mengurangi kompleksitas dalam pengembangan dan pemeliharaan aplikasi web. Tanpa perlu membuat dan mengelola situs terpisah untuk perangkat mobile dan desktop, proses pengembangan menjadi lebih efisien.

Contoh Aplikasi yang Menerapkan dan Tidak Menerapkan Responsive Design

1. **Aplikasi yang Sudah Menerapkan Responsive Design**:
   - **Apple**: Website resmi Apple (https://www.apple.com) merupakan contoh klasik dari situs yang menerapkan responsive design. Baik di desktop maupun mobile, website ini menyesuaikan ukuran gambar, teks, dan tata letaknya secara otomatis sehingga tetap terlihat rapi dan mudah dinavigasi di berbagai perangkat.
   - **Twitter**: Aplikasi web Twitter (https://www.twitter.com) juga sangat responsif, menyesuaikan tampilan feed, ikon, dan navigasi dengan ukuran layar yang berbeda-beda. Tampilan di smartphone tetap memberikan pengalaman yang optimal tanpa harus membuat aplikasi terpisah.

2. **Aplikasi yang Belum Menerapkan Responsive Design**:
   - **Contoh Situs Berita Lokal Lama**: Beberapa situs berita lokal lama masih belum menerapkan responsive design, sehingga ketika diakses melalui perangkat mobile, teks dan elemen-elemen situs tersebut terlalu kecil atau tata letaknya tidak sesuai. Pengguna harus melakukan zoom in dan scroll secara horizontal untuk membaca konten, yang mengakibatkan pengalaman pengguna yang buruk.
   - **Situs Web Institusi Pendidikan Tertentu**: Beberapa situs universitas atau sekolah yang menggunakan desain lama tidak responsif, sehingga saat diakses melalui perangkat mobile, tampilannya kacau, menu tersembunyi, atau elemen penting sulit diakses.

***Kesimpulan:***
Responsive design sangat penting dalam pengembangan aplikasi web modern untuk memastikan pengalaman pengguna yang baik di berbagai perangkat, meningkatkan SEO, dan menghemat biaya pengembangan serta pemeliharaan. Dengan meningkatnya akses internet melalui perangkat mobile, situs yang tidak responsif akan ketinggalan dibandingkan kompetitornya yang sudah mengadopsi desain ini.

<hr>

### Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!

**Margin**, **border**, dan **padding** adalah tiga properti penting dalam CSS yang digunakan untuk mengatur tata letak dan jarak antar elemen dalam sebuah halaman web. Masing-masing memiliki fungsi yang berbeda, namun semuanya membantu dalam mengontrol ruang di sekitar elemen.

1. **Margin**
   - **Definisi**: Margin adalah ruang kosong di luar batas (border) elemen. Margin digunakan untuk mengatur jarak antara elemen yang satu dengan elemen lainnya.
   - **Fungsi**: Mengatur jarak antar elemen di luar elemen itu sendiri. Tidak mempengaruhi ukuran elemen, hanya menambah jarak dari elemen lain di sekitarnya.
   - **Implementasi**: Anda dapat mengatur margin di semua sisi elemen (atas, kanan, bawah, kiri) atau secara spesifik untuk masing-masing sisi.
   
   **Contoh CSS:**
   ```css
   div {
     margin: 20px; /* Margin di semua sisi sebesar 20px */
   }

   p {
     margin-top: 10px;      /* Margin di sisi atas */
     margin-right: 15px;    /* Margin di sisi kanan */
     margin-bottom: 20px;   /* Margin di sisi bawah */
     margin-left: 5px;      /* Margin di sisi kiri */
   }
   ```

   **Properti Shorthand:**
   ```css
   div {
     margin: 10px 15px 20px 5px; /* Atas, kanan, bawah, kiri */
   }
   ```

2. **Border**
   - **Definisi**: Border adalah garis yang mengelilingi konten elemen dan padding. Border berada di antara padding dan margin.
   - **Fungsi**: Memberikan garis atau batas visual di sekitar elemen. Border dapat memiliki warna, ketebalan, dan gaya (seperti solid, dashed, atau dotted).
   - **Implementasi**: Border dapat diterapkan di semua sisi elemen atau hanya pada sisi-sisi tertentu (atas, kanan, bawah, kiri).

   **Contoh CSS:**
   ```css
   div {
     border: 2px solid black; /* Border semua sisi dengan ketebalan 2px, gaya solid, dan warna hitam */
   }

   p {
     border-top: 3px dashed red;    /* Border atas dengan gaya dashed */
     border-right: 5px dotted blue; /* Border kanan dengan gaya dotted */
   }
   ```

   **Properti Shorthand:**
   ```css
   div {
     border: 2px dashed green; /* Ketebalan, gaya, dan warna */
   }
   ```

3. **Padding**
   - **Definisi**: Padding adalah ruang di dalam elemen antara konten dan border. Padding menambah ruang di dalam elemen tetapi tidak menambah ukuran elemen di luar.
   - **Fungsi**: Mengatur ruang antara konten dan border. Padding berguna untuk memberikan ruang agar konten tidak menempel langsung pada batas border.
   - **Implementasi**: Seperti margin, padding dapat diatur untuk semua sisi atau secara individual untuk sisi atas, kanan, bawah, dan kiri.

   **Contoh CSS:**
   ```css
   div {
     padding: 10px; /* Padding semua sisi sebesar 10px */
   }

   p {
     padding-top: 5px;      /* Padding sisi atas */
     padding-right: 10px;   /* Padding sisi kanan */
     padding-bottom: 15px;  /* Padding sisi bawah */
     padding-left: 20px;    /* Padding sisi kiri */
   }
   ```

   **Properti Shorthand:**
   ```css
   div {
     padding: 10px 20px 15px 5px; /* Atas, kanan, bawah, kiri */
   }
   ```

***Diagram Hubungan Margin, Border, dan Padding***

```
+----------------------------+    <-- Margin (ruang di luar elemen)
|        margin              |
+----------------------------+    <-- Border (garis elemen)
|         border             |
+----------------------------+    <-- Padding (ruang dalam elemen)
|         padding            |
|   +--------------------+   |   <-- Konten (teks, gambar, dsb.)
|   |      Content       |   |
|   +--------------------+   |
+----------------------------+
```

Perbedaan Utama:
- **Margin** mengontrol ruang di luar elemen (antara elemen dengan elemen lain).
- **Border** adalah garis yang mengelilingi elemen dan berada di antara padding dan margin.
- **Padding** mengontrol ruang di dalam elemen, antara konten dan border.

***Contoh Implementasi Semua Properti:***

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Margin, Border, and Padding Example</title>
  <style>
    .box {
      margin: 20px;         /* Margin di luar elemen */
      border: 2px solid black; /* Border hitam dengan ketebalan 2px */
      padding: 15px;        /* Padding di dalam elemen */
      background-color: lightblue; /* Warna latar belakang elemen */
    }
  </style>
</head>
<body>

  <div class="box">
    Ini adalah contoh elemen dengan margin, border, dan padding.
  </div>

</body>
</html>
```

Pada contoh di atas:
- **Margin** menambah ruang di luar elemen `.box` dari elemen lain.
- **Border** memberikan garis di sekitar elemen.
- **Padding** menambah ruang antara teks konten dan border.

***Kesimpulan:***
- **Margin** digunakan untuk menambah jarak antara elemen dan sekelilingnya.
- **Border** digunakan untuk menambah batas atau garis di sekitar elemen.
- **Padding** digunakan untuk menambah ruang antara konten elemen dan border.
 
Dengan menggabungkan ketiganya, kita bisa mengontrol penempatan dan ruang dari elemen-elemen dalam tata letak halaman web.

<hr>

### Jelaskan konsep flex box dan grid layout beserta kegunaannya!

**Flexbox** dan **Grid Layout** adalah dua sistem tata letak yang sangat kuat dalam CSS yang digunakan untuk mengatur elemen-elemen dalam sebuah halaman web. Keduanya memiliki tujuan yang serupa, yaitu mempermudah pengaturan tata letak, tetapi mereka digunakan untuk kasus-kasus yang berbeda dan menawarkan pendekatan yang berbeda pula dalam tata letak halaman.

**1. Flexbox (Flexible Box Layout)**

**Konsep Flexbox**
Flexbox adalah sistem tata letak satu dimensi yang dirancang untuk mengatur elemen-elemen dalam satu arah, baik secara **horizontal** (baris) atau **vertikal** (kolom). Flexbox sangat berguna untuk mengatur tata letak elemen yang berubah-ubah ukurannya, baik itu elemen yang bersifat responsif maupun elemen dengan konten dinamis.

Flexbox terdiri dari dua komponen utama:
- **Flex container**: Elemen pembungkus yang memiliki properti `display: flex;`. Flex container akan menentukan bagaimana elemen-elemen di dalamnya diatur.
- **Flex items**: Elemen-elemen anak di dalam flex container yang akan diatur berdasarkan aturan flexbox.

Kegunaan Flexbox:
- Mengatur elemen dalam satu dimensi (baris atau kolom).
- Membuat elemen responsif secara otomatis sesuai dengan ukuran kontainer tanpa menggunakan banyak media query.
- Mengatur posisi elemen dengan mudah menggunakan properti seperti `justify-content` dan `align-items`.
- Mengatur perataan dan distribusi ruang antara elemen secara fleksibel.

Properti Utama Flexbox:
- **display: flex;** – Mengubah elemen menjadi flex container.
- **flex-direction** – Menentukan arah aliran elemen (row, row-reverse, column, column-reverse).
- **justify-content** – Mengatur posisi elemen di sepanjang sumbu utama (horizontal jika flex-direction adalah row).
- **align-items** – Mengatur perataan elemen di sepanjang sumbu silang (vertikal jika flex-direction adalah row).
- **flex-wrap** – Menentukan apakah elemen akan membungkus atau tetap dalam satu baris.
- **align-self** – Mengatur perataan elemen individual di sepanjang sumbu silang.

**2. Grid Layout**

**Konsep Grid Layout**
CSS Grid Layout adalah sistem tata letak dua dimensi yang memungkinkan pengaturan elemen secara **horizontal** dan **vertikal**. Grid memberikan kontrol yang lebih baik untuk membuat tata letak kompleks yang melibatkan baris dan kolom, menjadikannya alat yang sangat kuat untuk membuat grid pada halaman web.

Dengan Grid Layout, kita dapat menentukan jumlah baris dan kolom yang spesifik serta mendefinisikan ukuran masing-masing elemen dalam grid. Elemen dalam grid dapat ditempatkan di baris dan kolom tertentu, atau bisa membentang beberapa baris atau kolom.

Kegunaan Grid Layout:
- Mengatur elemen dalam dua dimensi (baris dan kolom).
- Membuat tata letak yang kompleks, seperti tata letak halaman yang terdiri dari header, sidebar, konten utama, dan footer.
- Mengontrol ukuran baris dan kolom secara eksplisit atau otomatis.
- Mengatur elemen agar menempati beberapa baris atau kolom sekaligus (spanning).
- Sangat fleksibel untuk tata letak yang memerlukan struktur grid yang jelas, seperti galeri gambar, dashboard, atau halaman yang memerlukan tata letak terstruktur.

Properti Utama Grid Layout:
- **display: grid;** – Mengubah elemen menjadi grid container.
- **grid-template-columns** – Menentukan jumlah dan ukuran kolom dalam grid.
- **grid-template-rows** – Menentukan jumlah dan ukuran baris dalam grid.
- **grid-column** – Menentukan tempat elemen di grid berdasarkan kolom.
- **grid-row** – Menentukan tempat elemen di grid berdasarkan baris.
- **gap** – Mengatur jarak antar elemen grid.


Perbedaan Antara Flexbox dan Grid Layout

| **Flexbox**                     | **Grid Layout**                   |
|----------------------------------|-----------------------------------|
| Sistem tata letak **satu dimensi** (horizontal atau vertikal) | Sistem tata letak **dua dimensi** (horizontal dan vertikal) |
| Cocok untuk tata letak yang fleksibel dan responsif dalam satu arah (misalnya baris produk) | Cocok untuk tata letak yang kompleks dengan banyak elemen dan struktur grid jelas |
| Elemen diatur berdasarkan urutan dalam HTML | Elemen bisa diatur di baris atau kolom mana saja tanpa memperhatikan urutan HTML |
| Sangat mudah untuk tata letak sederhana seperti menu navigasi atau galeri foto | Lebih cocok untuk struktur halaman penuh seperti dashboard atau layout yang memerlukan header, sidebar, konten, dan footer |
| Tidak ada kontrol eksplisit atas baris | Mengizinkan kontrol eksplisit pada baris dan kolom |

**Kapan Menggunakan Flexbox atau Grid?**
- Gunakan **Flexbox** jika tata letak Anda membutuhkan fleksibilitas dalam satu dimensi, misalnya ketika Anda ingin mengatur elemen secara dinamis berdasarkan ruang yang tersedia (misalnya, menu, galeri produk).
- Gunakan **Grid Layout** jika Anda memerlukan tata letak yang lebih kompleks dengan elemen yang ditempatkan di beberapa baris dan kolom, seperti layout halaman dengan bagian header, konten, sidebar, dan footer yang jelas.

***Kesimpulan***
Flexbox dan Grid Layout menawarkan pendekatan yang berbeda untuk menyusun tata letak halaman web. Flexbox sangat cocok untuk tata letak sederhana yang fleksibel dalam satu arah, sedangkan Grid Layout memberikan kontrol penuh untuk mengatur elemen secara dua dimensi. Penggunaan keduanya tergantung pada kompleksitas dan kebutuhan tata letak halaman yang sedang dikembangkan.

<br>
<br>
<hr>

</details>



<details>
  <summary><strong>Tugas 4</strong></summary>

## Langkah-langkah Pengimplementasian
### 1. Mengimplementasikan fungsi registrasi, login, dan logout

Buka `views.py` yang ada pada subdirektori `main` pada proyek, lalu tambahkan import `UserCreationForm`, `messages`, `authenticate`, `login`, `AuthenticationForm`, `logout`, dan `login_required` pada bagian paling atas.

```python
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
```

Tambahkan fungsi `register` ke dalam `views.py`. Fungsi ini berfungsi untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form.

```python
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
```

Buatlah berkas HTML baru dengan nama `register.html` pada direktori `main/templates` dan isi dengan template berikut

```python
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

Tambahkan fungsi `login_user` ke dalam `views.py`. Fungsi ini berfungsi untuk mengautentikasi pengguna yang ingin login.

```python
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

Buatlah berkas HTML baru dengan nama login.html pada direktori main/templates dan isi dengan template berikut.

```python
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

Tambahkan fungsi `logout_user` ke dalam `views.py`. Fungsi ini berfungsi untuk melakukan mekanisme logout.

```python
def logout_user(request):
    logout(request)
    return redirect('main:login')
```

Bukalah berkas `main.html` yang ada pada direktori `main/templates `dan tambahkan potongan kode di bawah ini setelah hyperlink tag untuk Add New Product Form.

```pyhton
...
<a href="{% url 'main:logout' %}">
  <button>Logout</button>
</a>
...
```

Buka `urls.py` yang ada pada subdirektori `main`, impor fungsi dan tambahkan path url ke dalam `urlpatterns` untuk mengakses funsi yang sudah diimpor 

```python
from main.views import register, login_user, logout_user

 urlpatterns = [
     ...
     path('register/', register, name='register'),
     path('login/', login_user, name='login'),
     path('logout/', logout_user, name='logout'),
 ]
```

Tambahkan potongan kode `@login_required(login_url='/login')` di atas fungsi `show_model` agar halaman main hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).

```python
...
@login_required(login_url='/login')
def show_main(request):
...
```

### 2. Menggunakan Data Dari Cookies

Buka kembali `views.py` yang ada pada subdirektori `main`. Tambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` pada bagian paling atas.

```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

Pada fungsi `login_user`, tambahkan fungsionalitas menambahkan cookie yang bernama `last_login` untuk melihat kapan terakhir kali pengguna melakukan login. Ganti kode yang ada pada blok `if form.is_valid()` menjadi potongan kode berikut.

```python
...
if form.is_valid():
    user = form.get_user()
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main"))
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
...
```

Pada fungsi `show_main`, tambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel context.

Lalu, ubah fungsi `logout_user` menjadi 

```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Buka berkas `main.html` dan tambahkan potongan kode berikut di atas atau dibawah tombol logout untuk menampilkan data last login.

```python
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

### 3. Menghubungan Model Product dengan User

Buka `models.py` yang ada pada subdirektori `main` dan tambahkan kode berikut pada dibawah baris kode untuk mengimpor model:

```python
from django.contrib.auth.models import User
```

Pada model `Product` yang sudah dibuat, tambahkan potongan kode berikut:

```python
class MoodEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```

Buka kembali `views.py` yang ada pada subdirektori `main`, dan ubah potongan kode pada fungsi `create_product_form` menjadi sebagai berikut:

```python
def create_product_form(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_model')

    context = {'form': form}
    return render(request, 'create_product_form.html', context)
```

Ubah value dari `model` dan `context` pada fungsi `show_model` menjadi seperti berikut.

```python
def show_model(request):
    model = Product.objects.filter(user=request.user)

    context = {
         'user': request.user.username,
         ...
    }
...
```

Simpan semua perubahan, dan lakukan migrasi model dengan `python manage.py makemigrations`.

Seharusnya, akan muncul error saat melakukan migrasi model. Pilih 1 untuk menetapkan default value untuk field user pada semua row yang telah dibuat pada database. Lalu, ketik angka 1 lagi untuk menetapkan user dengan ID 1 (yang sudah kita buat sebelumnya) pada model yang sudah ada.

Lakukan `python manage.py migrate` untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya.

Langkah terakhir, kita harus mempersiapkan aplikasi web kita untuk environtment production. Untuk itu, tambahkan sebuah import baru pada `settings.py` yang ada pada subdirektori `zoldyck`

```python
import os
```

Kemudian, ganti variabel `DEBUG` dari berkas `settings.py` menjadi seperti ini.

```python
PRODUCTION = os.getenv("PRODUCTION", False)
DEBUG = not PRODUCTION
```

<br>
<br>
<hr>

# PERTANYAAN

### Apa perbedaan antara HttpResponseRedirect() dan redirect()

`HttpResponseRedirect()` adalah kelas bawaan Django yang digunakan untuk mengarahkan (redirect) pengguna dari satu URL ke URL lain. Fungsinya adalah untuk mengembalikan response HTTP 302, yang memberitahu browser untuk menuju URL yang baru. Saat kamu menggunakan `HttpResponseRedirect()`, kamu perlu memberikan URL yang spesifik, contohnya:

```python
from django.http import HttpResponseRedirect
return HttpResponseRedirect('/some-url/')
```

`redirect()` adalah fungsi shortcut (fungsi yang sudah disederhanakan) di Django yang lebih fleksibel daripada `HttpResponseRedirect()`. Kamu bisa menggunakan `redirect()` dengan berbagai parameter seperti URL, nama view, atau bahkan objek model yang mendefinisikan URL secara dinamis.

#### Penggunaan `HttpResponseRedirect()` dalam proyek zoldyck 

Di dalam fungsi `login_user`, setelah pengguna berhasil login, sistem menggunakan `HttpResponseRedirect()` untuk mengarahkan pengguna ke halaman utama (`show_model`). Selain itu, cookie `last_login` diset untuk menyimpan waktu login terakhir pengguna.

Fungsi `logout_user` juga menggunakan `HttpResponseRedirect()` untuk mengarahkan pengguna kembali ke halaman login setelah logout, dan pada saat yang sama, cookie `last_login` dihapus.

```python
response = HttpResponseRedirect(reverse("main:show_model"))
response.set_cookie('last_login', str(datetime.datetime.now()))
```

#### Penggunaan `redirect()` dalam proyek zoldyck 

Dalam fungsi `create_product_form`, setelah form valid dan produk baru disimpan, sistem menggunakan `redirect()` untuk mengarahkan pengguna kembali ke halaman yang menampilkan produk (`show_model`).

```python
return redirect('main:show_model')
```

Dalam fungsi `register`, setelah pengguna berhasil mendaftar, sistem mengarahkan pengguna ke halaman login menggunakan `redirect()`.

```python
return redirect('main:login')
```

```bash
Kapan Menggunakan HttpResponseRedirect() dan redirect()?
`HttpResponseRedirect()` lebih cocok digunakan jika kita ingin mengatur lebih banyak hal di dalam response, seperti menambahkan cookies, mengatur headers, atau response lain yang memerlukan modifikasi lebih lanjut.

`redirect()` adalah cara yang lebih ringkas dan sederhana untuk mengarahkan pengguna ke URL, baik itu URL yang disediakan langsung, nama view, atau object model yang berkaitan.
```

<hr>

### Jelaskan cara kerja penghubungan model Product dengan User!

Di Django, untuk menghubungkan model `Product` dengan model `User`, kita biasanya menggunakan relasi **ForeignKey**. Relasi ini memungkinkan satu produk terkait dengan satu pengguna. Dengan kata lain, setiap produk dihubungkan dengan pengguna tertentu yang memilikinya atau membuatnya. Berikut adalah langkah-langkah bagaimana model `Product` bisa dihubungkan dengan model `User`:

**Mengimpor model** `User` Django sudah menyediakan model `User` secara bawaan melalui `django.contrib.auth.models.User`.

**Menambahkan ForeignKey pada Model** `Product` Pada model `Product`, kita tambahkan field `user` yang dihubungkan dengan model `User` menggunakan `ForeignKey`. Contohnya:

```python
from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

`ForeignKey(User, on_delete=models.CASCADE)`: Ini mendefinisikan bahwa setiap produk terkait dengan satu pengguna (`User`). Jika pengguna dihapus, maka semua produk yang terkait juga akan dihapus (`on_delete=models.CASCADE`).

**Menampilkan Produk Berdasarkan Pengguna** Pada view, kamu bisa menggunakan request.user untuk menampilkan produk yang hanya terkait dengan pengguna yang sedang login.

<hr>

### Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.

**Authentication (Otentikasi)** adalah proses memverifikasi identitas seseorang. Ketika pengguna login, mereka memasukkan kredensial seperti username dan password, yang kemudian diperiksa apakah cocok dengan yang ada di database. Jika cocok, pengguna dianggap "authenticated" atau telah diotentikasi. Contoh otentikasi adalah login dengan username dan password.

**Authorization (Otorisasi)** adalah proses menentukan apa yang diizinkan atau tidak diizinkan untuk dilakukan oleh pengguna setelah mereka diotentikasi. Authorization mengatur hak akses pengguna, seperti siapa yang boleh mengakses halaman tertentu atau melakukan tindakan spesifik.

**Saat pengguna login:**
`Authentication` terjadi ketika pengguna memasukkan kredensial mereka (username dan password) dan sistem memeriksa apakah kredensial tersebut valid.
`Authorization` menentukan apa yang bisa dilakukan oleh pengguna setelah mereka login. Misalnya, pengguna biasa mungkin hanya bisa melihat profil mereka, sementara admin bisa mengakses data lain yang lebih sensitif.

**Django mengimplementasikan kedua konsep ini sebagai berikut:**

**Authentication**: Django menggunakan mekanisme otentikasi bawaan dengan model User dan sistem autentikasi yang mendukung login, logout, dan pendaftaran pengguna. Django memiliki fungsi seperti `authenticate()` dan `login()` untuk otentikasi pengguna.

**Authorization**: Setelah pengguna diotentikasi, Django menggunakan decorators seperti `@login_required` untuk membatasi akses ke halaman tertentu, dan peran (groups atau permissions) untuk mengatur hak akses pengguna

<hr>
 
### Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?

Django mengingat pengguna yang telah login dengan menggunakan **session framework**. Setiap kali pengguna berhasil login, Django menyimpan informasi tentang pengguna dalam **session**. Django secara otomatis membuat **session ID** untuk pengguna yang sedang login, dan session ID ini disimpan dalam browser pengguna sebagai **cookie**. Ketika pengguna melakukan request di masa mendatang, browser mengirimkan cookie ini kembali ke server, dan Django dapat mengidentifikasi pengguna berdasarkan session ID tersebut.

**Cookies dan session dalam Django:**
• Saat pengguna login, Django membuat session ID dan menyimpannya di cookies browser.
• Server menyimpan informasi terkait session ID tersebut, seperti data pengguna yang terkait dengan session itu.
• Ketika pengguna mengunjungi kembali situs tersebut, cookies akan dikirim bersama dengan request HTTP, dan Django dapat mengetahui pengguna mana yang sedang melakukan request.

**Contoh penggunaan session di Django pada proyek zoldyck:**
```python

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user) <-------------------------- create session
        response = HttpResponseRedirect(reverse("main:show_model"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```

**Kegunaan lain dari cookies:**
`Menyimpan preferensi pengguna`: Misalnya, bahasa atau tema yang dipilih pengguna bisa disimpan dalam cookies.
`Pelacakan`: Cookies sering digunakan oleh situs untuk melacak perilaku pengguna di situs tersebut.
`Authentication token`: Untuk menjaga agar pengguna tetap login tanpa harus memasukkan kredensial setiap kali, cookies bisa digunakan untuk menyimpan token autentikasi.

**Apakah Semua Cookies Aman Digunakan?**
Tidak semua cookies aman. Beberapa masalah keamanan terkait cookies meliputi:
`Cookies yang tidak dienkripsi`: Jika cookies tidak dienkripsi, informasi sensitif seperti session ID bisa dicegat melalui serangan man-in-the-middle.
`Cookies yang disalahgunakan`: Cookies bisa digunakan untuk melacak aktivitas pengguna tanpa persetujuan mereka, yang melanggar privasi.
`Cross-site scripting (XSS)`: Jika sebuah situs rentan terhadap XSS, penyerang bisa mencuri cookies pengguna dan menyalahgunakannya untuk login ke akun mereka.

Untuk mengatasi masalah keamanan ini, Django menyediakan beberapa perlindungan:
`HttpOnly flag`: Mencegah JavaScript mengakses cookies, yang dapat membantu mengurangi risiko XSS.
`Secure flag`: Hanya mengirim cookies melalui koneksi HTTPS.
`CSRF Protection`: Melindungi dari serangan Cross-Site Request Forgery (CSRF) dengan token khusus pada form.

<br>
<br>
<hr>

</details>



<details>
  <summary><strong>Tugas 3</strong></summary>

## Langkah-langkah Pengimplementasian
### 1. Persiapan dan langkah awal sebelum mengerjakan Tugas 3

Langkah pertama adalah membuat file `base.html` dalam direktori `templates`. Untuk memulai, jalankan perintah berikut di terminal atau command prompt:

```bash
touch base.html
vi base.html
```

Perintah ini akan membuat dan membuka file `base.html`, lalu kita dapat mengisi file `base.html` dengan kode berikut

```python
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

### Mengapa Kita Memerlukan Data Delivery dalam Pengimplementasian Sebuah Platform?

Data delivery adalah proses pengiriman data dari satu bagian sistem ke bagian lain atau dari server ke klien. Dalam pengimplementasian sebuah platform, terutama platform berbasis web atau aplikasi mobile, data delivery sangat penting karena:

- **Integrasi Sistem:** Data delivery memastikan bahwa berbagai komponen dari sistem yang berbeda (misalnya, backend dan frontend) dapat berkomunikasi dan berbagi data secara efisien.
- **Pengalaman Pengguna:** Pengiriman data yang cepat dan akurat meningkatkan pengalaman pengguna. Misalnya, aplikasi web yang responsif harus dapat mengirimkan dan menerima data dengan cepat untuk memastikan interaksi yang lancar.
- **Konsistensi Data:** Data delivery yang baik membantu menjaga konsistensi data di seluruh aplikasi, menghindari inkonsistensi dan konflik yang mungkin muncul ketika data diperbarui di berbagai tempat.
- **Keamanan:** Data delivery juga mencakup aspek keamanan, seperti enkripsi data saat transit, untuk melindungi informasi sensitif dari akses yang tidak sah.

<hr>

### XML vs. JSON: Mana yang Lebih Baik?

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

<hr>

### Fungsi dari Method `is_valid()` pada Form Django

Method `is_valid()` dalam form Django digunakan untuk memvalidasi data yang dikirimkan melalui form. Berikut penjelasannya:

- **Validasi Data:** `is_valid()` memeriksa apakah data yang dikirimkan oleh pengguna memenuhi semua aturan validasi yang ditentukan dalam form. Ini termasuk memeriksa apakah semua field yang diperlukan diisi, apakah data sesuai dengan tipe yang diharapkan, dan apakah data mematuhi aturan validasi khusus (misalnya, format email yang benar).
- **Pengembalian Status:** Jika data valid, `is_valid()` mengembalikan `True`, dan data dapat diakses melalui `form.cleaned_data`. Jika tidak valid, mengembalikan `False`, dan Anda dapat mengakses pesan kesalahan melalui `form.errors`.

<hr>

### Pentingnya `csrf_token` pada Form Django

**CSRF (Cross-Site Request Forgery)** adalah jenis serangan di mana penyerang dapat melakukan aksi di atas nama pengguna yang sudah masuk tanpa sepengetahuan pengguna tersebut. CSRF token adalah mekanisme keamanan yang melindungi aplikasi web dari serangan ini dengan memastikan bahwa setiap permintaan yang dilakukan kepada server berasal dari sumber yang sah.

- **Fungsi `csrf_token`:** `csrf_token` adalah token unik yang dihasilkan untuk setiap sesi pengguna. Saat form disubmit, token ini harus dikirim bersama permintaan. Server memeriksa token tersebut untuk memastikan bahwa permintaan berasal dari aplikasi web yang sah dan bukan dari sumber eksternal.
- **Risiko Tanpa `csrf_token`:** Jika `csrf_token` tidak disertakan, penyerang dapat membuat form yang tampaknya sah dan mengirimkan permintaan berbahaya yang dilakukan atas nama pengguna yang sah. Ini dapat mengakibatkan perubahan data, penghapusan data, atau tindakan lainnya yang tidak diinginkan.

**Cara Penyerang Memanfaatkan Ketidakhadiran `csrf_token`:**
- **Meniru Formulir:** Penyerang dapat membuat halaman web palsu yang meniru form asli dan mengirimkan permintaan ke server dengan menggunakan cookies dari pengguna yang sah.
- **Eksploitasi:** Dengan mengeksploitasi ketidakhadiran `csrf_token`, penyerang dapat melakukan aksi tanpa izin, seperti mengubah pengaturan pengguna atau melakukan transaksi yang tidak sah.

Menambahkan `csrf_token` ke form Django membantu memastikan bahwa permintaan yang diterima server adalah permintaan yang sah dan mencegah berbagai jenis serangan CSRF.

<hr>

### Mengakses keempat URL dalam format XML, JSON, XML by ID, dan JSON by ID menggunakan Postman

#### URL dalam format XML
<img width="1440" alt="Screenshot 2024-09-18 at 10 56 27" src="https://github.com/user-attachments/assets/10b8a7ef-aebd-471e-9f5c-5fd9c5c79c17">

#### URL dalam format JSON
<img width="1440" alt="Screenshot 2024-09-18 at 10 56 37" src="https://github.com/user-attachments/assets/aacd6f5d-69d5-4e94-8bd9-264adb34f0b6">

#### URL dalam format XML by ID
<img width="1440" alt="Screenshot 2024-09-18 at 11 00 27" src="https://github.com/user-attachments/assets/f446b548-f4ed-43ff-84ce-4e393d228b88">


#### URL dalam format JSON by ID
<img width="1440" alt="Screenshot 2024-09-18 at 11 00 18" src="https://github.com/user-attachments/assets/b3628fb5-4e42-4518-a2e9-9b6876c652e8">


<br>
<br>
<hr>

</details>



<details>
  <summary><strong>Tugas 2</strong></summary>

## Langkah-langkah Pengimplementasian
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

<hr>

### Fungsi Git

Git berfungsi sebagai sistem kontrol versi yang sangat penting dalam pengembangan perangkat lunak. Dengan Git, pengembang dapat melacak setiap perubahan yang dilakukan pada kode sumber secara terperinci. Hal ini memungkinkan mereka untuk melihat riwayat lengkap perubahan, termasuk siapa yang membuat perubahan, kapan perubahan tersebut dibuat, dan alasan di balik perubahan itu. Git mendukung kerja tim dengan menyediakan fitur cabang (branch) yang memungkinkan pengembang untuk mengerjakan fitur baru atau perbaikan bug secara terpisah dari kode utama (master branch). Cabang-cabang ini dapat digabungkan (merged) kembali ke kode utama dengan aman setelah fitur atau perbaikan selesai dan diuji. Selain itu, Git memudahkan proses rollback, yaitu mengembalikan kode ke versi sebelumnya jika terjadi kesalahan atau masalah, yang membantu meminimalkan risiko dan kerusakan pada proyek. Dengan fitur seperti konflik penyatuan (merge conflicts) yang terkelola dengan baik dan kemampuan untuk membandingkan versi kode, Git membantu menjaga integritas kode dan memastikan kolaborasi yang efisien di antara tim pengembang dalam proyek yang kompleks dan dinamis.

<hr>

### Mengapa Django Dijadikan Permulaan Pembelajaran Pengembangan Perangkat Lunak?

Django sering dipilih sebagai framework pengenalan dalam pembelajaran pengembangan perangkat lunak karena beberapa alasan utama. Pertama, Django dirancang untuk mendukung pengembangan cepat (rapid development) dengan mengutamakan efisiensi dan produktivitas. Framework ini mengikuti arsitektur Model-View-Template (MVT), yang memisahkan tanggung jawab dalam pengembangan aplikasi web sehingga pemula dapat lebih mudah memahami konsep dasar seperti routing, templating, dan manajemen basis data tanpa terjebak dalam kode yang berlebihan. Django juga menyediakan berbagai fitur bawaan yang mempermudah pengelolaan aplikasi, seperti sistem autentikasi pengguna, antarmuka admin yang otomatis, dan sistem migrasi basis data. Dokumentasi Django yang lengkap dan komunitas yang aktif menyediakan banyak sumber daya belajar, tutorial, dan forum dukungan, membuatnya lebih mudah bagi pemula untuk mendapatkan bantuan dan memahami framework ini. Selain itu, Django mengutamakan keamanan dengan fitur-fitur seperti perlindungan terhadap serangan Cross-Site Request Forgery (CSRF) dan SQL Injection, yang mengajarkan praktik keamanan yang penting dalam pengembangan web.

<hr>

### Mengapa Model pada Django Disebut ORM (Object-Relational Mapping)?

Model dalam Django disebut sebagai ORM (Object-Relational Mapping) karena ia menyediakan cara untuk memetakan objek Python ke dalam struktur tabel basis data relasional secara langsung. ORM memungkinkan pengembang untuk bekerja dengan database menggunakan objek Python, tanpa harus menulis kueri SQL yang kompleks dan rawan kesalahan secara langsung. Dengan ORM, setiap model Django diwakili sebagai kelas Python, dan atribut dari kelas tersebut otomatis dipetakan ke kolom dalam tabel basis data. Fitur ini mengabstraksi detail teknis dari interaksi dengan basis data, membuat pengelolaan data menjadi lebih sederhana dan kode lebih mudah dipahami dan dirawat. ORM juga menyediakan fitur untuk migrasi basis data, yang memungkinkan perubahan pada model kode untuk diterapkan ke struktur basis data dengan mudah. Dengan cara ini, ORM memastikan konsistensi antara model kode dan tabel basis data, serta mengurangi potensi kesalahan dalam pengelolaan data. Secara keseluruhan, ORM mempermudah pengembang untuk bekerja dengan data dalam format yang lebih intuitif dan terintegrasi dengan bahasa pemrograman Python.


<br>
<br>
<hr>

</details>
