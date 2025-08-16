import pywhatkit as kit
import pandas as pd
import time

# Load reminders
df = pd.read_csv("reminders.csv")

for index, row in df.iterrows():
    name = row['Name']
    message = row['Message']
    phone = row['Phone']
    
    # Add + if missing
    if not str(phone).startswith("+"):
        phone = "+" + str(phone)  

    # Split "HH:MM"
    hour, minute = map(int, row['Time'].split(":"))

    print(f"Sending to {name} ({phone}): {message} at {hour}:{minute}")

    try:
        kit.sendwhatmsg(phone, message, hour, minute, wait_time=15, tab_close=True)
        time.sleep(10)  # gap between messages
    except Exception as e:
        print(f"Failed for {name}: {e}")
