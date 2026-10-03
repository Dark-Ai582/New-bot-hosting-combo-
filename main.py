import os
import time
import random
import requests
from datetime import datetime
from pytz import timezone  # For Indian time

def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    return []

# Realistic human typing simulation
def realistic_typing_simulation(message):
    words = message.split()
    typed_message = ""
    for word in words:
        typed_message += word + " "
        delay = random.uniform(0.3, 0.9)  # Pause between words
        time.sleep(delay)
    return typed_message.strip()

def send_messages_from_file():
    start_time = time.time()
    message_count = 0
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; SM-G970F) AppleWebKit/537.36 Chrome/90.0.4430.91 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    ]

    india = timezone('Asia/Kolkata')  # Set IST timezone

    while True:
        convo_id = read_file("convo.txt")[0]
        messages = read_file("NP.txt")
        tokens = read_file("tokennum.txt")
        hatters_names = read_file("hattersname.txt")
        speed = int(read_file("time.txt")[0]) if read_file("time.txt")[0].isdigit() else 5

        vikram_name = "\033[1;93m★『VIKRAM K1NG』★\033[0m"

        while True:
            for i in range(len(messages)):
                message = messages[i % len(messages)]
                token = tokens[i % len(tokens)] if tokens else "INVALID_TOKEN"
                hater_name = hatters_names[i % len(hatters_names)] if hatters_names else "Unknown"

                hater_colored = f"\033[1;35m{hater_name}\033[0m"
                message_colored = f"\033[1;96m{message}\033[0m"
                colored_message = f"{hater_colored} {message_colored}"

                current_time_ist = datetime.now(india).strftime("%Y-%m-%d %I:%M:%S %p")
                formatted_time = f"\033[1;97mTime (IST): {current_time_ist}\033[0m"

                uptime_seconds = int(time.time() - start_time)
                uptime_formatted = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))
                uptime_display = f"\033[1;94mUptime: {uptime_formatted}\033[0m"

                delay_used = round(random.uniform(speed, speed + 5), 2)
                delay_display = f"\033[1;95mDelay: {delay_used} sec\033[0m"

                convo_display = f"\033[1;92mGroup ID: {convo_id}\033[0m"
                token_display = f"\033[1;93mToken #{(i % len(tokens)) + 1}\033[0m"

                url = f"https://graph.facebook.com/v17.0/t_{convo_id}/"
                headers = {
                    "User-Agent": random.choice(user_agents),
                    "Accept-Language": "en-US,en;q=0.9",
                    "Content-Type": "application/json"
                }

                try:
                    # Realistic typing simulation
                    typed_message = realistic_typing_simulation(f"{hater_name} {message}")

                    response = requests.post(url, json={"access_token": token, "message": typed_message}, headers=headers)
                    message_count += 1

                    print(f"\n\033[1;41m🚀 FROM BRANDED KAMEENA VIKRAM ☠️\033[0m")
                    print(formatted_time)
                    print(uptime_display)
                    print(delay_display)
                    print(convo_display)
                    print(token_display)
                    print(f"⚔️━━━ {vikram_name} ━━━⚔️")

                    if response.ok:
                        print(f"\033[1;92m[✔] Sent ({message_count}): {colored_message}\033[0m\n")
                    else:
                        print(f"\033[1;91m[x] Failed ({message_count}): {colored_message}\033[0m")
                        print(f"Status Code: {response.status_code}, Response: {response.text}\n")

                    print("  \033[1;97m" + "-" * 60 + "\033[0m\n")

                except Exception as e:
                    print(f"\033[1;91m[!] Exception occurred: {e}\033[0m")

                if message_count % 10 == 0:
                    print("\033[1;33m[!] Taking a short break of 120 seconds to avoid detection...\033[0m")
                    time.sleep(120)
                    print("\033[1;33m[✓] Resumed after rest.\033[0m")

                jitter = random.uniform(0.3, 1.0)
                time.sleep(delay_used + jitter)

if __name__ == "__main__":
    send_messages_from_file()
    
