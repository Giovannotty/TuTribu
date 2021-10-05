from rest_framework import viewsets

from Tribus.serializers import *

# Create your views here.

class TribuAPI(viewsets.ModelViewSet):
    serializer_class = TribuSerial
    queryset = Tribu.objects.all() #Contiene los objetos que se desean enviar a través del API

class PostAPI(viewsets.ModelViewSet):
    serializer_class = PostSerial
    queryset = Post.objects.all()

class ReaccionAPI(viewsets.ModelViewSet):
    serializer_class = ReaccionSerial
    queryset = Reaccion.objects.all()

class ReaccionPostAPI(viewsets.ModelViewSet):
    serializer_class = ReaccionPostSerial
    queryset = ReaccionPost.objects.all()
    






    
