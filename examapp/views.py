from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from examapp.models import QuestionDb,SubmissionDb
from examapp.serializers import QuestionSerializer,SubmissionSerializer

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):
        qs=QuestionDb.objects.all()
        serializer_instance=QuestionSerializer(qs,many=True)
        return Response(serializer_instance.data)
    
    def post(self,request):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)   #incoming data not exisiting..
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.create(**actual_data)
            return Response(data={"message":"Question added successfully"})  #outgoing data 
        else:
            return Response(data={"errors":serializer_instance.errors})

class QuestionRetrieveUpdateDeleteView(APIView):
    def get(self,request,q_id):
        qs=QuestionDb.objects.get(id=q_id)
        serializer_instance=QuestionSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,q_id):
        form_data=request.data
        serializer_instance=QuestionSerializer(data=form_data)   # form_data contains the new data you want to save, not the existing question from the database
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            QuestionDb.objects.filter(id=q_id).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self,request,q_id):
        QuestionDb.objects.filter(id=q_id).delete()
        return Response({"message":"Question deleted successfully"})

class SubmissionListCreateView(APIView):
    def get(self,request):
        qs=SubmissionDb.objects.all()
        serializer_instance=SubmissionSerializer(qs,many=True)
        return Response(data=serializer_instance.data)
    def post(self,request):
        form_data=request.data
        serializer_instance=SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            SubmissionDb.objects.create(**actual_data)
            return Response(data={"Message":"Answer added successfully"})
        else:
            return Response(data={"errors":serializer_instance.errors})
class SubmissionRetrieveUpdateDeleteView(APIView):
    def get(self,request,ans_id):
        # qs=SubmissionDb.objects.get(id=ans_id)  It returns error if not exist
        qs=get_object_or_404(SubmissionDb,id=ans_id)   #It returns {"detail": "No SubmissionsDb matches the given query."} if not exist
        serializer_instance=SubmissionSerializer(qs)
        return Response(serializer_instance.data)
    def put(self,request,ans_id):
        form_data=request.data
        serializer_instance=SubmissionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            SubmissionDb.objects.filter(id=ans_id).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
    def delete(self,request,ans_id):
        SubmissionDb.objects.filter(id=ans_id).delete()
        return Response({"message":"Answer deleted successfully"})

