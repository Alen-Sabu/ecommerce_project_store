from django.urls import include, path
from . import views
from wkhtmltopdf.views import PDFTemplateView


urlpatterns = [
    path('cart',views.cart, name="cart"),
    path('', views.shop, name="shop"),
    path('search', views.search, name="product_search"),
    
    path('cart/add_to_cart',views.add_to_cart, name="add_to_cart"),
    path('cart/update-cart',views.updatecart, name="updatecart"),
    path('cart/delete_cart',views.deletecart, name="deletecart"), 

    path('wishlist',views.wishlist, name="wishlist"),
    path('add-to-wishlist', views.addtowishlist, name="addtowishlist"),
    path('cart/delete_wishlist',views.deletewishlist, name="deletewishlist"), 

    path('confirmation',views.order_confirmation, name="order_confirmation"),
    path('placeorder',views.place_order, name="placeorder"),
    path('checkout_guest', views.checkout_guest, name="checkout"),

    path('order_summary',views.order_summary, name="order-summary"),
    path('order_details/<int:id>', views.order_details, name="order-details"),
    path('order/<int:id>/cancel/', views.cancel_order, name='cancel_order'),
    path('filter-data',views.filter_data, name="filter-data"),

    path('address_section', views.address, name="order_address"), 
    path('invoice/<int:order_id>/<int:product_id>', views.invoice, name="invoice"),
    path('return/<int:order_id>/<int:product_id>', views.initiate_return, name="return"),

    path('add_address', views.add_address, name="add_address"),

    path('search/suggestions/', views.search_suggestions, name='search_suggestions'),


    path('apply_coupon', views.apply_coupon, name="apply_coupon"),

    path('payments', views.payment, name="payment"),
    path('cash_on_delivery', views.cash_on_delivery, name="cash_on_delivery"),
    path('proceed-to-pay', views.beforerazorpay, name="razorpay"),
    path('razor_pay', views.razorpay, name="razor_pay"),

    path('process-payment/', views.process_payment, name="process_payment"),
    path('paypal/', include('paypal.standard.ipn.urls')),
    
    path('payment-done/', views.payment_done, name="payment_done"),
    path('payment-cancelled/', views.payment_canceled, name="payment_canccelled"),


]
