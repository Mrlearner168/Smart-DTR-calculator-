from datetime import datetime, timedelta

def calculate_work_time(time_in_str, time_out_str):
    fmt = "%H:%M"

    time_in = datetime.strptime(time_in_str, fmt)
    time_out = datetime.strptime(time_out_str, fmt)

    if time_out < time_in:
        time_out += timedelta(days=1)

    total_time = time_out - time_in

    total_time -= timedelta(hours=1)

    print(f"Work Duration (after lunch break): {total_time}")
    return total_time


def parse_subtract(command):
    parts = command.lower().split()

    hours = 0
    minutes = 0

    for p in parts:
        if "h" in p:
            hours = int(p.replace("h", ""))
        if "m" in p:
            minutes = int(p.replace("m", ""))

    return hours * 60 + minutes


total_minutes = 0

print("Continuous Work Time Calculator by Rogelio")
print("Enter time in 24-hour format (HH:MM)")
print("Type 'q' to stop")
print("Type 's 30m' or 's 1h 15m' to subtract\n")

while True:

    time_in = input("Time In: ")

    if time_in.lower() == 'q':
        break

    if time_in.lower().startswith("s"):
        try:
            subtract_minutes = parse_subtract(time_in)
            total_minutes -= subtract_minutes

            total_hours = total_minutes // 60
            remaining_minutes = total_minutes % 60

            print(f"Adjusted Total: {total_hours} hours {remaining_minutes} minutes\n")
        except:
            print("Invalid subtract format\n")

        continue

    time_out = input("Time Out: ")

    if time_out.lower() == 'q':
        break

    try:
        work_duration = calculate_work_time(time_in, time_out)

        minutes = int(work_duration.total_seconds() / 60)
        total_minutes += minutes

        total_hours = total_minutes // 60
        remaining_minutes = total_minutes % 60

        print(f"Running Total Work Time: {total_hours} hours {remaining_minutes} minutes\n")

    except ValueError:
        print("Invalid time format. Use HH:MM\n")


print("\nFinal Total Work Time:")

final_hours = total_minutes // 60
final_minutes = total_minutes % 60

print(f"{final_hours} hours {final_minutes} minutes")