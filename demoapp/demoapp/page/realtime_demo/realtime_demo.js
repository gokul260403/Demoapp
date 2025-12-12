frappe.pages['realtime_demo'].on_page_load = function(wrapper) {
 
    let page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Realtime Demo Chart',
        single_column: true
    });

  
    let chart_container = $('<div id="realtime-chart" style="height:300px; margin-top:20px;"></div>');
    $(page.main).append(chart_container);
 
    const data = {
        datasets: [
            { name: "Random Data", values: [] }
        ]
    };
 
    let chart = new frappe.ui.RealtimeChart("#realtime-chart", "demo_event", 10, {
        title: "Live Random Data",
        data: data,
        type: "line",
        height: 300,
        colors: ["#7cd6fd"]
    });

     
    chart.start_updating();
	chart.stop_updating();
};
