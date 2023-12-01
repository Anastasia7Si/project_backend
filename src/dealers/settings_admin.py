import os

from dotenv import load_dotenv


class Settings:
    """Настройки."""
    load_dotenv()
    ADMIN_PREFIX: str = os.getenv("ADMIN_PREFIX", "admin")
    ADMIN_SITE_NAME: str = os.getenv("ADMIN_SITE_NAME", "FastAdmin")
    ADMIN_SITE_SIGN_IN_LOGO: str = os.getenv(
        "ADMIN_SITE_SIGN_IN_LOGO", "/admin/static/images/sign-in-logo.svg")
    ADMIN_SITE_HEADER_LOGO: str = os.getenv(
        "ADMIN_SITE_HEADER_LOGO", "/admin/static/images/header-logo.svg")
    ADMIN_SITE_FAVICON: str = os.getenv(
        "ADMIN_SITE_FAVICON", "/admin/static/images/favicon.png")
    ADMIN_PRIMARY_COLOR: str = os.getenv(
        "ADMIN_PRIMARY_COLOR", "#009485")
    ADMIN_SESSION_ID_KEY: str = os.getenv(
        "ADMIN_SESSION_ID_KEY", "admin_session_id")
    ADMIN_SESSION_EXPIRED_AT: int = os.getenv(
        "ADMIN_SESSION_EXPIRED_AT", 144000)
    ADMIN_DATE_FORMAT: str = os.getenv(
        "ADMIN_DATE_FORMAT", "YYYY-MM-DD")
    ADMIN_DATETIME_FORMAT: str = os.getenv(
        "ADMIN_DATETIME_FORMAT", "YYYY-MM-DD HH:mm")
    ADMIN_TIME_FORMAT: str = os.getenv("ADMIN_TIME_FORMAT", "HH:mm:ss")
    ADMIN_USER_MODEL: str = os.getenv("ADMIN_USER_MODEL")
    ADMIN_USER_MODEL_USERNAME_FIELD: str = os.getenv(
        "ADMIN_USER_MODEL_USERNAME_FIELD")
    ADMIN_SECRET_KEY: str = os.getenv("ADMIN_SECRET_KEY")
