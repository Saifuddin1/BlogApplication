from django.shortcuts import render,redirect
from .forms import UserRegistration,UserLoginForm,PostCreateForm
from .models import User,Post
from django.http import HttpResponseRedirect
# Create your views here.



def user_registration(request):
    if request.method == "POST":
        form = UserRegistration(request.POST)
        if form.is_valid():
            name = form.cleaned_data['user_name']
            email = form.cleaned_data['user_email']
            password = form.cleaned_data['user_password']
            phone = form.cleaned_data['user_phone']
            user = User(user_name = name,user_email = email,user_password = password,user_phone = phone)
            user.save()
            form = UserRegistration()
    else:
        form = UserRegistration()
    return render(request,"blog_app/userregistration.html",{"form":form})



def user_login(request):
    login_form = UserLoginForm()
    remove_session(request)
    # context: Dict[str, Any] = {'form': PatientLoginForm}
    if request.method == 'POST':
        email = request.POST.get('user_email')
        password = request.POST.get('user_password')
        user_record = User.objects.filter(user_email=email).first()
        if user_record and user_record.user_password == password:
            print("yes you are logged in ")
            request.session['username'] = email
            request.session['id'] = user_record.pk
            return redirect('get_post')
        else:
            return render(request, 'blog_app/login.html')
    return render(request, 'blog_app/login.html',{"form":login_form})



def edit_user_profile(request):
    # user = request.session.get('username')
    if not request.session.get('username'):
        remove_session(request)
        return redirect('login')
    user_id = request.session.get('id')
    if request.method == 'POST':
        pi = User.objects.get(pk=user_id)
        form = UserRegistration(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        pi = User.objects.get(pk = user_id)
        form = UserRegistration(instance = pi)
    return render(request, 'blog_app/edit_profile.html', {'form': form})


def user_profile(request):
    if not request.session.get('username'):
        remove_session(request)
        return redirect('login')
    user_data = User.objects.get(id = request.session.get('id'))
    form = UserRegistration(instance = user_data)  
    return render(request, 'blog_app/user_profile.html', {'form': form})





def about(request):
    return render(request,"blog_app/about.html")



def remove_session(request):
    session_keys_to_remove = ["username","id"]
    for key in session_keys_to_remove:
        if request.session.get(key):
            del request.session[key]



def user_logout(request):
    remove_session(request)
    return redirect('login')




def create_post(request):
    if not request.session.get('username'):
        remove_session(request)
        return redirect('login')
    user_id = request.session.get("id")
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            user = user_id
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            post = Post(user_id = user_id,title = title,body = body)
            post.save()
            return redirect('get_post')
            
    else:
        form = PostCreateForm()
    return render(request,"blog_app/create_post.html",{"form":form})


def get_post(request):
    all_posts = Post.objects.all()
    return render(request,"blog_app/posts.html",{"posts":all_posts})


def update_post(request,id):
    if not request.session.get('username'):
        remove_session(request)
        return redirect('login')
    if request.method == 'POST':
        pi = Post.objects.get(pk = id)
        form = PostCreateForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('get_post')
    else:
        pi = Post.objects.get(pk = id)
        form = PostCreateForm(instance = pi)
    return render(request,"blog_app/update_post.html",{"form":form})


def delete_post(request,id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/get_post/')


def contact(request):
    return render(request,"blog_app/contact.html")


def post_detail(request,id):
    post = Post.objects.get(id = id)
    user_id = post.user_id
    user = User.objects.get(id = user_id)
    print(user.user_name)
    return render(request,"blog_app/post_detail.html",{"post":post,"user":user})
    

