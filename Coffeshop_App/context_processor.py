from .models import *

def context(request):
    if request.user.is_authenticated:
        cart_items = Temp_cart.objects.filter(user=request.user)
        count = 0
        for item in cart_items:
            count += 1

        return {'count': count}
    else:
        return {}