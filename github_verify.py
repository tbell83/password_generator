import hashlib
import hmac
import os

secret = os.environ['SECRET']


def verifyHmacHash(data, signature):
    github_secret = bytearray('ThisIsTheSecret', 'UTF-8')
    mac = hmac.new(github_secret, msg=data, digestmod=hashlib.sha1)
    calculated_sig = 'sha1=' + mac.hexdigest()
    if calculated_sig == signature:
        return True
    else:
        return False
