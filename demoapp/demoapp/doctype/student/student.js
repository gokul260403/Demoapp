// Copyright (c) 2025, gokul and contributors
// For license information, please see license.txt

frappe.ui.form.on("student", {

   
refresh(frm){

    let is_allowed = frappe.user_roles.includes('System Manager');
    frm.toggle_enable(['age',"naming_series"], is_allowed);
   


    //a custom button to get the selected row of child table
//     frm.add_custom_button('get child',()=>{
//         let selected = frm.get_selected()
// console.log(selected)
//     })
    
     //adding a row to child while refreshing
    // let row = frm.add_child('marksheet', {
    // subject: 'subj',
    // score: 24
    // });
    // frm.refresh_field('marksheet');


    //adding a row to child table by custom button
    //  frm.add_custom_button('Add Marks', () => {
    //         let row = frm.add_child('marksheet', {
    //             subject: 'subj',
    //             score: 24
    //         });
    //         frm.refresh_field('marksheet');
    //     });


    // set address as mandatory while age is equal to 18
    // frm.toggle_reqd('address', frm.doc.age === 18);
   


    //only display address while age is eqaul to 18
    // frm.toggle_display('address', frm.doc.age === 18);


    // frm.add_custom_button('Open another form', () => {
    // frappe.set_route('Form', 'student', 'raju006');
    // })


    // if (!frm.doc.email) {
    // frm.set_intro('Please set the value of email' );
    // }
    
    //custom button is only show after the form is saved
    // if (!frm.is_new()) {
    // frm.add_custom_button('Click me', () => console.log('Clicked custom button'))
    // }


    //email dialog box
    // frm.email_doc();
    // frm.email_doc(`Hello ${frm.doc.student_name}`);

     //to disable save button based on role
    // if (frappe.user_roles.includes('Administrator')) {
    // frm.enable_save();
    // } else {
    // frm.disable_save();
    // }

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





  
 
        frm.add_custom_button('Add Student', function() {

       
            let dialog = new frappe.ui.Dialog({
                title: 'Add Student',
                fields: []   
            });

        
            let controls = {};
            ["student_name","email","age","address"].forEach(field => {
                controls[field] = new frappe.ui.form.make_control({
                    parent: dialog.body,
                    df: {
                        fieldname: field,
                        label: field.replace("_"," ").toUpperCase(),
                        fieldtype: field === "age" ? "Int" : "Data"
                    },
                    render_input: true
                });
                controls[field].make_input();
            });

          
            dialog.set_primary_action('Submit', function() {
                let data = {};
                Object.keys(controls).forEach(k => data[k] = controls[k].get_value());

                frappe.call({
                    method: "demoapp.demoapp.doctype.student.student.create_student_record",
                    args: data,
                    callback: function(r) {
                        frappe.msgprint("Student created: " + r.message);
                        dialog.hide();
                    }
                });
            });

            dialog.show();
        });
 











    }
});

 