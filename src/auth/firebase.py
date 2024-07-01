from firebase_admin import initialize_app
from firebase_admin import credentials
from firebase_admin import auth
from configs.settings import settings
from utils.base64 import b64_to_dict
from errors import CustomException
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


def initialize_firebase():
    fb_certificate = b64_to_dict(settings.firebase_api_key)
    fb_credentials = credentials.Certificate(fb_certificate)
    initialize_app(fb_credentials)


def get_firebase_user(
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
):
    """Get the user details from Firebase, based on TokenID in the request"""
    try:
        id_token = credentials.credentials
    except Exception:
        raise CustomException(
            status_code=401,
            error_code="G2",
            description="Unauthorized: Token not found in the request headers",
        )

    try:
        claims = auth.verify_id_token(id_token)
        return claims
    except Exception as e:
        raise CustomException(
            status_code=401,
            error_code="G2",
            description=f"Unauthorized: Invalid Token. {str(e)}",
        )
