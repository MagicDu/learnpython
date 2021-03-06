from django.shortcuts import render
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
# Create your views here.
from rest_framework import viewsets
from django.db.models import Q

from .models import Student
from .serializers import StudentSerializers
# Create your views here.


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-pk')
    # 指定序列化的类
    serializer_class = StudentSerializers


User = get_user_model()
# Create your views here.


class CustomBackend(ModelBackend):
    '''
    自定义用户验证(setting.py)
    '''

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(
                Q(username=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
