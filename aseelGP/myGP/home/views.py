from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, UserAddForm, FileForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, UploadedFile, PendAccess, UserInfo
from .forms import PostForm
from django.db.models import Q
import requests
import magic
from django.conf import settings
from django.http import FileResponse
import os
from django.http import JsonResponse



def home(request,**kwargs):

    return render(request, 'user-temp/home.html', {'register': kwargs.get('register', "empty")})


def signup(request):
    register = 'false'
    if request.method == "POST":
        user_form = UserForm(data=request.POST)

        add_user = UserAddForm(data=request.POST)

        if user_form.is_valid() and add_user.is_valid():

            user = user_form.save(commit=False)

            user.set_password(user.password)

            """email_list = User.objects.filter(email=user.email).values_list('email')
            print(email_list)
            if len(email_list) !=0:
                return HttpResponse('the email is allredy exist')"""

            user.username = user.email

            user.save()

            add = add_user.save(commit=False)

            add.user = user

            add.save()

            register = 'true'

            #return render(request, 'user-temp/home.html', {'register': register})
            #return HttpResponseRedirect(reverse('home'))
            return redirect('success')

        else:
            print(user_form.errors, add_user.errors)
            return render(request, 'user-temp/signup.html',
                          {'user_form': user_form, 'add_user': add_user, 'register': register})

    else:

        user_form = UserForm()
        add_user = UserAddForm()
    return render(request, 'user-temp/signup.html', {'user_form': user_form, 'add_user': add_user, 'register': 'register'})


def success_view(request):
    return render(request, 'user-temp/success_page.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username_query = User.objects.filter(email=email).only('username')
        if len(username_query)>0:
            username = username_query[0]
        else:
            username = ''

        user = authenticate(username=username, password=password)
        if user:

            if user.is_active:
                userinf = user.userinfo
                userinf.failed_login_num = 0
                userinf.save()
                login(request, user)
                #return HttpResponseRedirect(reverse('user_page'))
                #return HttpResponse('login sucssesfuly done ')
                return redirect('profile')

            else:
                return HttpResponse('account not active')
        else:
            print('someone failed login')
            print('username: {} and password:{}'.format(email, password))
            try:
                go1 = User.objects.get(username=username)
                go = go1.userinfo
            except:
                go = None

            if go != None:
                go.failed_login_num += 1
                go.save()
                if go.failed_login_num > 5:
                    go1.is_active = 0
                    go1.save()

            return HttpResponse('<h1>invalid login  (please note that when you reach 5 invalid logins your account will be deactivated)<h1>')
    else:
        #return render(request, 'app1_emp/login.html', {})
        return redirect('home')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))



@login_required
def profile(request):
    userPosts = Post.objects.filter(owner=request.user)
    return render(request, 'user-temp/profile.html', context={'userPosts': userPosts, 'useremail': request.user.email,'userinfo':request.user.userinfo})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            post_instance = form.save(commit=False)
            if post_instance.category_enum == 1 or request.user.userinfo.is_supervisor:
                post_instance.show = True
                post_instance.approved = True
            post_instance.owner = request.user
            post_instance.save()

            return redirect('profile')

    else:
        form = PostForm()

    return render(request, 'user-temp/create_post.html', {'form': form, 'userinfo': request.user.userinfo})

@login_required
def puplic_post(request):
    posts = Post.objects.filter(Q(show=True) & Q(approved=True)).order_by('-created_datetime')
    is_super = False
    if request.user.userinfo.is_supervisor:
        is_super = True
    return render(request, 'user-temp/puplic_post.html', {'posts': posts, 'is_super': is_super, 'userinfo': request.user.userinfo})


@login_required
def pendingpost(request):
    if request.user.userinfo.is_supervisor:
        posts = Post.objects.filter(Q(show=False) & Q(approved=False)).order_by('-created_datetime')
        return render(request, 'user-temp/pend_post.html', {'posts': posts, 'userinfo': request.user.userinfo})
    else:
        user0 = UserInfo.objects.get(id=request.user.id)
        user0.pendaccess += 1
        user0.save()
        return HttpResponse('<h1>you are not allowd here !!!!!!!!<h1> ')

@login_required
def showpost(request, i):
    if request.user.userinfo.is_supervisor:
        post = Post.objects.get(id=i)
        post.show = True
        post.approved = True
        post.save()
        return redirect('puplic_post')
    else:
        user0 = UserInfo.objects.get(id=request.user.id)
        user0.pendaccess += 1
        user0.save()
        return HttpResponse('<h1>you are not allowd here !!!!!!!!<h1> ')


def is_allowed_file(file):
    return file in ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                         'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                         'application/vnd.openxmlformats-officedocument.presentationml.presentation',
                         'application/vnd.ms-powerpoint']

