frappe.listview_settings['Employee'] = {
    
    // onload:function(listview) {
    //     listview.page.add_inner_button("Action", () => {
    //         frappe.msgprint("Custom action triggered!");
    //     });
         
    // },
    add_fields:["email","role"],
    filters: [
        ["role", "=", "SE"]
    ],
   
    
    onload(listview) {
        listview.page.add_inner_button(__('SE'), function() {
            listview.filter_area.clear();
            listview.filter_area.add([["Employee", "role", "=", "SE"]]);
        });
        listview.page.add_inner_button(__('Low Leave'), function() {
            listview.filter_area.clear();
            listview.filter_area.add([["Employee", "remaining_leave", "<", 4]]);
        });
    },

    formatters: {
        role(val) {

            if (val === "SE") {
                return `<span style="color: green; font-weight: bold;">${val}</span>`;
            }

            if (val === "HR") {
                return `<span style="color: blue; font-weight: bold;">${val}</span>`;
            }

            return val;  
        },
        remaining_leave(val){
            if(val<4){
                return `<span style="color: red; font-weight: bold;">${val}</span>`;
            }
            else{
                return `<span style="color: black; font-weight: bold;">${val}</span>`;
            }
        }
          
       
    }
};
