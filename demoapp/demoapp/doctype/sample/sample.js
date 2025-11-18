// Copyright (c) 2025, gokul and contributors
// For license information, please see license.txt

// frappe.ui.form.on("sample", {
// 	refresh(frm) {

        //get_route()
        // frappe.msgprint("Route:"+frappe.get_route());

        //set_route()
        // frm.add_custom_button("Student",function(){
        //     // frappe.set_route('List', 'student');
        //     // frappe.set_route(['List', 'student']);
        //     //frappe.set_route('List/student');
        //     //frappe.set_route("List", "student", { select_dept: "MCA" });
        // });
      

        //format()
        // let total_salary = 55000;
        // let formatted_salary = frappe.format(total_salary,{fieldtype: "Currency"} );
        // frappe.msgprint(`Total Salary: ${formatted_salary}`);
  
        //provide()


    //     frappe.require([
    //     "/assets/demoapp/js/library1.js",
    //     "/assets/demoapp/js/library2.js" ], function() {
    //     frappe.msgprint("Both libraries loaded!");
    // });

    //     frappe.require("/assets/demoapp/js/custom_chart.js", function() {
    //         frappe.msgprint("Custom JS loaded successfully!");
    //         create_chart();
    //     });


//    //server call AJAx
//     frappe.db.get_value('Employee','emp-008','role').then(r => {
//         frappe.msgprint(r.message.role)
//     })   
// 	},
// });






//  frappe.ui.form.on("sample", {
//     refresh(frm) {

//         const dialog = new frappe.ui.Dialog({
//             title: __("Create Logs"),
//             fields: [
//                 {
//                     fieldname: "logs",
//                     fieldtype: "Table",
//                     label: __("Logs"),
//                     in_place_edit: true,
//                     reqd: 1,
//                     fields: [
//                         {
//                             fieldname: "log_type",
//                             label: __("Log Type"),
//                             fieldtype: "Select",
//                             options: "IN\nOUT",
//                             in_list_view: 1,
//                             reqd: 1,
//                         },
//                         {
//                             fieldname: "time",
//                             label: __("Time"),
//                             fieldtype: "Time",
//                             in_list_view: 1,
//                             reqd: 1,
//                         }
//                     ],
//                     on_add_row: (idx) => {
//                         let data_id = idx - 1;
//                         let logs = dialog.fields_dict.logs;
//                         let log_type = (data_id % 2 === 0) ? "IN" : "OUT";
//                         logs.df.data[data_id].log_type = log_type;
//                         logs.grid.refresh();
//                     },
//                 },
//             ],
//             primary_action(values) {
//                 //  Clear existing child table
//                 frm.clear_table("logs");

//                 // Safely iterate through each row
//                 (values.logs || []).forEach(row => {
//                     // Handle both "row.log_type" and "row.doc.log_type" structures
//                     let log_type = row.log_type || (row.doc && row.doc.log_type);
//                     let time = row.time || (row.doc && row.doc.time);

//                     let child = frm.add_child("logs");
//                     child.log_type = log_type;
//                     child.time = time;
//                 });

//                 frm.refresh_field("logs");
//                 dialog.hide();
//                 frappe.msgprint(` ${values.logs.length} log(s) added successfully.`);
//             },
//             primary_action_label: __("Add Logs"),
//         });

//         frm.add_custom_button("Open Log Dialog", () => {
//             dialog.show();
//         });
//     },
// });



//Form Control (make_control)

// frappe.ui.form.on("sample", {
//     refresh(frm) {
         
//         let $wrapper = $('<div></div>')
//             .appendTo(frm.fields_dict.custom_html.wrapper);

         
//         let control = frappe.ui.form.make_control({
//             df: {
//                 fieldname: 'demo_field',
//                 label: 'Enter Demo Text',
//                 fieldtype: 'Data',
//                 placeholder: 'Type here...'
//             },
//             parent: $wrapper,
//             render_input: true
//         });

       
//         control.set_value("Book");
 
//         control.$input.on('change', function() {
//             frappe.msgprint(`You typed: ${control.get_value()}`);
//         });
//     }
// });

