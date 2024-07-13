import datetime
import time
import ctypes

def validate_time(alarm_time):
    try:
        datetime.datetime.strptime(alarm_time, "%H:%M")
        return True
    except ValueError:
        return False

def get_alarm_time():
    while True:
        alarm_time = input("HH:MM - ")
        if validate_time(alarm_time):
            return alarm_time
        else:
            print("Invalid time format. Please try again.")

def show_notification():
    ctypes.windll.user32.MessageBoxW(0, "Your alarm is going off!", "Time up!", 0x40 | 0x1)

def countdown_to_alarm(alarm_time):
    while True:
        now = datetime.datetime.now()
        current_time_str = now.strftime("%H:%M")
        alarm_time_obj = datetime.datetime.strptime(alarm_time, "%H:%M").replace(year=now.year, month=now.month, day=now.day)

        if alarm_time_obj < now:
            alarm_time_obj += datetime.timedelta(days=1)

        time_remaining = alarm_time_obj - now
        hours, remainder = divmod(time_remaining.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        print(f"Current time: {current_time_str} | Time remaining: {hours:02}:{minutes:02}:{seconds:02}")

        if current_time_str == alarm_time:
            show_notification()
            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = get_alarm_time()
    countdown_to_alarm(alarm_time)
