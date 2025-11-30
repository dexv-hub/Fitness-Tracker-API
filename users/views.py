from django.shortcuts import render

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


def test_view(request):
    return JsonResponse({'message': 'Users app is working!'})


@api_view(['GET'])
def users_list(request):
    data = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
    ]
    return Response(data)
