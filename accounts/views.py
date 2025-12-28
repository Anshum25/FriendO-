from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import redirect, render

from .models import Profile


def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        identifier = request.POST.get("identifier") or request.POST.get("username")
        password = request.POST.get("password")

        username = identifier
        UserModel = get_user_model()
        if identifier and "@" in identifier:
            user_obj = UserModel.objects.filter(email__iexact=identifier).first()
            if user_obj:
                username = user_obj.get_username()

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")

        messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def signup_view(request):
    if request.method == "POST":
        username = (request.POST.get("username") or "").strip()
        email = (request.POST.get("email") or "").strip()
        password = request.POST.get("password") or ""
        confirm_password = request.POST.get("confirmPassword") or ""

        if not username or not email or not password:
            messages.error(request, "All fields are required")
            return render(request, "signup.html")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, "signup.html")

        UserModel = get_user_model()

        if UserModel.objects.filter(username__iexact=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "signup.html")

        if UserModel.objects.filter(email__iexact=email).exists():
            messages.error(request, "Email already exists")
            return render(request, "signup.html")

        user = UserModel.objects.create_user(username=username, email=email, password=password)
        Profile.objects.get_or_create(user=user)

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "signup.html")


def logout_view(request):
    logout(request)
    return redirect("index")


def main(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    return render(request, "main.html", {"profile": profile})


def profile(request):
    return render(request, "profile.html")


def profile_setup(request):
    return render(request, "profile_setup.html")


def search_results(request):
    return render(request, "search_results.html")


def user_profile(request, username):
    UserModel = get_user_model()
    user_obj = UserModel.objects.filter(username=username).first()
    if not user_obj:
        return render(request, "404.html", status=404)
    profile, _ = Profile.objects.get_or_create(user=user_obj)
    return render(request, "profile.html", {"profile": profile, "viewed_user": user_obj})


def search_user(request):
    query = request.GET.get("q", "").strip()
    UserModel = get_user_model()
    results = []
    if query:
        results = UserModel.objects.filter(username__icontains=query)[:20]
    return render(request, "search_results.html", {"query": query, "results": results})
