import time,frappe

def my_background_job(text):
    time.sleep(5)
    print(f"Worker running job with text: {text}")
    frappe.get_doc({
        "doctype": "ToDo",
        "description": f"Background job finished: {text}"
    }).insert(ignore_permissions=True)
    frappe.db.commit()