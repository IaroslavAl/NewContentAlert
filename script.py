import requests
from apscheduler.schedulers.blocking import BlockingScheduler

BOT_TOKEN = "7467267837:AAGIbD1xMAWtXa1z0KoqA-OSJCluzSsKnAI"
CHAT_ID = "-1002378926651"
MESSAGE = "Привет! Это автоматическое уведомление."

def send_telegram_message():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": MESSAGE}
    response = requests.post(url, data=data)

    if response.status_code == 200:
        print("Сообщение успешно отправлено")
    else:
        print(f"Ошибка отправки: {response.text}")

# Создаём планировщик задач
scheduler = BlockingScheduler()
scheduler.add_job(send_telegram_message, "interval", minutes=1)  # Раз в минуту

print("Бот запущен. Нажмите Ctrl+C для выхода.")
scheduler.start()