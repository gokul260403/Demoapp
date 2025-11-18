frappe.pages['demo-page'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Mypage',
		single_column: true
	});
     page.add_action_icon("refresh", () => {
        frappe.msgprint("Page refreshed!");
    });
	page.set_title('My Page')
	// page.set_title_sub('Subtitle')     //not working
    page.set_indicator('Pending', 'orange')
	// page.clear_indicator()
	// let $btn = page.set_primary_action('New', () => create_new(), 'octicon octicon-plus')  //not working
	// page.clear_primary_action()
	// let $btn = page.set_secondary_action('Refresh', () => refresh(), 'octicon octicon-sync')
    // page.clear_secondary_action()
// add a normal menu item
	// page.add_menu_item('Send Email', () => open_email_dialog())       //not working                 

// add a standard menu item
	// page.add_menu_item('Send Email', () => open_email_dialog(), true)   //not working
	// page.clear_menu()
	// add a normal menu item
// page.add_action_item('Delete', () => delete_items())
// page.clear_actions_menu()


// add a normal inner button
// page.add_inner_button('Update Posts', () => update_posts())
// add a dropdown button in a group
// page.add_inner_button('New Post', () => new_post(), 'Make')


// // change type of ungrouped button
// page.change_inner_button_type('Update Posts', null, 'primary');

// // change type of a button in a group
// page.change_inner_button_type('Delete Posts', 'Actions', 'danger');


// // remove inner button
// page.remove_inner_button('Update Posts')

// // remove dropdown button in a group
// page.remove_inner_button('New Posts', 'Make')

// page.clear_inner_toolbar()


// let field = page.add_field({
//     label: 'Status',
//     fieldtype: 'Select',
//     fieldname: 'status',
//     options: [
//         'Open',
//         'Closed',
//         'Cancelled'
//     ],
//     change() {
//         console.log(field.get_value());
//     }
// });




// let values = page.get_form_values()
 
// page.clear_fields()




$(`
        <h3>Custom Desk Page</h3>
        <p>Loaded using the Page API.</p>
    `).appendTo(page.body);





  
    const $content = $(`
        <div class="dashboard-wrapper" style="padding: 20px;">
            <div class="row">
                <div class="col-sm-4">
                    <div class="card shadow-sm bg-secondary text-center p-3">
                        <h4>Total Customers</h4>
                        <h2 id="total_customers">--</h2>
                    </div>
                </div>
                <div class="col-sm-4">
                    <div class="card shadow-sm text-center p-3">
                        <h4>Total Sales</h4>
                        <h2 id="total_sales">--</h2>
                    </div>
                </div>
                <div class="col-sm-4">
                    <div class="card shadow-sm text-center p-3">
                        <h4>Pending Invoices</h4>
                        <h2 id="pending_invoices">--</h2>
                    </div>
                </div>
            </div>
        </div>
    `);

    $content.appendTo(page.body);



	page.set_primary_action('Sample', () => {
        frappe.set_route('sample');  // 👈 navigate to another page
    });
	// page.set_secondary_action('Sample', () => {
    //     frappe.set_route('sample');  // 👈 navigate to another page
    // });

     
    // load_dashboard_data();
};
 
// function load_dashboard_data() {
    
//     const stats = {
//         total_customers: 152,
//         total_sales: 87400,
//         pending_invoices: 9
//     };

//     // Update dashboard values
//     $('#total_customers').text(stats.total_customers);
//     $('#total_sales').text('₹' + stats.total_sales.toLocaleString());
//     $('#pending_invoices').text(stats.pending_invoices);
// }