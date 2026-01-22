def normalize_phone(phone: str) -> str:
    """
    Rules:
    - Remove spaces and dashes.
    - If number starts with "+977" and has 10 digits after it → valid.
    - If number starts with "0" and has total length 11 → convert to +977 format.
    - If number has exactly 10 digits and starts with 98 or 97 → add +977.
    - Anything else is invalid.
    """
    p = phone.replace(" ", "").replace("-", "")

    if p.startswith("+977") and len(p) == 14:
        return p

    if p.startswith("0") and len(p) == 11:
        return "+977" + p[1:]

    if len(p) == 10 and (p.startswith("98") or p.startswith("97")):
        return "+977" + p

    raise ValueError("Invalid phone number")