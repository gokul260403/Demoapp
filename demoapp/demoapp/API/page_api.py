import frappe
import json
import requests

@frappe.whitelist()
def get_records(doctype, filters=None, page=1, page_size=10):
    try:
        if filters:
            filters = json.loads(filters)
        else:
            filters = {}

        page = int(page)
        page_size = int(page_size)
        offset = (page - 1) * page_size

        
        total_records = frappe.db.count(doctype, filters)
 
        records = frappe.get_all(
            doctype,
            filters=filters,
            fields=["*"],  
            limit_start=offset,
            limit_page_length=page_size,
            order_by="creation desc"
        )

        return {
            "page": page,
            "page_size": page_size,
            "total_records": total_records,
            "total_pages": (total_records + page_size - 1) // page_size,
            "data": records
        }

    except Exception as e:
        frappe.log_error(title="Pagination Error", message=frappe.get_traceback())
        frappe.throw(str(e))


@frappe.whitelist()
def fetch_external_data():
    url = "http://127.0.0.1:8000/api/method/demoapp.demoapp.doctype.employee.employee.read_employee"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        frappe.msgprint(f"Fetched {len(data)} records")
        return data
    else:
        frappe.throw(f"Failed to fetch data: {response.status_code}")


# import frappe, requests

# @frappe.whitelist()
# def fetch_external_data():
#     base_url = frappe.utils.get_url()  # gets the current site's URL, e.g. "http://demosite.localhost:8000"
#     url = f"{base_url}/api/method/demoapp.demoapp.doctype.employee.employee.read_employee"
    
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json().get("message", [])
#         frappe.msgprint(f"Fetched {len(data)} records from {url}")
#         return data
#     else:
#         frappe.throw(f"Failed to fetch data: {response.status_code}")
