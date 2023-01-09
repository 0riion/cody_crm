from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import User
from .serializers import UserListSerializer


class UserView(viewsets.GenericViewSet):
    model = User
    queryset = None
    permission_classes = None

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.all()
        return self.queryset

    def get_permissions(self):
        if self.request.method in ():
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [IsAuthenticated, ]

        return super().get_permissions()

    def list(self, request):

        email = request.query_params.get('email', None)
        user_name = request.query_params.get('user_name', None)
        created_date_start = request.query_params.get('created_date', None)
        created_date_end = request.query_params.get('created_date', None)

        filter_request = {}
        if user_name:
            filter_request['username'] = user_name

        if email:
            filter_request['email'] = email

        if created_date_start and created_date_end:
            filter_request['created_at__gte'] = created_date_start
            filter_request['created_at__lte'] = created_date_end

        queryset = self.get_queryset().filter(
            is_active=True,
            deleted_at=None,
            **filter_request
        )
        serializer = UserListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
