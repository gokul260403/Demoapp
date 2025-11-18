 frappe.ui.form.on('Progress Bar', {
    refresh: function(frm) {
        frm.trigger('update_progress_bar');
    },
    
    custom_progress: function(frm) {
        frm.trigger('update_progress_bar');
    },
    update_progress_bar: function(frm) {
        const progress_val = frm.doc.custom_progress || 0;
        const progress_html = `
            <div style="background-color: #e0e0e0; border-radius: 5px;">
                <div style="width: ${progress_val}%; background-color: #2196f3; padding: 5px 0; color: white; text-align: center; border-radius: 5px;">
                    ${progress_val}%
                </div>
            </div>
        `;
        frm.set_df_property('custom_progress_bar_html', 'options', progress_html);
    }
});
