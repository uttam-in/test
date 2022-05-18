import jwt
from account.models import Doctor


def isAunthenticated(token):

    try:

        payload = dict(jwt.decode(token, 'secret', algorithms=['HS256']))
        user = Doctor.objects.get(pk=payload.get('id', ''))

        if user:
            return True
        else:
            return False
    except:
        return False