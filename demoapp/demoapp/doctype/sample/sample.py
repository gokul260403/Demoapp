# Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class sample(Document):
	pass

@frappe.whitelist()  ##created for actions in sample doctype
def gokul():
    frappe.msgprint("Hii")