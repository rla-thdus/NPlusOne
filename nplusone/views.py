from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from nplusone.models import WebToon

@api_view(['GET'])
def one_to_one_test(request):
    for webtoon in WebToon.objects.all():
        print(webtoon.writer.name)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def one_to_many_test(request):
    for webtoon in WebToon.objects.all():
        print(webtoon.upload_date.day)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def many_to_many_test(request):
    for webtoon in WebToon.objects.all():
        print(webtoon.title, [tag.name for tag in webtoon.tag.all()])
    return Response(status=status.HTTP_200_OK)

