frappe.show_alert({
    message:__('Hi, you have a new message'),
    indicator:'green'
}, 5);

 
frappe.ui.form.on('sample', {
    refresh: function(frm) {
     
        frm.add_custom_button(__('Scan QR Code'), function() {
            new frappe.ui.Scanner({
                dialog: true,      
                multiple: false,    
                on_scan(data) {
                    console.log('Scanned value:', data.decodedText);
                    // frm.set_value('name1', data.decodedText);
                    // frm.save();
                }
            });
        });
    }
});
