import os

from langfuse import get_client

from app.core.config import settings

os.environ["LANGFUSE_HOST"] = settings.LANGFUSE_HOST
os.environ["LANGFUSE_PUBLIC_KEY"] = settings.LANGFUSE_PUBLIC_KEY
os.environ["LANGFUSE_SECRET_KEY"] = settings.LANGFUSE_SECRET_KEY

langfuse = get_client()
