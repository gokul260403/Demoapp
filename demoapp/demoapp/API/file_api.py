import frappe
from frappe import _
import json
 
@frappe.whitelist()
def upload_file():
    
    if 'file' not in frappe.request.files:
        frappe.throw(_("No file part found in request"))

    file = frappe.request.files['file']
    filename = file.filename
    folder = frappe.request.form.get('folder') or 'Home'
 
    _file = frappe.get_doc({
        "doctype": "File",
        "file_name": filename,
        "attached_to_doctype": None,
        "attached_to_name": None,
        "is_private": 0,
        "content": file.read(),
        "folder": folder
    })
    _file.save()
    frappe.db.commit()

    return {"message": "File uploaded successfully", "file_url": _file.file_url, "name": _file.name}

 
@frappe.whitelist()
def get_file(name=None):
    if name:
        file_doc=frappe.get_doc("File",name)
        return{
             "file_name": file_doc.file_name,
             "file_url": file_doc.file_url,
             "is_private": file_doc.is_private
        }
    else:
        file_doc = frappe.get_all("File")
        return { "file":file_doc}

 
@frappe.whitelist()
def update_file(name, new_file_name=None, is_private=None):
    
    file_doc = frappe.get_doc("File", name)

    if new_file_name:
        file_doc.file_name = new_file_name
    if is_private is not None:
        file_doc.is_private = int(is_private)

    file_doc.save()
    frappe.db.commit()

    return {"message": "File updated successfully", "name": file_doc.name}

 
@frappe.whitelist()
def delete_file(name):
    
    frappe.delete_doc("File", name,)
    frappe.db.commit()
    return {"message": f"File '{name}' deleted successfully"}



# def save(doc, method):
#     frappe.msgprint(f"Todo DocEvent Testing Doc Name: {doc.name}")
 






 

 
@frappe.whitelist()
def bulk_create_records(doctype, records):
    try:
        records = json.loads(records)
        created = []
        for rec in records:
            doc = frappe.get_doc({ "doctype": doctype, **rec })
            doc.insert()
            created.append(doc.name)

        frappe.db.commit()
        return {"message": "Bulk records created successfully", "names": created}
    except Exception as e:
        frappe.log_error(title="Bulk Create Error", message=frappe.get_traceback())
        frappe.db.rollback()
        frappe.throw(str(e))
        
@frappe.whitelist()
def bulk_update_records(doctype, records):
    try:
        records = json.loads(records)
        updated = []
        for rec in records:
            name = rec.pop("name", None)
            if not name:
                continue
            doc = frappe.get_doc(doctype, name)
            doc.update(rec)
            doc.save()
            updated.append(name)
        frappe.db.commit()
        return {"message": "Bulk records updated successfully", "names": updated}
    except Exception as e:
        frappe.log_error(title="Bulk Update Error", message=frappe.get_traceback())
        frappe.db.rollback()
        frappe.throw(str(e))

@frappe.whitelist()
def bulk_delete_records(doctype, names):
    try:
        names = json.loads(names)
        deleted = []
        for name in names:
            frappe.delete_doc(doctype, name)
            deleted.append(name)
        frappe.db.commit()
        return {"message": "Bulk records deleted successfully", "names": deleted}
    except Exception as e:
        frappe.log_error(title="Bulk Delete Error", message=frappe.get_traceback())
        frappe.db.rollback()
        frappe.throw(str(e))
