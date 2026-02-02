start_time_in_system = 0


def get_display_time(number_seconds: int):
    sec = number_seconds % 60
    minute = number_seconds // 60
    return f"{minute:02}:{sec:02}"

import re
import requests
from datetime import datetime, timezone

def get_utc(url, pre, suf):
    """Fetch UTC datetime from a webpage using regex pattern."""
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    match = re.search(rf"{re.escape(pre)}(\d{{9,20}}){re.escape(suf)}", response.text)
    if not match:
        raise ValueError(f"No timestamp found with prefix='{pre}' and suffix='{suf}'")
    return datetime.fromtimestamp(int(match.group(1)), tz=timezone.utc)

def format_date(dt_obj, fmt):
    """Format datetime object as string."""
    return dt_obj.strftime(fmt)

def format_time(dt_obj, fmt):
    """Extract time part from datetime object."""
    return dt_obj.strftime(fmt)
