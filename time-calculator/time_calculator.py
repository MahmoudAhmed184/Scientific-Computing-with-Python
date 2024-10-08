HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
DAYS_IN_WEEK = 7
WEEK_DAYS = [
    "saturday",
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
]


def convert_to_twenty_four_hour_form(hour: int, period: str) -> int:
    if hour == 12 and period == "AM":
        return 0
    if hour == 12 and period == "PM":
        return 12
    if period == "PM":
        return hour + 12
    return hour


def convert_to_twelve_hour_form(hour: int) -> tuple:
    if hour == 0:
        return 12, "AM"
    if hour == 12:
        return 12, "PM"
    if hour > 12:
        return hour - 12, "PM"
    return hour, "AM"


def add_time(start_time: str, duration: str, day_of_week: str = None) -> str:
    initial_time, period = start_time.split()
    initial_hours, initial_minutes = map(int, initial_time.split(":"))

    initial_hours = convert_to_twenty_four_hour_form(initial_hours, period)

    duration_hours, duration_minutes = map(int, duration.split(":"))

    total_minutes = initial_minutes + duration_minutes
    total_hours = initial_hours + duration_hours + (total_minutes // MINUTES_IN_HOUR)

    updated_minutes = total_minutes % MINUTES_IN_HOUR
    updated_hours = total_hours % HOURS_IN_DAY

    updated_hours, period = convert_to_twelve_hour_form(updated_hours)

    updated_time = f"{updated_hours}:{updated_minutes:02} {period}"

    days_passed = total_hours // HOURS_IN_DAY

    if day_of_week:
        day_index = WEEK_DAYS.index(day_of_week.lower())
        updated_day = WEEK_DAYS[(day_index + days_passed) % DAYS_IN_WEEK]
        updated_time += f", {updated_day.capitalize()}"

    if days_passed == 1:
        updated_time += " (next day)"
    elif days_passed > 1:
        updated_time += f" ({days_passed} days later)"

    return updated_time
