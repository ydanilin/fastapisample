import os


API_V1_STR = "/vVelvet1"
PROJECT_NAME = "Velvet API"


# SECRET_KEY = os.getenvb(b"SECRET_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    SECRET_KEY = os.urandom(32)

ACCESS_TOKEN_EXPIRE_MINUTES = 3600 / 60  # There are seconds in the specs


# database info
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_SOCKET = os.getenv("POSTGRES_SOCKET")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
base_uri = (f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@"
            f"{POSTGRES_HOST}/{POSTGRES_DB}")
if not POSTGRES_HOST:
    args_part = f"?host={POSTGRES_SOCKET}"
else:
    args_part = f"?port={POSTGRES_PORT}" if POSTGRES_PORT else ""
SQLALCHEMY_DATABASE_URI = (
    f"{base_uri}{args_part}"
)

# superuser
FIRST_SUPERUSER = os.getenv("FIRST_SUPERUSER")
FIRST_SUPERUSER_PASSWORD = os.getenv("FIRST_SUPERUSER_PASSWORD")
