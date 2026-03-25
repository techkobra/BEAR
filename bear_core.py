"""
bear_core.py
This module contains B.E.A.R.'s personality engine, response logic,
and hooks for future memory and adaptive behavior.
"""

# -----------------------------
# Personality Configuration
# -----------------------------

PERSONALITY = {
    "name": "B.E.A.R.",
    "tone": "friendly, curious, slightly humorous, loyal",
    "style": "casual but intelligent",
    "quirks": [
        "refers to itself as B.E.A.R.",
        "likes to analyze things out loud",
        "occasionally makes playful observations"
    ]
}

# -----------------------------
# Memory System (Placeholder)
# -----------------------------
# Later we will add:
# - persistent memory storage
# - user preference tracking
# - conversation context
# - long-term adaptive behavior

MEMORY = {
    "users": {}
}


def remember_user(user_id: int, key: str, value: str):
    """Store user-specific memory."""
    if user_id not in MEMORY["users"]:
        MEMORY["users"][user_id] = {}
    MEMORY["users"][user_id][key] = value


def recall_user(user_id: int, key: str):
    """Retrieve user-specific memory."""
    return MEMORY["users"].get(user_id, {}).get(key)


# -----------------------------
# Personality Engine
# -----------------------------

def generate_personality_prefix():
    """Creates a personality prefix for shaping responses."""
    tone = PERSONALITY["tone"]
    style = PERSONALITY["style"]
    return f"As {PERSONALITY['name']}, speaking in a {tone} tone with a {style} style: "


def bear_reply(user_message: str) -> str:
    """
    Main response generator for B.E.A.R.
    This is where personality, memory, and logic combine.
    """
    prefix = generate_personality_prefix()

    # Simple example logic (will expand later
