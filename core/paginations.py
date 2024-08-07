import math

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PagePagination(PageNumberPagination):
    page_size = 3
    max_page_size = 10
    page_size_query_param = 'p_size'

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        total_pages = math.ceil(count / self.get_page_size(self.request))
        return Response({
            'total_items': count,
            'total_pages': total_pages,
            'prev': self.page.previous_page_number() if self.get_previous_link() else None,
            'next': self.page.next_page_number() if self.get_next_link() else None,
            'results': data
        })
