import json
from http import HTTPStatus

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from customers.models import Customer
from orders.validators import validate_order
from orders.models import Order
from robots.models import Robot


@csrf_exempt
def create_order(request):
    """
    View-функция, отвечающая за создание и добавление заказа робота
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            status, response = validate_order(data)
            if not status:
                return JsonResponse(response, status=HTTPStatus.BAD_REQUEST)

            customer, _ = Customer.objects.get_or_create(email=data['email'])
            robot_status = Robot.objects.filter(
                serial=data['robot_serial']).exists()
            if not robot_status:
                Order.objects.get_or_create(
                    customer=customer, robot_serial=data['robot_serial'])
                return JsonResponse(
                    {"message": "you have been added to wishlist, wait for an e-mail"},
                    status=HTTPStatus.CREATED)
            else:
                return JsonResponse(
                    {"message": "this robot is available"},
                    status=HTTPStatus.CREATED)
        except Exception as e:
            return JsonResponse(
                {'error': str(e)}, status=HTTPStatus.BAD_REQUEST
            )
    return JsonResponse(
        {"error": "Method not allowed"},
        status=HTTPStatus.METHOD_NOT_ALLOWED
    )
