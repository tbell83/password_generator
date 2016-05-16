import hashlib
import hmac
import os

github_secret = bytearray(os.environ['SECRET'], 'UTF-8')


def verifyHmacHash(data, signature):
    mac = hmac.new(github_secret, msg=data, digestmod=hashlib.sha1)
    calculated_sig = 'sha1=' + mac.hexdigest()
    if calculated_sig == signature:
        return True
    else:
        return False
