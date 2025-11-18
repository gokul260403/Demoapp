  # Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today,days_diff,getdate,add_days


class LeaveApplication(Document):
	# def validate(self):
	# 	current_date=today()
	# 	if self.from_date < current_date:
	# 		frappe.throw("Invalid Date: The 'From Date' cannot be in the past.")
	# 	elif self.to_date < self.from_date :
	# 		frappe.throw("Invalid Date: The 'To Date' cannot be before 'From Date'.")    ##it causes the date +str error "<" not supported bw str and int

	def validate(self):
		current_date = getdate(today())   
		from_date = getdate(self.from_date)
		to_date = getdate(self.to_date)

		if from_date < current_date:
			frappe.throw("Invalid Date: The 'From Date' cannot be in the past.")
		elif to_date < from_date:
			frappe.throw("Invalid Date: The 'To Date' cannot be before 'From Date'.")

	def on_submit(self):
		total_leave = frappe.db.get_single_value('Leave Settings', 'total_leave')
		employee=frappe.get_doc("Employee",self.emp_name)
		from_date = getdate(self.from_date)
		to_date = getdate(self.to_date)
		leave_days=days_diff(to_date,from_date)+1
  
		if employee.used_leave>=total_leave:
			frappe.throw(f'There is no available leave for {employee.employee_name}')
        
			
		if self.status=="approved": 
			employee.used_leave = employee.used_leave+leave_days
			employee.remaining_leave=total_leave - employee.used_leave
			employee.save()
			frappe.msgprint("leave_days:"+str(leave_days))

		

@frappe.whitelist()
def date(from_date,to_date):
	if to_date:
		days=days_diff(to_date, from_date)+1
		return days



@frappe.whitelist()
def calculate_sundays(from_date, to_date):
    # if not from_date or not to_date:
    #     return 0
    from_date = getdate(from_date)
    to_date = getdate(to_date)

    total_days = days_diff(to_date, from_date) + 1
    sunday_count = 0

     
    for i in range(total_days):
        current_date = add_days(from_date, i)
        if current_date.weekday() == 6:  
            sunday_count += 1

    return sunday_count
