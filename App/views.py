from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
import pyrebase
from django.contrib import auth

def home(request):
    return render(request,'pages/home.html')

firebaseConfig = {
    'apiKey': "AIzaSyDOKDAESIYsS1Ql2xFYiCYGMsZPoHr52Io",
    'authDomain': "djangofirebaseauth.firebaseapp.com",
    'projectId': "djangofirebaseauth",
    'storageBucket': "djangofirebaseauth.appspot.com",
    'messagingSenderId': "874847614571",
    'appId': "1:874847614571:web:9243771eb8e52f3395e32e",
    'measurementId': "G-GWBE79YQ9C",
    "databaseURL" : "https://djangofirebaseauth-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
authentication = firebase.auth()    # for login logout
database = firebase.database()    # for performing opertions[read, write] on firebase real time database also signup

def loginCredentials(request):
    if request.method == 'POST':
        Email = request.POST['email']
        Password = request.POST['password']
        try: 
            user = authentication.sign_in_with_email_and_password(Email, Password)
            # inform = authentication.get_account_info(user['idToken'])
            # print(inform)
            request.session['idToken'] = str(user['idToken'])
            messages.success(request,"User Successfully SignIn")
            return render(request,'pages/welcome.html')
        except:
            messages.error(request,"Invallid Credentials")
            return redirect('/')
    else:
        return HttpResponse("404 not found")

def Logout(request):
    auth.logout(request)
    return redirect('/')

def signUp(request):
    return render(request,'pages/SignUp.html')

def signUpCredentials(request):
    if request.method == 'POST':
        Name = request.POST['name']
        Email = request.POST['email']
        Password = request.POST['password']
        try:
            user = authentication.create_user_with_email_and_password(Email,Password)
            uid = user['localId']
            data={'name':Name,'status':'1'}
            database.child('users').child(uid).child('details').set(data)

            messages.success(request,'Successfully SignUp')

        except:
            messages.error(request,"Not Signup! Please Try Again")

        return redirect('/signUp')
    else:
        return HttpResponse("404 not found")