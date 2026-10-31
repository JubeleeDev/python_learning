
from zoneinfo import ZoneInfo
import datetime as dt

def hours_until(deadline: dt.datetime) -> float:
    if deadline.tzinfo is None:
        raise ValueError("deadline must have a timezone")

    current_moment = dt.datetime.now().astimezone()

    if current_moment >= deadline:
        return 0
    else:
        return ((deadline - current_moment) / dt.timedelta(hours=1))


if __name__ == "__main__":
    aware = dt.datetime.now(tz=ZoneInfo("Europe/Moscow"))
    print("Moscow/Europe time is", aware)
    utc = aware.astimezone(dt.timezone.utc)
    print("UTC moment is", utc)
    
    minutes = dt.timedelta(minutes=90)
    print(f"Moscow now is {aware}, 90 minutes ago is {aware - minutes}")

    print(hours_until(dt.datetime.now().astimezone(tz=ZoneInfo("Europe/Moscow")) + dt.timedelta(hours=2)))

    try:
        hours_until(dt.datetime.now())
    except ValueError:
        print("got naive error")
