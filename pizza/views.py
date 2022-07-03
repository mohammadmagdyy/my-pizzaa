from django.utils.html import format_html
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth 
from orders.models import orders
from orders.models import payment
from django.utils import timezone
from orders.models import   orderdetails 
from .models import customers
from .models import products
from datetime import datetime
import re
from django.contrib.auth import authenticate , login

# Create your views here.
def index(request):
    context={
        'products':products.objects.all()
    }
    return render(request,'pages/index.html',context)

def signup(request):
    fname=''
    lname=None
    phone=''
    city=''
    password=''
    email=''
    confirm =''
    gender=''
    matt=None
    matt2=None
    terms=None
    username=None
    if request.method == 'POST' and 'btnsubmitup' in request.POST:
        if 'fname' in request.POST and 'user' in request.POST and 'phone' in request.POST and 'city' in request.POST and 'email' in request.POST and 'confirmpass' in request.POST and 'gender' in request.POST and 'terms' in request.POST and 'pass' in request.POST:
            fname=request.POST['fname']
            username=request.POST['user']
            phone=request.POST['phone']
            city=request.POST['city']
            password=request.POST['pass']
            email=request.POST['email']
            confirm=request.POST['confirmpass']
            gender=request.POST['gender']
            matt=re.match("[0-9]",password)
            matt2=re.match("[a-zA-z]",password)
            ismatched=bool(matt)
            ismatched2=bool(matt2)
            terms=request.POST['terms']
            if fname and username and phone and city and password and email and confirm and gender:
                if password != confirm:
                     messages.warning(request,'passwords must be equal')
                     fname=request.POST['fname']
                     username=request.POST['user']
                     phone=request.POST['phone']
                     city=request.POST['city']
                     password=request.POST['pass']
                     email=request.POST['email']
                     confirm=request.POST['confirmpass']
                     gender=request.POST['gender']
                     return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
           'email':email,
           'confirmpass':confirm,
           'gender':gender
        })
                elif len(password)<8:
                      messages.warning(request,'passwords must contain at 8 characters including an upper case letter , a lower case letter and anumber')
                      fname=request.POST['fname']
                      username=request.POST['user']
                      phone=request.POST['phone']
                      city=request.POST['city']
                      password=request.POST['pass']
                      email=request.POST['email']
                      confirm=request.POST['confirmpass']
                      gender=request.POST['gender']
                      return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
           'email':email,
           'confirmpass':confirm,
           'gender':gender
        })
                elif User.objects.filter(username=username).exists():
                    messages.warning(request,'username already exists')
                    fname=request.POST['fname']
                    username=request.POST['user']
                    phone=request.POST['phone']
                    city=request.POST['city']
                    password=request.POST['pass']
                    email=request.POST['email']
                    confirm=request.POST['confirmpass']
                    gender=request.POST['gender']
                    return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
           'email':email,
           'confirmpass':confirm,
           'gender':gender
        })
                elif  ismatched:
                     messages.warning(request,'passwords must contain at 8 characters including an upper case letter , a lower case letter and anumber ')
                     fname=request.POST['fname']
                     username=request.POST['user']
                     phone=request.POST['phone']
                     city=request.POST['city']
                     password=request.POST['pass']
                     email=request.POST['email']
                     confirm=request.POST['confirmpass']
                     gender=request.POST['gender']
                     return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
           'email':email,
           'confirmpass':confirm,
           'gender':gender
        })
                elif not re.findall("[a-z]",password) or not re.findall("[A-Z]",password)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   :
                     messages.warning(request,'passwords must contain at 8 characters including an upper case letter , a lower case letter and anumber. ')
                     fname=request.POST['fname']
                     username=request.POST['user']
                     phone=request.POST['phone']
                     city=request.POST['city']
                     password=request.POST['pass']
                     email=request.POST['email']
                     confirm=request.POST['confirmpass']
                     gender=request.POST['gender']
                     return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
           'email':email,
           'confirmpass':confirm,
           'gender':gender
        })
                elif User.objects.filter(email=email).exists():
                    messages.warning(request,'email already exists')
                    fname=request.POST['fname']
                    username=request.POST['user']
                    phone=request.POST['phone']
                    city=request.POST['city']
                    password=request.POST['pass']
                    email=request.POST['email']
                    confirm=request.POST['confirmpass']
                    gender=request.POST['gender']
                    return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
           'email':email,
           'confirmpass':confirm,
           'gender':gender
        })
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    
                    
                    user.save()
                    customerprofile=customers(
                        user=user,name=fname,phone=phone,city=city,
                    )
                    customerprofile.save()
                    fname=''
                    username=''
                    phone=''
                    city=''
                    password=''
                    email=''
                    confirm=''
                    gender=''



                    messages.success(request,format_html("you registered sucess ,<a href='/signin' style='color:green;'>sign in</a> if you want to buy any of our product"))
                    return redirect('signup')
                   
        else:
            messages.warning(request,'something went wrong!')
            return render(request,'pages/profile/signup.html',{
           'fname':fname,
           'user':username,
           'phone':phone,
           'city':city,
           'pass':password,
           'email':email,
           'confirmpass':confirm,
           'gender':gender
        })
        


    else:    
        return render(request,'pages/profile/signup.html')

