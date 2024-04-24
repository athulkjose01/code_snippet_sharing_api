from corsheaders.signals import check_request_enabled

from posts.models import MySite


def cors_allow_mysites(sender, request, **kwargs):
    return MySite.objects.filter(host=request.headers["origin"]).exists()


check_request_enabled.connect(cors_allow_mysites)

# myapp/handlers.py
from corsheaders.signals import check_request_enabled


def cors_allow_api_to_everyone(sender, request, **kwargs):
    return request.path.startswith("/api/")


check_request_enabled.connect(cors_allow_api_to_everyone)