# from django.shortcuts import render
# from rest_framework.views import APIView

# from rest_framework.response import Response

# from meteo.models import React

# from .serializers import ReactSerializer
# from rest_framework import viewsets

# # Create your views here.

# class ReactViewSet(viewsets.ModelViewSet):
#     queryset = React.objects.all()
#     serializer_class = ReactSerializer

# class ReactView(APIView):
#     def get(self, request):
#         output= [{"Lieu":output.Lieu,
#             "Date":output.Date,
#             "temp":output.Temp,
#             "vent":output.vent,
#             "precepitation":output.precepitation,
#             "humidite":output.humidite}
#             for output in React.objects.all()]
#         return Response(output)
    
#     def post(self, request):
#         serializer=ReactSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#         return Response(serializer.data)


from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from .models import React
from .serializers import CreateReactSerializer, ReactSerializer
from rest_framework import viewsets


def ReactAPI(request):
    if request.method == 'POST':
        Lieu = request.POST.get('Lieu')
        Date = request.POST.get('Date')
        temp = request.POST.get('Température')
        vent = request.POST.get('Vent')
        precepitation = request.POST.get('Précipitation')
        humidite = request.POST.get('Humidité')
        icon = request.POST.get('Icon')

        print("Received data:")
        print("Lieu:", Lieu)
        print("Date:", Date)
        print("Température:", temp)
        print("Vent:", vent)
        print("Précipitation:", precepitation)
        print("Humidité:", humidite)
        print("Icon:", icon)
    
    return HttpResponse("Data received successfully")


# class mavue(APIView):
#     def post(self,request):
#         data=request.data
#         print(data)
#         serializer=ReactSerializer(data=data)
#         if serializer.is_valid():
#             serializer.serial.save()
            
#         return Response({"message":"L element est bien inseré ."},status=status.HTTP_201_CREATED)
    

@csrf_exempt
def ReactAPI(request, pk=0):
    if request.method =='GET':
        react = React.objects.all()
        react_serializer = ReactSerializer(react, many=True)
        return JsonResponse(react_serializer.data, safe=False)
    elif request.method == 'POST':
        Lieu = request.POST.get('Lieu')
        Date = request.POST.get('Date')
        temp = request.POST.get('Température')
        vent = request.POST.get('vent')
        precepitation = request.POST.get('Précipitation')
        humidite = request.POST.get('Humidité')
        icon = request.POST.get('Icon')

        react_data = {
        'Lieu': Lieu,
        'Date': Date,
        'Température': temp,
        'Vent': vent,
        'Précipitation': precepitation,
        'Humidité': humidite,
        'Icon': icon
    }

    # Initialize serializer with the data
        react_serializer = ReactSerializer(data=react_data)

    # Check if serializer is valid
        if react_serializer.is_valid():
        # Save the data
            react_serializer.save()
            return JsonResponse("Adding successfully", safe=False)
        return JsonResponse("Failed to add successfully", safe=False)
    elif request.method =='Put':
        react_data = JSONParser().parse(request)
        print("meteo data")
        print(react_data)
        print("meteo ID")
        react = React.objects.get(id=react_data[id])
        print("meteo")
        react_serializer = ReactSerializer(react, data=react_data)
        if react_serializer.is_valid():
            react_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method =='DELETE':
        react = React.objects.get(reactId=pk)
        react.delete()
        return JsonResponse("meteo was Deleted successfully", safe=False)


# class ReactViewSet(viewsets.ModelViewSet):
#     queryset = React.objects.all()
#     serializer_class = ReactSerializer

# class ReactListView(APIView):
#     def get(self, request):
#         forecasts = React.objects.all()
#         serializer = ReactSerializer(forecasts, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ReactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# @api_view(['GET','POST'])
# def meteo_list(request):



#     if request.method == 'GET':
#         meteo =React.objects.all()
#         serializer = ReactSerializer(meteo, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer=ReactSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreateReactView(APIView):
#     serializer_class = CreateReactSerializer


#     def post (self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         serializer = self.serializer_class(data= request.data)
#         if serializer.is_valid():
#             Lieu =serializer.data.get('Lieu')
#             Date = serializer.data.get('Date')
#             temp = serializer.data.get('temp')
#             vent = serializer.data.get('vent')
#             precepitation = serializer.data.get('preceitation')
#             humidite = serializer.data.get('humidite')
#             queryset= React.objects.filter(Lieu=Lieu)
#             if queryset.exists():
#                 react = queryset[0]
#                 react.Lieu=Lieu
#                 react.Date = Date
#                 react.temp=temp
#                 react.vent=vent
#                 react.precepitation=precepitation
#                 react.humidite=humidite
#                 react.save(update_fields=['temp','Lieu','Date','temp','precepitation','humidite'])
                
#             else:
#                 react= React(Lieu=Lieu,Date=Date,Precepitation=precepitation, humidite=humidite,vent=vent)
#                 react.save()

#             return Response(ReactSerializer(react).data, status=status.HTTP_200_OK)