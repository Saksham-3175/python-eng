from notifypy import Notify
import time

notification = Notify(
    default_notification_title="Water Reminder",
    default_notification_message="Drink a glass of Water",
    default_notification_application_name="Python Reminder App",
    # default_notification_urgency="normal",
    # default_notification_audio=""
    # default_notification_icon=""
)
while True:
    notification.send()
    time.sleep(5)