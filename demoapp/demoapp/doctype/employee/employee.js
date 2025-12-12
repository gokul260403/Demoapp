// Copyright (c) 2025, gokul and contributors
// For license information, please see license.txt

frappe.ui.form.on("Employee", {
    refresh(frm) {
        let wrapper = frm.fields_dict.email?.$wrapper;
        // wrapper.empty();
        let control = frappe.ui.form.make_control({
            parent: wrapper ,
            df: {
                label: 'Mail(form control)',
                fieldname: 'mail',
                fieldtype: 'Data'
            },
            render_input: true
        })
        control.set_value(frm.doc.email )
    },

});

    // frappe.meta.docfield_map['DocField'].fieldtype.formatter = (value) => {
    //  if (value === 'Data') {
    //     return `<div style="background-color:black;color:white;">Data</div>`;
    // } else {
    //     return value;
    // }
    // };


// frappe.meta.docfield_map['DocField'].fieldtype.formatter = (value) => {
//  if (value==='Section Break') return '🔵 Section Break';
//  else return value;
// }