def signin(request):
    username=None
    password=None
    if request.method=='POST' and 'btnsubmit' in request.POST:
       
           username=request.POST['user']
           password=request.POST['psw']
          
           user=auth.authenticate(username=username,password=password)
           if user is not None:
                   auth.login(request,user)
                   messages.success(request,'you have loggined successfully')
                   username=''
                   password=''
           else:
                    messages.warning(request,'wrong username or password!')
                    return render(request,'pages/profile/signin.html',
                    {
                        'username':username,
                        'password':password
                    }
                    )
                  
           return redirect('signin')
    else:  
        return render(request,'pages/profile/signin.html')

def profile(request):
    fname=None
    username=None
    phone=None
    password=None
    confirmpsw=None
    city=None
    gender=None
    email=None
    context=None
    if request.user.is_authenticated:
        customer=customers.objects.get(user=request.user)
        context= {
        'city':customer.city,
        'user':request.user.username,
        'pass':request.user.password,
        'email':request.user.email,
        'fname':customer.name,
        'phone':customer.phone,
    }
        if request.method=='POST' and 'btnsave' in request.POST and 'agree' in request.POST:
            fname=request.POST['fname']
            username=request.POST['user']
            phone=request.POST['phon']
           
            password=request.POST['password']
            confirmpsw=request.POST['conpsw']
            city=request.POST['city']
            email=request.POST['mail']
          
           
            if fname and username and phone and city and password and email and confirmpsw :
                customer.name=fname
                customer.phone=phone
                customer.city=city
                if password != confirmpsw:
                    messages.info(request,'passwords are not equal')
                elif not password.startswith('pbkdf2_sha256$'):
                     request.user.set_password(password)
                    

                
                
                request.user.save()
                customer.save()
                messages.success(request,'your data has been saved')
    else:
         messages.success(request,'you must loggin to edit your profile')
        
         return render(request,'pages/profile/profile.html',context)

    return render(request,'pages/profile/profile.html',context)
    if request.method=='POST' and 'btnsave' in request.POST:
            fname=request.POST['fname']
            username=request.POST['user']
            phone=request.POST['phone']
            city=request.POST['city']
            password=request.POST['pass']
            email=request.POST['email']
            confirm=request.POST['confirmpass']
            gender=request.POST['gender']
            if fname and username and phone and city and password and email and confirmpassword and gender:
                if request.user.is_authenticated and 'agree' in request.POST:
                    pass
    

def logout(request):
    auth.logout(request)
    return redirect('index')
    

def pizza(request):
    return render(request,'pages/product/pizza.html')

def product(request,pro_id):
   
    context={
        'product':get_object_or_404(products,pk=pro_id)
    }
   
    return render(request,'pages/product/product.html',context)
