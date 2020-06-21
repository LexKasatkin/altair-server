from rest_framework.pagination import LimitOffsetPagination

class LargeLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 30
    max_limit = 120


class StandardResultsSetPagination(LimitOffsetPagination):
    default_limit = 60
    max_limit = 120