@login_required
def create_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            # Check if the file size exceeds 32MB
            if file.size > 32 * 1024 * 1024:  # 32MB in bytes
                return render(request, 'user-temp/file_size_exceeded.html')

            # Check if the file is of an allowable type
            if not is_allowed_file(file.content_type):
                return render(request, 'user-temp/invalid_file_type.html')

            api_key = settings.VIRUSTOTAL_API_KEY
            url = 'https://www.virustotal.com/api/v3/files'
            headers = {
                'x-apikey': api_key,
            }
            # Send the PDF file to VirusTotal for scanning
            files = {'file': (file.name, file.read())}
            response = requests.post(url, files=files, headers=headers)
            result = response.json()
            id_url = result['data']['links']['self']
            report = requests.get(id_url, headers=headers).json()
            report_result = report['data']['attributes']['stats']
            engins = report['data']['attributes']['results']

            scan_result = result.get('data', {}).get('attributes', {}).get('last_analysis_stats', {}).get('malicious',
                                                                                                          'Unknown')

            if (report_result['malicious'] != 0) and (report_result['suspicious'] != 0):
                return render(request, 'user-temp/infected_file.html',{'report_result': report_result, 'engins':engins})

            uploaded_file = form.save(commit=False)
            uploaded_file.scan_result = report_result
            uploaded_file.owner = request.user
            if request.user.userinfo.is_supervisor:
                uploaded_file.show = True
                uploaded_file.approved = True
            uploaded_file.save()
            return render(request, 'user-temp/upload_success.html',{'report_result': report_result, 'engins':engins})

    else:
        form = FileForm()

    return render(request, 'user-temp/upload.html', {'form': form})


@login_required
def puplic_files(request):
    files = UploadedFile.objects.filter(Q(show=True) | Q(approved=True)).order_by('-created_datetime')
    is_super = False
    if request.user.userinfo.is_supervisor:
        is_super = True
    return render(request, 'user-temp/puplic_files.html', {'files': files, 'is_super': is_super, 'userinfo': request.user.userinfo})


@login_required
def my_files(request):
    files = UploadedFile.objects.filter(owner=request.user).order_by('-created_datetime')
    return render(request, 'user-temp/myfiles.html', {'files': files, 'userinfo': request.user.userinfo})


@login_required
def download_file(request, file_id):
    uploaded_file = UploadedFile.objects.get(pk=file_id)
    file_path = uploaded_file.file.path
    file_name = os.path.basename(file_path)

    response = FileResponse(open(file_path, 'rb'), content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file_name}"'

    return response


@login_required
def pendingfiles(request):
    if request.user.userinfo.is_supervisor:
        files = UploadedFile.objects.filter(Q(show=False) | Q(approved=False)).order_by('-created_datetime')
        return render(request, 'user-temp/pend_files.html', {'files': files, 'userinfo': request.user.userinfo})
    else:
        user0 = UserInfo.objects.get(id=request.user.id)
        user0.pendaccess += 1
        user0.save()
        return HttpResponse('<h1>you are not allowd here !!!!!!!!<h1> ')

@login_required
def showfile(request, i):
    if request.user.userinfo.is_supervisor:
        file = UploadedFile.objects.get(id=i)
        file.show = True
        file.approved = True
        file.save()
        return redirect('pendingfiles')
    else:
        user0 = UserInfo.objects.get(id=request.user.id)
        user0.pendaccess += 1
        user0.save()
        return HttpResponse('<h1>you are not allowd here !!!!!!!!<h1> ')


def hidefile(request, i):
    if request.user.userinfo.is_supervisor:
        file = UploadedFile.objects.get(id=i)
        file.show = False
        file.approved = False
        file.save()
        return redirect('puplic_files')

    else:
        file = UploadedFile.objects.get(id=i)
        if file.owner.id == request.user.id:
            file.show = False
            file.save()
            return redirect('profile')
        else:
            user0 = UserInfo.objects.get(id=request.user.id)
            user0.pendaccess += 1
            user0.save()
            return HttpResponse('<h1>you are not allowd to hide another one file !!!!!!!!<h1> ')



def hidepost(request, i):
    if request.user.userinfo.is_supervisor:
        post = Post.objects.get(id=i)
        post.show = False
        post.approved = False
        post.save()
        return redirect('profile')

    else:
        post = Post.objects.get(id=i)
        if post.owner.id == request.user.id:
            post.show = False
            post.save()
            return redirect('profile')
        else:
            user0 = UserInfo.objects.get(id=request.user.id)
            user0.pendaccess += 1
            user0.save()
            return HttpResponse('<h1>you are not allowd to hide another one post !!!!!!!!<h1> ')


def unusualactivity(request):
    if request.user.userinfo.is_supervisor:
        users = UserInfo.objects.filter(pendaccess__gt=0)
        return render(request, 'user-temp/unusualactivity.html', {'users': users, 'userinfo': request.user.userinfo})
    else:
        user0 = UserInfo.objects.get(id=request.user.id)
        user0.pendaccess += 1
        user0.save()
        return HttpResponse('<h1>you are not allowd here !!!!!!<h1> ')



def scan_link(request):
    if request.method == 'POST':
        api_key = settings.VIRUSTOTAL_API_KEY
        url_to_scan = request.POST.get('url', '')

        if not url_to_scan:
            return JsonResponse({'error': 'URL parameter is missing'}, status=400)

        api_url = 'https://www.virustotal.com/api/v3/urls'
        headers = {'x-apikey': api_key}
        data = {'url': url_to_scan}

        response = requests.post(api_url, headers=headers, data=data)

        if response.status_code == 200:
            result = response.json()
            id_url = result['data']['links']['self']
            report = requests.get(id_url, headers=headers).json()
            report_result = report['data']['attributes']['stats']
            engins = report['data']['attributes']['results']
            return render(request, 'user-temp/urlscanresult.html',{'report_result': report_result, 'engins':engins})
        else:
            return JsonResponse({'error': 'Failed to scan the link'}, status=response.status_code)

    return render(request, 'scan_link.html')
