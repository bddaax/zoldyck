from django.test import TestCase, Client
from django.utils import timezone
from .models import Product  

class mainTest(TestCase):
    
    # Test apakah URL utama dapat diakses
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    # Test apakah template yang digunakan sesuai
    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    # Test untuk halaman yang tidak ada
    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    # Test model Product untuk memastikan produk Zoldyck ditambahkan
    def test_create_product(self):
        product = Product.objects.create(
            name="Zeno Zoldyck",
            price=12000000,
            description="Detektif untuk investigasi mendalam.",
            service="Dragon's Insight - Investigasi Mendalam",
            experience="Zeno telah memecahkan lebih dari 50 kasus besar...",
            rating=4.9,
            category="Investigasi Mendalam",
            stock=2,
            additional_experience="Sering dipanggil untuk menangani kasus organisasi kriminal internasional.",
        )
        self.assertEqual(product.name, "Zeno Zoldyck")
        self.assertEqual(product.price, 12000000)
        self.assertEqual(product.rating, 4.9)
