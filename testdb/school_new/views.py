from django.shortcuts import render
from school_new.models import Personnew
from rest_framework.response import Response
from rest_framework.views import APIView

class get_data(APIView):

    def get(self, request):
        per=Personnew.objects.all()
        final_response = []
        for i in per:
            temp = {}
            temp['personid'] = i.personid
            temp['lastname'] = i.lastname
            temp['firstname'] = i.firstname
            final_response.append(temp)
        return Response({'Succss':True, 'data':final_response})

    def post(self, requset):
        req_data = requset.data
        personid = req_data.pop('personid')
        obj, _ = Personnew.objects.get_or_create(personid=personid, defaults=req_data)
        return Response({'Success':True, 'id':obj.personid})


# Create your views here.
