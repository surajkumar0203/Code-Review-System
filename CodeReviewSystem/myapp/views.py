from django.http import JsonResponse
from myapp.tasks import analyze_repo_code
from rest_framework.decorators import api_view
from rest_framework.response import Response
from celery.result import AsyncResult
from myapp.serializers import Start_taskSerializer
import json

@api_view(["POST"])
def start_task(request):
    serializer = Start_taskSerializer(data=request.data)
    if serializer.is_valid():
        url = serializer.validated_data.get('url')
        pr_number = serializer.validated_data.get('pr_number')
        github_token = serializer.validated_data.get('github_token')
        task=analyze_repo_code.delay(url,pr_number,github_token)
        res = AsyncResult(task.id)
        print(task.id)
        return Response({"id": task.id,"status":res.state})
    return Response(serializer.errors, status=400)
    

@api_view(["GET"])
def show_start_task(request,task_id):
    res = AsyncResult(task_id)
    print(task_id)
    if res.state == "SUCCESS":
        return Response({"id": task_id,"status":res.state,"result":res.result})
    return Response({"id": task_id,"status":res.state})
