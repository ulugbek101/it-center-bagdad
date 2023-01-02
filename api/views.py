from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import GroupSerializer

from main.models import Group, Pupil, Subject, Teacher


@api_view(['GET'])
def group_delete(request):
    model_name = request.GET.get('model')
    pk = request.GET.get('pk')

    if model_name == 'group':
        item = Group.objects.get(id=pk)
        if request.GET.get('confirm'):
            deleted = 'false'
            try:
                item.delete()
                deleted = 'true'
            except:
                pass

            return Response({
                'deleted': deleted,
                'id': pk,
            })

        else:
            serialized_item = GroupSerializer(item, many=False).data
            serialized_item[
                'confirmationText'] = f"{serialized_item.get('name')} guruhini o'chirishga ishinchingiz komilmi ? " \
                                      f"Agar davom etsangiz, guruh va bu guruhda ro'yxatda olingan barcha o'quvchilar " \
                                      f"butkul o'chib ketadi"
            return Response(serialized_item)
    return
