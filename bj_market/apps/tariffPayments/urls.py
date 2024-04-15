from django.urls import path
from .views import PostPublicationPaymentView, ExecutePaymentView, CancelPaymentView


urlpatterns = [
    path('payment/', PostPublicationPaymentView.as_view(), name='payment'),
    # {
    #     "tariff_plan": "Premium",
    #     "amount": 10.00,
    #     "currency": "USD"
    # }
    path('payment/execute/', ExecutePaymentView.as_view(), name='execute_payment'),
    path('payment/cancel/', CancelPaymentView.as_view(), name='cancel_payment'),


]
