# Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

# import frappe
from frappe import _


def execute(filters=None):
	"""Return columns and data for the report.

	This is the main entry point for the report. It accep			ts the filters as a
	dictionary and should return columns and data. It is called by the framework
	every time the report is refreshed or a filter is updated.
	"""
	columns = get_columns()
	data = get_data()

	return columns, data


def get_columns():
	"""Return columns for the report.

	One field definition per column, just like a DocType field definition.
	"""
	return [
		{
			"label": _("student Name"),
			"fieldname": "student_name",
			"fieldtype": "Data",
		},
		 
	]


def get_data():
	"""Return data for the report.

	The report data is a list of rows, with each row being a list of cell values.
	"""
	return [
		["Row 1", 1],
		["Row 2", 2],
	]
