from rest_framework.pagination import LimitOffsetPagination

class HackerNewsViewPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 100