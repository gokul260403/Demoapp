# Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.search.full_text_search import FullTextSearch

class student(Document):
    # def before_insert(self):
    #     frappe.msgprint("student data saving....")
    # def before_naming(self):
    #     frappe.msgprint("student naming.......")
    # def autoname(self):
    #     self.name=frappe.generate_hash("", 8)
    # def autoname(self):
    #     if self.age == 10:
    #         self.name="hii"
    #     else:
    #         self.name ="hello"+ make_autoname(self.student_name)
    # def before_validate(self):
    #     if self.email:
    #        self.email = self.email.strip().lower()
    # def validate(self):
        # if self.age>30:
    #         frappe.throw("age must be less than 30")
    # def before_save(self):
    #     frappe.msgprint("saved....")
    # def before_submit(self):
    #     pass
    # def before_cancel(self):
    #     frappe.msgprint("cancelled....")
    # def before_update_after_submit(self):
    #     pass
    # def after_insert(self):
    #     frappe.msgprint("student data inserted....")
    # get the last Task created
    # def before_save(self):
        # task = frappe.get_last_doc('student')
        # frappe.msgprint(f"Latest Task: {task.name}")
        
        # student=frappe.get_doc('student',"siva")
        # frappe.msgprint(f"Age of siva: {student.age}")
                
        # doc = frappe.new_doc('demofeild')
        # doc.data_hkmr="gokul"
        # doc.insert()
        
        # frappe.delete_doc('demofeild','Demo-002')
        # frappe.rename_doc('demofeild', 'Demo-001', 'Demo-0001')
        pass
        
        
        
        
        
        
        
    
    
@frappe.whitelist()
def name(f_name,l_name):
    full_name=f_name+l_name
    return full_name

 

@frappe.whitelist()
def create_student_record(student_name, email, age, address=None):
    student = frappe.get_doc({
        "doctype": "student",
        "student_name": student_name,
        "email": email,
        "age": age,
        "address": address
    })
    student.insert()
    frappe.db.commit()
    return student.name
