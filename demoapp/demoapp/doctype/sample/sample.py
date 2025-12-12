# Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now ,getdate,today,add_to_date,date_diff,days_diff,random_string,unique,get_abbr,validate_url,validate_phone_number
from frappe.utils import month_diff,pretty_date,format_duration,comma_and,money_in_words,validate_json_string,validate_email_address
from frappe.utils.pdf import get_pdf

class sample(Document):
    def before_save(self):
        ####Dialog API######
        # frappe.msgprint(msg='Dialog testing', title='sample message')
        
        # frappe.throw(title="error",msg="dialog error message")
        
        
        #####realtime############
        # frappe.publish_progress(25,"progress bar",description='progress bar............')
        
        # frappe.publish_progress(50,'progress bar',description='progress bar........')
        
        # frappe.publish_realtime("test_event", {"text": "Hello World!"})
        
        ###########utility api ###########
        # frappe.msgprint(now())
        
        # date=getdate()
        # frappe.msgprint(str(date))
        
        # frappe.msgprint("today:"+today())
        
        # frappe.msgprint(add_to_date(today(), months=2))
        
    #    date_1 = today()
    #    date_2 = add_to_date(date_1, days=10)
    #    frappe.msgprint(str(date_diff(date_2, date_1)))
    
    
    #    date_1 = today()
    #    date_2 = add_to_date(date_1, days=10)
    #    frappe.msgprint("days:"+str(days_diff(date_2, date_1)))
    
    
    #    date_1 = today()
    #    date_2 = add_to_date(date_1, days=85)
    #    frappe.msgprint(str(month_diff(date_2, date_1)))
    
    #  frappe.msgprint(pretty_date(now()))
    
        #  frappe.msgprint(format_duration(1000000,hide_days=True))
        
        # frappe.msgprint(comma_and([1,2,3],add_quotes=False))
        # frappe.msgprint(comma_and('abcd'))
        
        # frappe.msgprint(money_in_words(800,'USD'))
        
        # frappe.msgprint(random_string(10))
        
        #not working.....................
        # frappe.msgprint(mask_string("152153521"))
        #not working.....................
        
        # frappe.msgprint(str(unique([1, 2, 3, 1, 1, 1])))
        # frappe.msgprint(str(unique('abcda')))
        # frappe.msgprint(str(unique(('Apple', 'Apple', 'Banana', 'Apple'))))
       
       
       
    #    frappe.msgprint(get_abbr('gokul raj'))
    
        #   frappe.msgprint(str(validate_url('google')))
        #   frappe.msgprint(str(validate_url('https://google.com')))
    
        # frappe.msgprint(validate_email_address('other text, rushabh@erpnext.com, some other text'))
        
        
        # frappe.msgprint(str(validate_phone_number('753858375')))
        
        # validate_json_string('[]')
        # validate_json_string('[{}]')
        # validate_json_string('[{"player": "one", "score": 199}]')

        # try:
        #     # Throws frappe.ValidationError
        #     validate_json_string('invalid json')
        # except frappe.ValidationError:
        #     print('Not a valid JSON string')
        
        ############3#document api####################
        
        # doc=frappe.get_doc("student","raju006")
        # doc.address="mkm"
        # doc.save()
        
        # doc=frappe.get_last_doc("student")
        # frappe.msgprint("last docname:"+doc.name)
        
        # doc=frappe.get_cached_doc("sample")
        # frappe.msgprint("cached docname:"+doc.name)
            
        # doc=frappe.new_doc("student")
        # doc.student_name="Hari"
        # doc.insert()
        
        # frappe.delete_doc("student","arif007")
         
        # frappe.rename_doc("student","c65276bb","sam")
        
        # meta=frappe.get_meta("student")
        # frappe.msgprint(str(meta.has_field('status')))
        
        
        #only used in that current doctype
        # old = self.get_doc_before_save()
        # if old and old.select != self.select:
        #    frappe.msgprint("value changed")
        
        
        # old = self.has_value_changed("select")
        # if old :
        #    frappe.msgprint("value changed")
        
        # doc=frappe.get_doc("student","raju006")
        # print(doc.check_permission(permtype='write'))
        
        # doc=frappe.get_doc("student","sam")
        # title=doc.get_title()
        # frappe.msgprint("title:"+title)
        
        
        # doc=frappe.get_doc("student","raju006")
        # doc.address="mkkmm"
        # doc.save()
        # doc.notify_update()
        
        
        #####doc.db_set()####
        # doc=frappe.get_doc("student","raju006")
        # doc.db_set('address', "CGL")
    
        # doc=frappe.get_doc("student","raju006")
        # url=doc.get_url()
        # frappe.msgprint(url)
        
        # doc=frappe.get_doc("student","raju006")
        # doc.add_comment('Comment', text='Test Comment')
        # doc.save()
        
        # doc=frappe.get_doc("student","raju006")
        # doc.add_comment('Edit', 'Values changed')
        # doc.save()
        
        
        # doc=frappe.get_doc("student","raju006")
        # frappe.msgprint(str(doc.get_tags()))
         
        # doc=frappe.get_doc("student","raju006")
        # doc.add_tag('raju')
        # doc.save()
        
        
        
        ##############not working ########################
        # doc = frappe.get_last_doc("student")
        # doc.last_active = now()
        # doc.db_update()

        # doc=frappe.get_doc("student","raju006")
        # for child_doc in doc.get_children():
        #     print(child_doc.name)
            
        # doc=frappe.get_doc("student","raju006")
        # doc.add_viewed()
        # doc.save()

        # doc=frappe.get_doc("student","raju006")
        # doc.add_seen()
        # doc.save()
        
        # doc=frappe.get_doc("student","raju006")
        # doc.append("marksheet",{
        #     "subject":"computer",
        #     "score":98
        # })
        # doc.save()
        #############not working##########################
        
        ########database API########
        # students=frappe.db.get_list('student',filters={'address':'mkm'},pluck='name',)
        # print(students)
        
        # students=frappe.db.get_list('student',fields=['count(name) as count','address'],group_by='address')
        # print(students)
        
        # students=frappe.db.get_all('student',pluck='name')
        # print(students)
        
        # students=frappe.db.get_all('student',filters={'address':'mkm'},pluck='name',)
        # print(students)
        
        # student_address=frappe.db.get_value("student","raju006","address")
        # print(student_address)
        
          
        # student_address,mail=frappe.db.get_value("student","raju006",['address','email'])
        # print(student_address , mail)
        
        # student_dict=frappe.db.get_value("student","raju006",['address','email'],as_dict=1)
        # print(student_dict)
        
        # total_leave=frappe.db.get_single_value("Leave Settings","total_leave")
        # print("Total leave from Leave settings:",total_leave)
        
        # frappe.db.set_value("student",'raju006',"address",'CGL')
        
        # exists=frappe.db.exists("student",{'student_name':'raju','address':'CGL'})
        # print("exists:",exists)
        
        # count= frappe.db.count('student')
        # print(count)
        
        # count=frappe.db.count("student",{"address":"mkm"})
        # print(count)
        
        
        # frappe.db.delete("student",'ca5528af')
        
        # frappe.db.truncate("Error Log")
        
        # save_point=frappe.db.savepoint("address_savepoint")
        # frappe.db.set_value("student",'raju006',"address",'temp')
        # frappe.db.rollback()
        
        # frappe.db.rename_table("flow", "Flow")
        # frappe.db.rename_table("Flow", "flow")
        
        # print(frappe.db.describe("student"))
        
        # frappe.db.add_unique("student",["address","email"])
        
        
        pass
        
        
        
        # frappe.db.change_column_type('student',"address", "Text")
        
        
        
@frappe.whitelist()  ##created for actions in sample doctype
def gokul():
    frappe.msgprint("Hii")
    
 
 #get_pdf utility function 
@frappe.whitelist(allow_guest=True)
def generate_invoice():

    cart = {
        'Samsung Galaxy S20': 10,
        'iPhone 13': 80
    }

    html = '<h1>Invoice from Star Electronics e-Store!</h1>'
    html += '<ol>'

    for item, qty in cart.items():
        html += f'<li>{item} - {qty}</li>'

    html += '</ol>'

    # Prepare file response
    frappe.local.response.filename = "invoice.pdf"
    frappe.local.response.filecontent = frappe.utils.pdf.get_pdf(html)
    frappe.local.response.type = "pdf"


@frappe.whitelist(allow_guest=True)
def publish():
     frappe.publish_realtime("test_event", {"text": "Hello World!"})