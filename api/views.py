import json
from http import HTTPStatus

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.validators import validate_robot_creation
from robots.models import Robot


@csrf_exempt
def create_robot(request):
    """
    View-функция, отвечающая за создание и добавление экземпляра
    робота в БД.
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
