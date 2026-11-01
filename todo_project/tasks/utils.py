
def convert_to_number(value: str, name: str, show_error: bool = True) -> int | None:
    result = None
    
    try:
        result = int(value)
    except ValueError:
        if show_error:
            print(f"cannot convert {name} value to int")
    return result