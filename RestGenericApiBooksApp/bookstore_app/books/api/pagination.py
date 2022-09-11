from rest_framework.pagination import PageNumberPagination


class SmallPagination(PageNumberPagination):
    """ Small size pagination """
    page_size = 5


class LargePagination(PageNumberPagination):
    """ Large size pagination """
    page_size = 30
