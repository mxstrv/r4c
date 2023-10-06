import json
from http import HTTPStatus

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.validators import validate_robot_creation
from orders.models import Order
from orders.utils import send_order_emails
from robots.models import Robot


@csrf_exempt
def create_robot(request):
    """
    View-функция, отвечающая за создание и добавление экземпляра
    робота в БД.
    При создании робота проверяется наличие клиентов, находящихся
    в списке ожидания на данную модель. Если таковые имеются - им
    отправляется электронное письмо формата, указанного в ТЗ.
    """
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            status, response = validate_robot_creation(data)
            if not status:
                return JsonResponse(response, status=HTTPStatus.BAD_REQUEST)
            robot = Robot(
                serial=f'{data["model"]}-{data["version"]}',
                model=data["model"],
                version=data["version"],
                created=data["created"]
            )
            robot.save()

            waiting_list = Order.objects.filter(
                robot_serial=robot.serial).values_list('customer__email', flat=True)
            print(list(waiting_list))
            if waiting_list:
                send_order_emails(model=robot.model, version=robot.version, maillist=waiting_list)

            return JsonResponse(
                {"message": "robot successfully created"},
                status=HTTPStatus.CREATED
            )
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=HTTPStatus.BAD_REQUEST)
    return JsonResponse(
        {"error": "Method not allowed"},
        status=HTTPStatus.METHOD_NOT_ALLOWED
    )
