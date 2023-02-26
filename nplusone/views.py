from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from nplusone.models import WebToon, UploadDay


@api_view(['GET'])
def own_field_test(request):
    for webtoon in WebToon.objects.all():
        print(webtoon.title)
    return Response(status=status.HTTP_200_OK)


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
def many_to_one_test(request):
    for upload_day in UploadDay.objects.all():
        print([day.title for day in upload_day.webtoon_set.all()])
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def many_to_many_test(request):
    for webtoon in WebToon.objects.all():
        print(webtoon.title, [tag.name for tag in webtoon.tag.all()])
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def one_to_one_solve_test(request):
    for webtoon in WebToon.objects.all().select_related('writer'):
        print(webtoon.writer.name)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def one_to_many_solve_test(request):
    for webtoon in WebToon.objects.all().select_related('upload_date'):
        print(webtoon.upload_date.day)
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def many_to_many_solve_test(request):
    for webtoon in WebToon.objects.all().prefetch_related('tag'):
        print(webtoon.title, [tag.name for tag in webtoon.tag.all()])
    return Response(status=status.HTTP_200_OK)
