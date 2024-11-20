from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
import json

from django.contrib.auth import logout as auth_logout

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                "message": "Login sukses!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, akun dinonaktifkan."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali email atau kata sandi."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '').strip()
            password1 = data.get('password1', '')
            password2 = data.get('password2', '')

            # Validation
            if not username or not password1 or not password2:
                return JsonResponse({
                    "status": "failed",
                    "message": "All fields are required."
                }, status=400)

            if password1 != password2:
                return JsonResponse({
                    "status": "failed",
                    "message": "Passwords do not match."
                }, status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({
                    "status": "failed",
                    "message": "Username already exists."
                }, status=400)

            # Create the new user
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password1
                )
                user.save()
                
                return JsonResponse({
                    "status": "success",
                    "message": "User created successfully!"
                }, status=201)
            except Exception as e:
                return JsonResponse({
                    "status": "failed",
                    "message": f"Error creating user: {str(e)}"
                }, status=400)

        except json.JSONDecodeError:
            return JsonResponse({
                "status": "failed",
                "message": "Invalid JSON data"
            }, status=400)

    return JsonResponse({
        "status": "failed",
        "message": "Invalid request method."
    }, status=405)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)