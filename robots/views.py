from datetime import datetime, timedelta
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse
from django.db.models import Count

from robots.models import Robot
from robots.utils import generate_report


def download_excel_file(request) -> HttpResponse:
    """
    Загружает отчет в формате Excel с информацией о роботах за последнюю неделю.

    :param request: HTTP-запрос.
    :type request: HttpRequest

    :return: HTTP-ответ с файлом Excel в формате XLSX.
    :rtype: HttpResponse
    """
    days_in_report = 7

    if request.method == 'GET':
        current_date = datetime.today()
        previous_week = (current_date - timedelta(days=days_in_report))
        file_data = (Robot.objects
                     .filter(created__range=[previous_week, current_date])
                     .values('model', 'version')
                     .annotate(week_amount=Count('model')))

        excel_data = generate_report(list(file_data))

        response = HttpResponse(
            excel_data,
            content_type='application/vnd.ms-excel')
        response[
            'Content-Disposition'] = 'attachment; filename="robots_report.xlsx"'

        excel_data.save(response)

        return response
    else:
        return JsonResponse(
            {"error": "Method not allowed"},
            status=HTTPStatus.METHOD_NOT_ALLOWED
        )
