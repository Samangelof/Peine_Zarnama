from rest_framework import serializers
from .models import TariffPlan


class PostPublicationPaymentSerializer(serializers.Serializer):
    tariff_plan = serializers.IntegerField()

    def validate_tariff_plan_id(self, value):
        try:
            tariff_plan = TariffPlan.objects.get(id=value)
        except TariffPlan.DoesNotExist:
            raise serializers.ValidationError("Invalid tariff plan ID.")
        
        return tariff_plan

    
    
class PayPalExecuteSerializer(serializers.Serializer):
    paymentId = serializers.CharField(required=True)
    PayerID = serializers.CharField(required=True)
