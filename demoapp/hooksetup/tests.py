import frappe
def before_tests():
    if not frappe.db.exists("User", "test@example.com"):
        frappe.get_doc({
            "doctype": "User",
            "email": "test@example.com",
            "first_name": "Test",
            "roles": [{"role": "System Manager"}]
        }).insert()