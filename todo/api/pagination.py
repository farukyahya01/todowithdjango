from rest_framework.pagination import PageNumberPagination

class SmallPagination(PageNumberPagination):
    page_size = 25
    page_query_param = 'sayfa'

class MediumPagination(PageNumberPagination):
    page_size = 75
    page_query_param = 'sayfa'

class LargePagination(PageNumberPagination):
    page_size = 150
    page_query_param = 'sayfa'
