def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function '{func.__name__}' ....")
        result = func(*args, **kwargs)
        print(f"[LOG] Function '{func.__name__}' completed.")
        return result
