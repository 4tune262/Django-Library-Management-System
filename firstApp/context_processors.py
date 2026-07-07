# from .models import Cart
#
# def cart_info(request):
#     cart_count = 0
#
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user)
#
#         for item in cart.items.all():
#             cart_count += item.quantity
#
#     return {
#         "cart_count": cart_count,
#         "cart": cart,
#     }
from .models import Cart

def cart_info(request):

    cart = None
    cart_count = 0

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_count = cart.items.count()

    return {
        "cart": cart,
        "cart_count": cart_count,
    }