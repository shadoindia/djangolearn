from django.shortcuts import render
from school.models import Person
from rest_framework.response import Response
from rest_framework.views import APIView

class get_data(APIView):

    def get(self,request):
        per=Person.objects.all()
        for i in per:
            print('*****',i.personid,i.lastname,i.firstname)
        return Response({'succss':True})

