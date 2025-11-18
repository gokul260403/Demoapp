# # Copyright (c) 2025, gokul and Contributors
# # See license.txt

# import frappe,random
# from frappe.tests import IntegrationTestCase


# # On IntegrationTestCase, the doctype test records and all
# # link-field test record dependencies are recursively loaded
# # Use these module variables to add/remove to/from that list
# EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
# IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



# class IntegrationTestLeaveApplication(IntegrationTestCase):
# 	"""
# 	Integration tests for LeaveApplication.
# 	Use this class for testing interactions between multiple components.
# 	"""

# 	def setUp(self):
# 		random_suffix = random.randint(1000, 9999)
# 		self.employee = frappe.get_doc({
# 			"doctype": "Employee",
# 			"employee_name": f"harish_{random_suffix}",
# 			"role": "HR",
# 			"email": f"harish_{random_suffix}@gmail.com",
# 		}).insert()

# 		self.leave_application =frappe.get_doc({
# 			"doctype":"Leave Application",
# 			"emp_name":self.employee.name,
# 			"role":"HR",
# 			"from_date": "2025-10-27",
# 			"to_date": "2025-10-28",
# 			"description": "Test leave for integration case",
# 			"status": "applied"
# 		}).insert()


# 	def test_leave_linked_to_employee(self):
			
# 		leave = frappe.get_doc("Leave Application", self.leave_application.name)
# 		self.assertEqual(leave.emp_name, self.employee.name)
# 		# self.assertEqual(self.leave_application.status,"Pending")
# 		# self.assertEqual(self.leave_application.role,"SE")

		
# 	def test_employee_created(self):
		
# 		exists = frappe.db.exists("Employee", self.employee.name)
# 		self.assertTrue(exists)
    
# 	def tearDown(self):
# 		frappe.delete_doc("Employee", self.employee.name)
# 		frappe.delete_doc("Leave Application",self.leave_application.name)
 
import frappe, random
from frappe.tests import IntegrationTestCase
       
# IGNORE_TEST_RECORD_DEPENDENCIES = ["*"] 
class IntegrationTestLeaveApplication(IntegrationTestCase):
    """Integration tests for Leave Application"""

    doctype = "Leave Application"
   
    def setUp(self):
        frappe.flags.in_test = True
        frappe.flags.disable_email_sending = True
        frappe.flags.disable_pdf_generation = True
        random_suffix = random.randint(1000, 9999)

        self.employee = frappe.get_doc({
            "doctype": "Employee",
            "employee_name": f"harish_{random_suffix}",
            "role": "HR",
            "email": f"harish_{random_suffix}@gmail.com",
        }).insert(ignore_permissions=True)

        self.leave_application = frappe.get_doc({
            "doctype": "Leave Application",
            "emp_name": self.employee.name,
            "role": "HR",
            "from_date": "2025-10-27",
            "to_date": "2025-10-28",
            "description": "Test leave for integration case",
            "status": "applied"
        }).insert(ignore_permissions=True)
    
    def test_leave_linked_to_employee(self):
        leave = frappe.get_doc("Leave Application", self.leave_application.name)
        self.assertEqual(leave.emp_name, self.employee.name)

    def test_employee_created(self):
        exists = frappe.db.exists("Employee", self.employee.name)
        self.assertTrue(exists)

    def tearDown(self):
        frappe.delete_doc("Leave Application", self.leave_application.name, force=1)
        frappe.delete_doc("Employee", self.employee.name, force=1)
