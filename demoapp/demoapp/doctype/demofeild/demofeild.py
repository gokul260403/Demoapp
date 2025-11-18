# Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class demofeild(Document):
    def before_save(self):
        frappe.msgprint(str(self.duration_lekp))
