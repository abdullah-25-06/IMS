from django.shortcuts import render,redirect
from django.db.models import Sum
from django.http import HttpResponse
from .models import Product,MedOrder_interm
from django.contrib import messages
# Create your views here.
#--------------------------#
# all User
def index(request):
    return render(request,'main.html')
#--------------------------#
# all regular User
def products(request):
    items = Product.objects.all()
    context={
        'items':items
    }
    return render(request,'Store/products.html',context)

def intermOrder(request,id):
    item = Product.objects.get(pk=int(id))
    if request.method =='POST':
        amount = int(request.POST['amount'])
        if item.quantity >= amount:
            MedOrder_interm.objects.create(
                user = request.user,
                p = item,
                quantity = amount 
            )
            messages.success(request,f'{ item.p_name } is successfully added to your Temporary Cart')
            return redirect('store:products')
        else:
            messages.error(request,f'Store has Just { item.quantity } "{ item.p_name }" You requested for { amount } Sorry!')
            return redirect('store:products')
    
def temp_cart(request,id):
    cart = MedOrder_interm.objects.all().filter(user=id)
    total_amount=cart.aggregate(total=Sum('amount'))
    context={
        'items': cart,
        'total':total_amount
    }
    return render(request,'Store/cart.html',context)

# def confirmOrder(request):
#     pass
#--------------------------#
# all admin User
# def All_Data(request):
#     '''This Will Show Products Comapany Suppliers'''
#     pass

# def All_Order(request):
#     """This Will Show all Orders"""

#--------------------------#