from django.shortcuts import render, redirect
from .models import parts, Contact
from django.contrib import messages

from django.core.mail import send_mail

from django.contrib.auth.decorators import login_required
from cart.cart import Cart

# Create your views here.

def index(request):
    pro = parts.objects.all()
    return render(request, 'index.html', {'pro': pro})

def contact(request):
    if request.method == "POST":
        cname = request.POST['cname']
        cemail = request.POST['cemail']
        cphone = request.POST['cphone']
        cmsg = request.POST['cmsg']

        if len(cname) < 2 or len(cemail) < 2 or len(cphone) < 10 or len(cmsg) < 2:
            messages.info(request, '1')
        else:
            contact = Contact(cname=cname, cemail=cemail, cphone=cphone, cmsg=cmsg)
            contact.save()
    return redirect('/')


########################################    For sending mail ( def ContactUs )  ########################################
def ContactUs(request):
    if request.method == "POST":
        cname = request.POST.get('cname')
        cemail = request.POST.get('cemail')
        cmsg = request.POST.get('cmsg')

        data = {
            'cname': cname,
            'cemail': cemail,
            'cmsg': cmsg

        }
        message = '''
        Message : {}

        From : {}
        '''.format(data['cmsg'], data['cemail'])
        send_mail(data['cname'], message, '', ['broadcominc47@gmail.com'])
        return redirect("/")
    return render(request, "/")


#Add to cart
@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = parts.objects.get(id=id)
    cart.add(product=product)
    return redirect("index")


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = parts.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    cart = Cart(request)
    product = parts.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = parts.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')