
def describe_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 201:
            return "Created"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            return "Server Error"
        case _:
            return "Unknown"

def handle_event(event: dict) -> str:
    match event:
        case {"type": "login", "user": user}:
            return f"{user} logged in"
        case {"type": "logout", "user": user}:
            return f"{user} logged out"
        case {"type": "purchase", "user": user, "amount": amount} if amount > 1000:
            return f"big purchase by {user}"
        case {"type": "purchase", "user": user, "amount": amount} if amount <= 1000:
            return f"purchase by {user}"
        case _:
            return "unknown event"


if __name__ == "__main__":

    check_code: list[int] = [200, 201, 404, 503, 2000]
    for code in check_code:
        print(f"status check for code {code}. Returned status is {describe_status(code)}")

    events: list[dict] = []
    events.append({"type": "login", "user": "qwerty"})
    events.append({"type": "logout", "user": "qwerty"})
    events.append({"type": "purchase", "user": "qwerty", "amount": 1001})
    events.append({"type": "purchase", "user": "qwerty", "amount": 999})
    events.append({"type": "delete", "user": "qwerty"})

    for event in events:
        print(f"check event {event}. Returned event status is {handle_event(event)}")
        print("-" * 20)


    
