import frappe
import random
from datetime import datetime

def push_demo_data():
    label = datetime.now().strftime("%H:%M:%S")
    points = [random.randint(0, 100)]
    frappe.publish_realtime("demo_event", {"label": label, "points": points})
