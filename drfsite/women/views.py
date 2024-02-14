from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response

from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView


class WomenAPIview(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts': WomenSerializer(w, many=True).data})

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() # автоматически вызовет метод create


        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error":'Method PUT not allowed'})

        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({'error': 'Method PUT not exist'})


        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save() # вызовет метод update
        return Response({"post": serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": 'Method DELETE not allowed'})
        try:
            instance = Women.objects.get(pk=pk)
            instance.delete()
            return Response({"post": "delete post with id: " + str(pk)})
        except Women.DoesNotExist:
            return Response({'error': 'Post with id ' + str(pk) + ' does not exist'})


# class WomenAPIview(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
