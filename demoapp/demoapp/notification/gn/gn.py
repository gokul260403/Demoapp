import frappe

def get_context(context):
	# do your magic here
	pass


 

# def hourly_notification():
     
#     frappe.publish_realtime(
#         event="msgprint",
#         message="⏰ Hourly Scheduler Triggered!",
#         user="Administrator"
#     )
 
#     frappe.logger().info("⏰ Hourly notification sent to Administrator.")

def hourly_notification():
   
    frappe.get_doc({
        "doctype": "Notification Log",
        "subject": "Hourly Notification",
        "email_content": "Scheduler ran successfully!",
        "for_user": "Administrator",
        "type": "Alert"
    }).insert(ignore_permissions=True)

    frappe.db.commit()
    return "Notification Sent"