def addtocard(request):
     quantity=None
     order=None
     old_order=None
     if request.method=='POST'and 'btnquantity' in request.POST and 'pro_id' in request.POST and 'price' in request.POST:
        quantity=request.POST['quantity']
        pro_id=request.POST['pro_id']
       
        if request.user.is_authenticated and not request.user.is_anonymous:
            if quantity.isdigit():
                 if int(quantity) >=1:
                     try:
                         order=orders.objects.get(user=request.user,is_finised=False)
                     except orders.DoesNotExist:
                                order=None
                     pro=products.objects.get(id=pro_id)
                     try:
                         old_order=orders.objects.get(user=request.user,is_finised=False)
                     except orders.DoesNotExist:
                         oid_order=None
                     detail=orderdetails.objects.filter(order=old_order,product=pro).exists()
                     if order:
                          if detail:
                             messages.success(request,'you added a new product to your order')
                             orderdetail=orderdetails.objects.get(product=pro,order=old_order) 
                             orderdetail.quatity += int(quantity)
                             orderdetail.save()
                             return redirect('flavor/'+request.POST['pro_id'])
                          else:
                             messages.success(request,'you added a new product to your order')
                            
                             orderdetail=orderdetails.objects.create(product=pro,order=old_order,price=pro.price,quatity=quantity)
                            
                            
                             return redirect('flavor/'+request.POST['pro_id'])
                     else:
                         messages.success(request,'you made a new order successfully ')
                         new_order=orders()
                         new_order.user=request.user
                         new_order.order_date=timezone.now()
                         #new_order.details=
                         new_order.is_finised=False
                         new_order.save()
                         orderdetail=orderdetails.objects.create(product=pro,
                         order=new_order,price=pro.price,quatity=quantity
                         )
                         orderdetail.save()
                         return redirect('flavor/'+request.POST['pro_id'])
                    # order=orders(
                        # user = request.user,order_date=datetime.now().strftime("%d/%m/%y-%H:%M"),order_details=details,is_finished=False
                    #)
                     #order.save()
                     #details=orderdetails(product=product.name,order=order,price=product.price,quantity=quantity)
                    # details.save(

                    # )
                     
                    
                     
                 elif int(quantity)<=0:
                     messages.info(request,'you must order at least one order!')
                     return redirect('flavor/'+request.POST['pro_id'])
        else:
            messages.info(request,'you must loggin to order!')
            return redirect('flavor/'+request.POST['pro_id'])
     else:
            return redirect('flavor/'+request.POST['pro_id'])
def mycard(request):
    orderr=None
    if request.user.is_authenticated and not request.user.is_anonymous:
        try:
            orderr=orders.objects.get(user=request.user,is_finised=False)
        except orders.DoesNotExist:
            orderr=None
        orderdetail=orderdetails.objects.all().filter(order=orderr)
        
        total=0
        result=0
        for sub in orderdetail:
            total += sub.price*sub.quatity
            result =sub.price*sub.quatity
    



        context={
            'customer':customers.objects.get(user=request.user),
            'order':orderr,
            'orderdetails':orderdetails.objects.all().filter(order=orderr),
            'total':total,
            'result':result
        }
    
    return render(request,'pages/product/mycard.html',context)

def about(request):
    return render(request,'pages/product/about.html')

def productss(request):
    context={
        'products':products.objects.all()
    }
    return render(request,'pages/product/products.html',context)

def search(request):
    pname=None
    fprice=None
    sprice=None
    description=None
    pro=None
    checked=None
    if request.method=='POST' and 'btnsearch' in request.POST:
       
        if 'cbcs' in request.POST:
            checked=True
        else:
            checked=False
       
        pro=products.objects.all()
        if 'pname' in request.POST:
            pname=request.POST['pname']
            if pname:
                if checked:
                     pro=pro.filter( name__contains=pname)
                else:
                    pro=pro.filter(name__icontains=pname)
        if 'desc' in request.POST:
            description=request.POST['desc']
            if description:
                if checked:
                    pro=pro.filter( description__contains=description)
                else:
                    pro=pro.filter(description__icontains=description)
        if 'p1' in request.POST and 'p2' in request.POST:
            fprice=request.POST['p1']
            sprice=request.POST['p2']
            if fprice and sprice:
                if fprice.isdigit() and sprice.isdigit():
                  pro=pro.filter(price__gte = fprice,price__lte=sprice) 
            context={
              'products':pro
            }
            return render(request,'pages/product/products.html',context)
    return render(request,'pages/product/search.html')
