// Copyright (c) 2025, gokul and contributors
// For license information, please see license.txt

frappe.ui.form.on("Leave Application", {
    to_date(frm) {
        Leave_calculation(frm)
        
    },
    from_date(frm){
        Leave_calculation(frm)

    }
});

function Leave_calculation(frm){
    if (frm.doc.from_date && frm.doc.to_date){
           frappe.call({
            method: "demoapp.demoapp.doctype.leave_application.leave_application.date",   
            args: {
                from_date: frm.doc.from_date,
                to_date: frm.doc.to_date,
            },
            callback: function (r) {
                if (r.message) {
                    frm.set_value("leave_days", r.message);
                    if (r.message>frm.doc.remaining_leave){
                        frappe.msgprint("Invalid date: you have only "+ frm.doc.remaining_leave +" days leave")
                        frm.set_value("to_date",null)
                        //frm.refresh_field()
                    }
                }
            }
        });

        // frappe.call({
        //         method: "demoapp.demoapp.doctype.leave_application.leave_application.calculate_sundays",   
        //         args: {
        //             from_date: frm.doc.from_date,
        //             to_date: frm.doc.to_date,
        //         },
        //         callback: function (r) {
        //             if (r.message) {
        //                  var sundays = r.message;
        //                  var excluding_sundays=frm.doc.leave_days-sundays;
        //                  frm.set_value("excluding_sundays",excluding_sundays);
        //                 }
        //             }
        //         }
        //     });

    }
}

