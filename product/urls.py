from django.conf.urls import url, include

from product import views

urlpatterns = [
    url(r'^$', views.product_list, name="product_list"),
    url(r'^(?P<next_pk>\d+)$', views.get_products, name='next-products'),

]