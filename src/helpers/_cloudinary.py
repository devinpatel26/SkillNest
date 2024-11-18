# config file (e.g., cloudinary_config.py)
import cloudinary
from decouple import config

CLOUDINARY_CLOUD_NAME = config('CLOUDINARY_CLOUD_NAME', default="")
CLOUDINARY_PUBLIC_API_KEY = config('CLOUDINARY_PUBLIC_API_KEY', default="")
CLOUDINARY_API_SECRET = config('CLOUDINARY_API_SECRET', default="")

def cloudinary_init():
    cloudinary.config(
        cloud_name=CLOUDINARY_CLOUD_NAME,
        api_key=CLOUDINARY_PUBLIC_API_KEY,
        api_secret=CLOUDINARY_API_SECRET,
        secure=True
    )
