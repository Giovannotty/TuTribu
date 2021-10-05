from django.urls import path, include

from Tribus.views import *

from rest_framework.routers import DefaultRouter

#localhost:8000/tribus/API/crud/tribu

router = DefaultRouter()
router.register('tribu',  TribuAPI)
router.register('post', PostAPI)
router.register('reaccion', ReaccionAPI)
router.register('reaccionpost', ReaccionPostAPI)

urlpatterns = [
    path('crud/', include(router.urls))
]