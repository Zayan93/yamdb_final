from django.utils.encoding import force_text
from rest_framework import status
from rest_framework.exceptions import APIException


class CustomValidator(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'Сервер не доступен'

    def __init__(self, detail, fields, status_code):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = {fields: force_text(detail)}
        else:
            self.detail = {'detail': force_text(self.default_detail)}
