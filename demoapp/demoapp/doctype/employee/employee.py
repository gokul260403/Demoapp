# Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Employee(Document):
    def before_insert(self):
        total_leave = frappe.db.get_single_value('Leave Settings', 'total_leave')
        self.remaining_leave=total_leave
       


@frappe.whitelist()
def create_employee(employee_name,role,email):
    doc = frappe.get_doc({
        "doctype": "Employee",
        "employee_name": employee_name,
        "role": role,
        "email": email
    })
    doc.insert()
    frappe.db.commit()
    return {"message":"Employee Created","name":doc.name}


@frappe.whitelist()
def read_employee(name=None):
	if name:
		doc = frappe.get_doc("Employee",name)
		return doc.as_dict()
	else:
		employees=frappe.get_all("Employee",fields=["employee_name","role","email"])
	return employees

# @frappe.whitelist()
# def update_employee(name):
#     doc=frappe.get_doc("Employee",name)
#     doc.save()
#     frappe.db.commit()
#     return{"message":"updated","name":doc.name}



# @frappe.whitelist()
# def update_employee(name, **kwargs):
#     doc = frappe.get_doc("Employee", name)    
#     doc.update(kwargs)                       
#     doc.save()                               
#     frappe.db.commit()                       
#     return {"message": "Employee updated successfully", "name": doc.name}



@frappe.whitelist()
def update_employee(name=None):
        data = frappe.request.json or {}
        doc = frappe.get_doc("Employee", data.get(name))
        doc.employee_name = data.get("employee_name")
        doc.role = data.get("role")
        doc.email = data.get("email")
        doc.save()
        frappe.db.commit()
        return {"message": "Student updated successfully", "data": doc}
 

@frappe.whitelist()
def delete_employee(name):
    doc=frappe.delete_doc("Employee",name)
    frappe.db.commit()
    return{"message":"deleted","name":doc.name}

# @frappe.whitelist()
# def update_employee(name):
# 	doc = frappe.get_doc("Employee", name)
# 	for key, value in kwargs.items():
# 		if key in doc.as_dict():
# 			setattr(doc, key, value)

# 	doc.save()
# 	frappe.db.commit()

# 	return {"message": "Employee updated", "name": doc.name, "updated_fields": kwargs}

