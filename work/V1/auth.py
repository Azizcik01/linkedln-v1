from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from work.models.auth import User
from work.V1.helper import No_method, UserSerializer


class Sign_in(GenericAPIView, No_method):

    # parser_classes = AllowAny,

    def post(self, request):
        data = request.data

        if 'email' or 'password' not in data:
            return Response({
                'error':'To\'liq ma\'lumot berilmadi! '
            })
        
        user = User.objects.filter(email=data['email']).first()

        if not user:
            return Response({
                'error':'Foydalanuvchi mavjud emas'
            })
        if not user.check_password(data['password']):
            return Response({
                'error':'Xato parol !'
            })
        
        token = Token.objects.get_or_create(user=user)[0]

        return Response({
            'token':token.key
        })


class Sign_up(GenericAPIView, No_method):
    permission_classes = AllowAny,
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        password = data.get('password')

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        user.set_password(str(password))
        user.save()
        
        token = Token.objects.create(user=user)

        return Response({
            'token':token.key
        })
