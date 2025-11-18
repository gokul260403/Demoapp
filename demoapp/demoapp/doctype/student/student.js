// Copyright (c) 2025, gokul and contributors
// For license information, please see license.txt

frappe.ui.form.on("student", {
refresh(frm){
    frappe.call({
    method:"demoapp.demoapp.doctype.student.student.name",
    args:{
        f_name:frm.doc.student_name,
        l_name:frm.doc.email,
    },
    callback: function(r){
        if(r.message){
            frappe.msgprint("full_name :"+r.message)
        }
    }

})
}

});
