// Copyright (c) 2025, gokul and contributors
// For license information, please see license.txt

frappe.ui.form.on("sample", {
    before_save: function(frm) {
        frappe.utils.play_sound("ping");
    },
	refresh(frm) {
        frappe.realtime.on("test_event", (data) => {
        alert(data.text);
        });
        // frappe.realtime.off('test_event');


        frappe.realtime.on("doctype_update", (d) => console.log("Update:", d));


        //get_route()
        // frappe.msgprint("Route:"+frappe.get_route());

        //set_route()
        // frm.add_custom_button("Student",function(){
        //     // frappe.set_route('List', 'student');
        //     // frappe.set_route(['List', 'student']);
        //     // frappe.set_route('List/student');
        //     // frappe.set_route("List", "student", { select_dept: "MCA" });
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

        // frappe.require("/assets/demoapp/js/custom_chart.js", function() {
        //     frappe.msgprint("Custom JS loaded successfully!");
        //     create_chart();
        // });


   //server call AJAx
    // frappe.db.get_value('Employee','emp-001','role').then(r => {
    //     frappe.msgprint(r.message.role)
    // })   

    // frappe.db.get_doc("Employee",'emp-001').then(r =>{
    //     frappe.msgprint(r.role)
    // })

    // frappe.db.get_list("Employee",{
    //     fields:["employee_name"],filters:{role:"SE"}
    // }).then(r=>{
    //     console.log(r);
    // })
    // frappe.db.set_value('Employee','emp-001','role','HR').then(r=>{
    //     console.log(r.message);
    // })

    // frappe.db.set_value('Employee','emp-001','role','SE').then(r=>{
    //     console.log(r.message);
    // })

    // frappe.db.insert({doctype:"Employee",employee_name:"sam"}).then(r=>{
    //     console.log(r)
    // })

    // frappe.db.insert({doctype:"Employee",employee_name:"samraj"}).then(r=>{
    //     console.log(r)
    // })

    //  frappe.db.count("Employee",{role:"SE"}).then(r=>{
    //     console.log(r)
    //  })

    //    frappe.db.delete_doc("Employee",'emp-004').then(r=>{
    //     console.log(r.message)
    //    });

       
    //    frappe.db.exists("Employee","emp-004").then(exists=>{
    //     console.log(exists)
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








// frappe.ui.form.on("sample", {
//     refresh(frm) {
//         frappe.msgprint({
//     title: __('Notification'),
//     indicator: 'green',
//     message: __('refresh')
// });
    

// frappe.throw(__('This is an Error Message'))

// frappe.prompt('First Name', ({ value }) => console.log(value))

// frappe.prompt({
//     label: 'Birth Date',
//     fieldname: 'date',
//     fieldtype: 'Date'
// }, (values) => {
//     console.log(values.date);
// })
   
// frappe.show_alert({
//     message:__('Hi, you have a new message'),
//     indicator:'green'
// }, 5);





// frappe.confirm('Are you sure you want to proceed?',
//     () => {
       
// frappe.show_alert({
//     message:__('Hi, you have a new message'),
//     indicator:'green'
// }, 5);
//     }, () => {
//           console.log("No")
//     })

// frappe.warn('Are you sure you want to proceed?',
//     'There are unsaved changes on this page',
//     () => {
//          console.log("yes")    
//     },
//     'Continue',
//     true 
// )

// frappe.show_progress('Loading..', 70, 100, 'Please wait');



// MultiSelectDialog
    // frm.add_custom_button("Select Leave Applications", () => {
    //         new frappe.ui.form.MultiSelectDialog({
    //             doctype: "Leave Application",
    //             target: frm,
    //             setters: {
    //                 emp_name: null,
    //                 status: "approved"
    //             },
    //             add_filters_group: 1,
    //             date_field: "from_date",

    //             get_query() {
    //                 return {
    //                     filters: {
    //                         docstatus: ["!=", 2]
    //                     }
    //                 };
    //             },

    //             action(selections) {
    //                 frappe.msgprint("Selected:<br>" + selections.join("<br>"));
    //                 console.log(selections);
    //             }
    //         });
    // });

// scanner api
    // frm.add_custom_button("scanner",() => {
    //     new frappe.ui.Scanner({
    //         dialog:true,
    //         multiple:true,
    //         on_scan(data) {
    //         handle_scanned_barcode(data.decodedText); //use console.log(data.decodedText)
    //         }
    //     })
    // })


    },
});
 
