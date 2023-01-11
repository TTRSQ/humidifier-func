import time
import hashlib
import hmac
import base64
import httpx
import os
from enum import Enum
import json

__API_TOKEN = os.getenv("API_TOKEN")
__API_SECRET = os.getenv("API_SECRET")
__BOT_API_HOST = "https://api.switch-bot.com"


def __create_auth_headers():
    token = __API_TOKEN
    secret = __API_SECRET

    nonce = ""
    t = int(round(time.time() * 1000))
    string_to_sign = "{}{}{}".format(token, t, nonce)

    string_to_sign = bytes(string_to_sign, "utf-8")
    secret = bytes(secret, "utf-8")

    sign = base64.b64encode(
        hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest()
    )

    return {
        "Authorization": token,
        "t": str(t),
        "sign": str(sign, "utf-8"),
        "nonce": nonce,
    }


class Method(Enum):
    GET = 1
    POST = 2


def request_bot_api(path: str, method: Method, param: dict = {}):
    headers = __create_auth_headers()
    res = None
    print(f"[INFO]bot_request\tpath:{path}\tparam:{json.dumps(param)}")
    if method == Method.GET:
        res = httpx.get(__BOT_API_HOST + path, headers=headers, params=param)
    elif method == Method.POST:
        headers["Content-Type"] = "application/json; charset=utf8"
        res = httpx.post(__BOT_API_HOST + path, headers=headers, json=param)
    print(f"[INFO]bot_response\ttext:{res.text}")
    return res.json()
