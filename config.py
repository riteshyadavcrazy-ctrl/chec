import os
import re
from dotenv import load_dotenv
load_dotenv()


def parse_chat_identifier(value, default=None):
    """Return a Pyrogram-friendly chat identifier.

    Supports numeric IDs, -100 IDs, @usernames, bare public usernames,
    and t.me links. Empty/disabled values return ``default``.
    """
    raw = str(value or "").strip()
    if not raw or raw.lower() in {"0", "none", "false", "off", "disabled", "null"}:
        return default

    # Convert public Telegram links into usernames. Invite links are kept as-is
    # because they cannot be membership-checked without a real chat id.
    match = re.match(r"(?:https?://)?(?:t\.me|telegram\.me)/([^/?#]+)", raw)
    if match:
        slug = match.group(1).strip()
        if slug.startswith("+") or slug in {"joinchat", "c"}:
            return raw
        raw = slug

    if raw.startswith("@"):
        return raw
    if re.fullmatch(r"-?\d+", raw):
        try:
            return int(raw)
        except ValueError:
            return raw
    return raw


# ════════════════════════════════════════════════════════════════════════════════
# ░ CONFIGURATION SETTINGS
# ════════════════════════════════════════════════════════════════════════════════

# VPS --- FILL COOKIES 🍪 in """ ... """ 
INST_COOKIES = """
# write up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

# ─── BOT / DATABASE CONFIG ──────────────────────────────────────────────────────
API_ID       = os.getenv("API_ID", "")
API_HASH     = os.getenv("API_HASH", "")
BOT_TOKEN    = os.getenv("BOT_TOKEN", "")
MONGO_DB     = os.getenv("MONGO_DB", "")
DB_NAME      = os.getenv("DB_NAME", "telegram_downloader")

# ─── OWNER / CONTROL SETTINGS ───────────────────────────────────────────────────
OWNER_ID     = list(map(int, os.getenv("OWNER_ID", "").split()))  # space-separated list
STRING       = os.getenv("STRING", None)  # optional session string
LOG_GROUP    = parse_chat_identifier(os.getenv("LOG_GROUP", "-1001234456"))

# ─── SECURITY KEYS ──────────────────────────────────────────────────────────────
MASTER_KEY   = os.getenv("MASTER_KEY", "gK8HzLfT9QpViJcYeB5wRa3DmN7P2xUq")  # session encryption
IV_KEY       = os.getenv("IV_KEY", "s7Yx5CpVmE3F")  # decryption key

# ─── COOKIES HANDLING ───────────────────────────────────────────────────────────
YT_COOKIES   = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)

# ─── USAGE LIMITS ───────────────────────────────────────────────────────────────
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT  = int(os.getenv("PREMIUM_LIMIT", "500"))

# ════════════════════════════════════════════════════════════════════════════════
# ░ PREMIUM PLANS CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════════

P0 = {
    "d": {
        "s": int(os.getenv("PLAN_D_S", 1)),
        "du": int(os.getenv("PLAN_D_DU", 1)),
        "u": os.getenv("PLAN_D_U", "days"),
        "l": os.getenv("PLAN_D_L", "Daily"),
    },
    "w": {
        "s": int(os.getenv("PLAN_W_S", 3)),
        "du": int(os.getenv("PLAN_W_DU", 1)),
        "u": os.getenv("PLAN_W_U", "weeks"),
        "l": os.getenv("PLAN_W_L", "Weekly"),
    },
    "m": {
        "s": int(os.getenv("PLAN_M_S", 5)),
        "du": int(os.getenv("PLAN_M_DU", 1)),
        "u": os.getenv("PLAN_M_U", "month"),
        "l": os.getenv("PLAN_M_L", "Monthly"),
    },
}

# ════════════════════════════════════════════════════════════════════════════════
# ░ END
# ════════════════════════════════════════════════════════════════════════════════
