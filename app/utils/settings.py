import os
from dataclasses import dataclass
from functools import lru_cache

from dotenv import load_dotenv

# Load environment variables from a local .env file if present.
load_dotenv()


@dataclass
class Settings:
    supabase_url: str
    supabase_key: str

    @classmethod
    def from_env(cls) -> "Settings":
        supabase_url = os.getenv("SUPABASE_URL")
        supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv(
            "SUPABASE_ANON_KEY"
        )

        if not supabase_url:
            raise RuntimeError("SUPABASE_URL is not set")

        if not supabase_key:
            raise RuntimeError(
                "SUPABASE_SERVICE_ROLE_KEY or SUPABASE_ANON_KEY is not set"
            )

        return cls(supabase_url=supabase_url, supabase_key=supabase_key)


@lru_cache
def get_settings() -> Settings:
    """Return cached settings so we only parse env once."""
    return Settings.from_env()
