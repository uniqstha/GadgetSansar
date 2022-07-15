from .cart import Cart

def cart_total_amount(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        total_bill=0.00
        for key,value in request.session['cart'].items():
            total_bill = total_bill+((float(value['price']) * value['quantity']))
        return {'cart_total_amount' : total_bill} 
    else:
        return {'cart_total_amount' : 0} 
def tax(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        total_tax=0.00
        for key,value in request.session['cart'].items():
            total_tax =total_tax+(float(value['price']) * value['quantity'])*0.13
        return {'tax' : round(total_tax, 2)} 
    else:
        return {'tax' : 0} 
def totalwithtax(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        total=0.00
        for key,value in request.session['cart'].items():
            total = total+(((float(value['price']) * value['quantity'])*0.13)+(float(value['price']) * value['quantity']))
            print(round(total, 2))
        return {'totalwithtax' : round(total, 2)} 
        
    else:
        return {'totalwithtax' : 0} 


