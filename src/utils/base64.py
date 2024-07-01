import json
import base64


def b64_to_dict(b64):
    decoded_bytes = base64.b64decode(b64)
    decoded_str = decoded_bytes.decode("utf-8")
    return json.loads(decoded_str)
