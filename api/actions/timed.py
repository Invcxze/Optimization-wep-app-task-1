from rest_framework.response import Response


def length_time(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        result = end - start
        print(result)
        return Response({1: "1"})
    return wrapper



