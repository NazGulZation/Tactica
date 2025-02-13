import time


def generate_id():
    """Generate a unique ID using the current timestamp (to milliseconds) as a string."""
    return str(int(time.time() * 1000))