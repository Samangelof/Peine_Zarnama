from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from paypalrestsdk import Payment, exceptions
from managements.models import Product
from .models import TariffPlan
from .serializers import PostPublicationPaymentSerializer



class PostPublicationPaymentView(APIView):
    def post(self, request):
        serializer = PostPublicationPaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tariff_plan = serializer.validated_data['tariff_plan']
        try:
            tariff_plan = TariffPlan.objects.get(id=tariff_plan)
        except TariffPlan.DoesNotExist:
            return Response({"error": "Invalid tariff plan ID"}, status=status.HTTP_400_BAD_REQUEST)

        amount = tariff_plan.price
        currency = tariff_plan.currency

        payment = Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": "http://localhost:4942/api/v4/pay/payment/execute/",
                "cancel_url": "http://localhost:4942/payment/cancel/"
            },
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": tariff_plan.name,
                        "sku": "tariff_plan",
                        "price": str(amount),
                        "currency": currency,
                        "quantity": 1
                    }]
                },
                "amount": {
                    "total": str(amount),
                    "currency": currency
                },
                "description": "Payment for tariff plan: {}".format(tariff_plan.name)
            }]
        })

        if payment.create():
            for link in payment.links:
                if link.rel == "approval_url":
                    approval_url = str(link.href)
                    return Response({"approval_url": approval_url, "paymentID": payment.id}, status=status.HTTP_200_OK)
        else:
            return Response({"error": payment.error}, status=status.HTTP_400_BAD_REQUEST)




class ExecutePaymentView(APIView):
    def post(self, request):
        payment_id = request.data.get('payment_id')
        payer_id = request.data.get('payer_id')

        if not payment_id or not payer_id:
            return Response({"error": "payment_id and payer_id are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payment = Payment.find(payment_id)
        except exceptions.ResourceNotFound as e:
            return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)

        if payment.execute({"payer_id": payer_id}):
            # Получаем идентификатор продукта, для которого оплачивался тариф
            product_id = request.data.get('product_id')
            if not product_id:
                return Response({"error": "product_id is required."}, status=status.HTTP_400_BAD_REQUEST)

            # Изменяем поле tariff_paid на True
            try:
                product = Product.objects.get(id=product_id)
                product.tariff_paid = True
                product.status = 'active'  # Изменяем статус на "Активный"
                product.save()
            except Product.DoesNotExist:
                return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

            return Response({"message": "Payment executed successfully. Tariff active."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": payment.error}, status=status.HTTP_400_BAD_REQUEST)


class CancelPaymentView(APIView):
    def get(self, request):
        payment_id = request.GET.get('payment_id')
        if not payment_id:
            return Response({"error": "payment_id is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            payment = Payment.find(payment_id)
            if payment.state == 'created' or payment.state == 'approved':
                payment = payment.cancel()
                if payment.success():
                    return Response({"message": "Payment cancelled"}, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "Failed to cancel payment"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"error": "Payment cannot be cancelled"}, status=status.HTTP_400_BAD_REQUEST)
        except exceptions.ResourceNotFound as e:
            return Response({"error": "Payment not found."}, status=status.HTTP_404_NOT_FOUND)