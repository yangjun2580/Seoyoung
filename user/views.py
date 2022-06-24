import os
from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password
from Seoyoung.settings import MEDIA_ROOT


class Join(APIView):
    def get(self, request):
        return render(request, 'user/join.html')

    def post(self, request):
        password = request.data.get('password')
        email = request.data.get('email')
        nickname = request.data.get('nickname')
        name = request.data.get('name')

        if User.objects.filter(email=email).exists() :
            return Response(status=500, data=dict(message='해당 이메일 주소가 존재합니다.'))
        elif User.objects.filter(nickname=nickname).exists() :
            return Response(status=500, data=dict(message='사용자 이름 "' + nickname + '"이(가) 존재합니다.'))

        User.objects.create(password=make_password(password),
                            email=email,
                            nickname=nickname,
                            name=name,
                            profile_image="default_profile.png")

        return Response(status=200, data=dict(message=""))

class Login(APIView):
    def get(self, request):
        return render(request, "user/login.html")

    def post(self, request):

        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = User.objects.filter(email=email).first()

        if user is None:
            return Response(dict(msg="사용자 ID 없음"))

        if user.check_password(password):
            # TODO 로그인한거 세션
            request.session['email'] = email
            return Response(dict(msg="로그인 성공"))
        else:
            return Response(dict(msg="로그인 실패. 패스워드 다름"))



class Logout(APIView):
    def get(self, request):
        request.session.flush()
        return render(request, "user/login.html")


class UploadProfile(APIView):
    def post(self, request):

        # 파일 불러오자
        file = request.FILES['file']
        email = request.data.get('email')

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        profile_image = uuid_name

        user = User.objects.filter(email=email).first()

        user.profile_image = profile_image
        user.save()

        return Response(status=200)

