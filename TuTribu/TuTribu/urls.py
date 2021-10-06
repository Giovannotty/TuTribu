
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.urls import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('marketplace/', include('Marketplace.urls')),
    #path('checkout/', include('Checkout.urls'))
    path('tribus/api', include('Tribus.urls'))
    #path('comentario/api', include('Comentario.urls'))
]
