from django.shortcuts import render, redirect
from .forms import QRCodeForm
import qrcode
import os, base64
from django.conf import settings
from io import BytesIO

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'index.html')

def qr_generator(request):
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        
        if form.is_valid():
            company_name = form.cleaned_data['Company_name']
            url = form.cleaned_data['url']
            # Generate QR Code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            
            img = qr.make_image(fill='black', back_color='white')
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            img_str = base64.b64encode(buffer.getvalue()).decode()
            file_name = company_name.replace(" ", "_").lower()+".png"
            # img = qrcode.make(url)
            #file_name = company_name.replace(" ", "_").lower()+".png"
            # file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            # img.save(file_path)


            # #Create URL for the QR Code
            # qr_url = os.path.join(settings.MEDIA_URL, file_name)
            context = {
                'company_name': company_name,
                'qr_code': img_str,
                'file_name': file_name,

            }
            
            return render(request, 'qr_code_display.html', context)
    else:
        form = QRCodeForm()
        context = {
            'form': form,

        }
        return render(request, 'qr_generator.html', context)
    


def signup(request):
    if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     confirmpassword = request.POST['confirmpassword']
    #     email = request.POST['email']
    #     if User.objects.filter(email=email).exists():
    #         return render(request, 'signup.html')
    #     if password != confirmpassword:
    #         return render(request, 'signup.html')
    #     User.objects.create_user(username, email, password)
    #     return redirect('signin')
        return redirect('qr_generator')

    return render(request, 'signup.html')
    

def signin(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # user = authenticate(username=username, password=password)
        # if user is not None:
        #     login(request, user)
        #     return redirect('qr_generator')
        # else:
        #     return render(request, 'signin.html')
        return redirect('qr_generator')
    return render(request, 'signin.html')

def signout(request):
    logout(request)
    return redirect('home')


