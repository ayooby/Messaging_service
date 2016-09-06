from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login
from panel.views import index
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .forms import UserAddForm
from .models import UserProfile


# Create your views here.


def login_user(request):
    if request.method == "GET":

        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # Return a 'disabled account' error message
                return render(request, 'login.html', {
                    'error': 'your account is disabled , contact support .',
                }, content_type='application/xhtml+xml')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {
                'errror': 'your username or password is invalid, try again.',
            }, content_type='application/xhtml+xml')


def logout_user(request):
    logout(request)
    return redirect('/')


def user_lists(request):
    id = request.GET.get('delete', None)
    if id:
        UserProfile.objects.get(user_id=id).delete()

    users_profile = UserProfile.objects.all()
    context = {'users': users_profile}
    return render(request, 'users.html', context)


def handle_uploaded_file(image):
    import StringIO
    from PIL import Image
    image_file = StringIO.StringIO(image.read())
    image = Image.open(image_file)
    w, h = image.size
    image = image.resize((w/2, h/2), Image.ANTIALIAS)

    image_file = StringIO.StringIO()
    image.save(image_file, 'JPEG', quality=90)
    return image


def user_add(request):
    if request.method == "POST":
        form = UserAddForm(request.POST, request.FILES)
        print form.is_valid()
        if form.is_valid():
            uploaded_form = form.cleaned_data
            username = uploaded_form['username']
            firstname = uploaded_form['firstname']
            lastname = uploaded_form['lastname']
            email = uploaded_form['email']
            password = uploaded_form['password1']
            id = uploaded_form['id']
            pic = ""
            if 'picture' in request.FILES:
                pic = request.FILES['picture']
            if id:
                user = User.objects.get(id=id)
                user.first_name = firstname
                user.last_name = lastname
                user.email = email
                user.set_password(password)
                user.save()
                if 'picture' in request.FILES:
                    usp = UserProfile.objects.get(user_id=id)
                    usp.picture = request.FILES['picture']
                    usp.save()
            else:
                user = User.objects.create_user(username=username,
                                            first_name=firstname, last_name=lastname, email=email, password=password)
                user.save()

                userprofile = UserProfile(picture=pic, user=user)
                # userprofile.picture.save(user.username+".jpg", save=True)
                userprofile.save()
            return HttpResponseRedirect(reverse('users:user_lists'))
        context = {'form': form}
        return render(request, 'add_user.html', context)
    else:
        id = request.GET.get('edit', None)
        data = None
        if id:
            usp = UserProfile.objects.get(user_id=id)
            data = {'username': usp.user.username, 'firstname': usp.user.first_name,
                    'lastname': usp.user.last_name, 'email': usp.user.email, 'id':id}
    form = UserAddForm(initial=data)
    context = {'form': form}
    return render(request, 'add_user.html', context)


def responce_image(address):
    try:
        image_data = open(address, "rb").read()
        return HttpResponse(image_data, content_type="image/png")
    except IOError:
        return address


def getProfilePicture(request):
    userp = None
    try:
        userp = UserProfile.objects.get(user_id=request.user.id)
    except:
        userp = None
    if userp == None:
        res = responce_image("static/dist/img/404_user.png")
    else:
        res = responce_image("users/static/users/picture/{username}.jpg".format(username=userp.user.username))
    return HttpResponse(res)
