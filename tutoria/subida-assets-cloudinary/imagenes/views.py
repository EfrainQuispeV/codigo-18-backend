from rest_framework.views import APIView
from .serializer import ImagenSerializer
from rest_framework.response import Response
from rest_framework import status

class SubidaImagen(APIView):
    def post(self, request):
       serializer = ImagenSerializer(request.data)
       if serializer.is_valid():
            img_url = serializer.validated_data['img_url']
            img_url.name = 'images/' + img_url.name
            imagen = serializer.save()

            #opbtener la URL completa de cloudinary
            img_url_full = imagen.img_url.url #.url www.claudinary/minube/carpeta/patito.png
            imagen.img_url_full = img_url_full
            imagen.save()

            #actualizamos nuestra respuesta de la URL
            respuesta  = ImagenSerializer(imagen)
            return Response(respuesta.data, status=status.HTTP_201_CREATED)