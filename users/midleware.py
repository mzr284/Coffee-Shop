from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class UpdateLastSeen:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        Response = self.get_response(request)
        if request.user.is_authenticated:
            User.objects.filter(id=request.user.id).update(last_seen=timezone.now())
        return Response