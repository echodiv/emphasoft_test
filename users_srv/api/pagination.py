from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class SimplePagination(PageNumberPagination):
    """
    Пагинация для вывода всех пользователей без метаданных
    """
    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'meta': {
                'total_page': self.page.paginator.count,
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
            }
        })