def remove_from_cart(request,orderdetail_id):
    if request.user.is_authenticated and not request.user.is_anonymous and orderdetail_id:
        orderdetaill=orderdetails.objects.get(id=orderdetail_id)
        if orderdetaill.order.user.id==request.user.id:
             orderdetaill.delete()
    return redirect('mycard')
def add_to_quantity(request,orderdetail_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        orderdetailss=orderdetails.objects.get(id=orderdetail_id)
        if orderdetailss.order.user.id==request.user.id:
            orderdetailss.quatity=(orderdetailss.quatity)+1
            orderdetailss.save()
        return redirect('mycard')

def sub_from_quantity(request,orderdetail_id):
     if request.user.is_authenticated and not request.user.is_anonymous:
        orderdetailss=orderdetails.objects.get(id=orderdetail_id)
        if orderdetailss.order.user.id==request.user.id:
            orderdetailss.quatity=(orderdetailss.quatity)-1
            orderdetailss.save()
        return redirect('mycard')

def paymentt(request):
    context=None
    shipmentaddresse=None
    shipmentphonee=None
    cardnumbere=None
    expiredatee=None
    securitycodee=None
    orderss=None
    if request.method=='POST' and 'shipmentaddress' in request.POST and 'shipmentphone' in request.POST and 'cardnumber' in request.POST and 'expiredate' in request.POST and 'securitycode' in request.POST:
        shipmentaddresse=request.POST['shipmentaddress']
        shipmentphonee=request.POST['shipmentphone']
        cardnumbere=request.POST['cardnumber']
        expiredatee=request.POST['expiredate']
        securitycodee=request.POST['securitycode']
        if  shipmentaddresse and shipmentphonee and  cardnumbere and  expiredatee and securitycodee:
            if request.user.is_authenticated and not request.user.is_anonymous:
                if orders.objects.all().filter(user=request.user,is_finised=False):
                    orderss=orders.objects.get(user=request.user,is_finised=False)
                    paymente=payment(order=orderss,shipmentaddress=shipmentaddresse,shipmentphone=shipmentphonee,cardnumber=cardnumbere,expiredate=expiredatee,securitycode=securitycodee)
                    paymente.save()
                    orderss.is_finised=True
                    orderss.save()
                    context={
                            'shipadd':shipmentaddresse,
                            'shipphon':shipmentphonee,
                            'cardno':cardnumbere,
                            'date':expiredatee,
                            'code':securitycodee
                        }
                    messages.success(request,'your order is finished')
                else:
                     messages.success(request,'your order is must loggin finished')
            else:
                  messages.success(request,'your order is must order finished')  
        elif shipmentaddresse=='':
             messages.success(request,'please,Enter the shipment address')
             return redirect('mycard')
        elif shipmentphonee=='':
             messages.success(request,'please,Enter the shipment phone')
             return redirect('mycard')
        
        elif cardnumbere=='':
             messages.success(request,'please,Enter your card number')
             return redirect('mycard')
        elif expiredatee=='':
             messages.success(request,'please,Enter the expire date of your card')
             return redirect('mycard')
        elif securitycodee=='':
             messages.success(request,'please,Enter the security code of your card')
             return redirect('mycard')
    else:
        if request.user.is_authenticated and not request.user.is_anonymous:
            orderr=orders.objects.get(user=request.user)
            orderdetail=orderdetails.objects.all().filter(order=orderr)
            
            total=0
            result=0
            for sub in orderdetail:
                total += sub.price*sub.quatity
                result =sub.price*sub.quatity
            context={
            'customer':customers.objects.get(user=request.user),
            'order':orders.objects.get(user=request.user),
            'orderdetails':orderdetails.objects.all().filter(order=orderr),
            'total':total,
            'result':result
        }



          
            messages.success(request,'your order is not finished')
    return render(request,'pages/product/mycard.html',context)

def generalsearch(request):
    pro=products.objects.all()
    input=None
    if request.method=='POST' and 'inputsearch' in request.POST and 'btnsearch' in request.POST:
        input=request.POST['inputsearch']
        if input.isdigit():
            pro=pro.filter(price__lte=input)
        elif len(input) >15:
            pro=pro.filter(description__icontains=input)
        else:
            pro=pro.filter(name__icontains=input) 
    context={
        'products':pro
    }
    return render(request,'pages/product/products.html',context)

