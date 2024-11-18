from drf_spectacular.utils import OpenApiResponse, extend_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from connector.operations import CalculateProductionPlanOperations
from connector.serializers import (
    ProductionPlanRequestSerializer,
    ProductionPlanResponseSerializer,
)


@extend_schema(tags=['production-plan'])
class ProductionPlanView(APIView):
    """
    Production Plan view
    """

    permission_classes = (permissions.AllowAny,)

    request_serializer_class = ProductionPlanRequestSerializer
    response_serializer_class = ProductionPlanResponseSerializer

    @extend_schema(
        responses={
            200: OpenApiResponse(
                description='Request success',
                response=response_serializer_class,
            ),
            400: OpenApiResponse(description='Invalid value'),
            500: OpenApiResponse(description='Internal server error'),
        },
        request=request_serializer_class,
    )
    def post(self, request):
        # Serialize request data to make sure it's in correct format
        request_serializer = self.request_serializer_class(data=request.data)
        request_serializer.is_valid(raise_exception=True)

        # Calculate the production plan
        result = CalculateProductionPlanOperations(
            request_serializer.validated_data
        ).calculate_production()

        # Serialize result to make sure it's in correct format
        response_serializer = self.response_serializer_class(
            data=result, many=True
        )
        response_serializer.is_valid(raise_exception=True)

        return Response(result, status=status.HTTP_200_OK)
