from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from nplusone.models import WebToon


class TestAPI(APIView):
    def get(self, request):
        for webtoon in WebToon.objects.all():
            print(webtoon.writer.name)
        return Response(status=status.HTTP_200_OK)
