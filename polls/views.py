from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response


#from polls.models import Student
#from polls.serializers import StudentSerializers


def index(request):
    print(request.method)
    print(request.GET.get('username'))
    return HttpResponse("Hello, world. You're at the polls R.K.M.")

@csrf_exempt
def post_call(request):
    print(request.method)
    print(request.GET.get('username'))
    return HttpResponse("Hello, world. You're at the polls karuna.")

@csrf_exempt
def put_call(request):
    print(request.method)
    print(request.GET.get('username'))
    return HttpResponse("Hello, world. You're at the polls srini.")

@csrf_exempt
def delete_call(request):
    print(request.method)
    print(request.GET.get('username'))
    return HttpResponse("Hello, world. You're at the polls rikesh.")


class PostMan(APIView):
    def get(self,request):
        str = Student.objects.all()
        # Student.objects.create(name='karuna',age=27)
        data = StudentSerializers(str, many=True)
        return Response({"response": data.data})


    def post(self,request):
        n = request.data['name']
        ages = request.data['age']
        Student.objects.create(name=n, age=ages)
        return Response("karunamoorthy .")

    def put(self,request):
        n = request.data['name']
        new = request.data['up']
        st = Student.objects.filter(name=n).last()
        st.name = new
        st.save()
        return Response("srini .")

    def delete(self,request):
        n = request.data['up']
        Student.objects.filter(name=n).last().delete()
        return Response("rikesh .")

