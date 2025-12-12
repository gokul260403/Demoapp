import frappe


#### frappe.qb.get_query############
#basic query
query=frappe.qb.get_query("student")
print(query.run(as_dict=True))


#basic query with fields
query=frappe.qb.get_query("student",fields=["student_name" ,"email"])
print(query.run(as_dict=True))


# Select specific fields
query = frappe.qb.get_query("student", fields=["student_name", "email"])

# You can also pass fields as a comma-separated string
query = frappe.qb.get_query("student", fields="student_name, email")

# Or select all fields using '*'
query = frappe.qb.get_query("student", fields="*")


## using aliases
query = frappe.qb.get_query(
    "student",
    fields=["student_name as user_name", "email as user_email"]
)
print(query.run(as_dict=True))

##liked documents fields
query=frappe.qb.get_query("Leave Application",fields=["name","emp_name.employee_name as emp_name"])
print(query.run(as_dict=True))

##### child tabel feilds
query=frappe.qb.get_query("student",fields=["name","marksheet.subject",],filters={"name":"raju006"})
print(query.run())


##Fetching child table records
query = frappe.qb.get_query(
    "student",
    fields=[
        "name",
        "student_name",
        {"marksheet": ["subject", "score"]}  
    ],
    limit=5
)
print(query.run(as_dict=True))




# Dictionary Filters (Equality) 
# filters={"first_name": "Admin"}



#####Dictionary Filters (Other Operators) #############

# filters={"creation": [">", "2023-01-01 00:00:00"]}
# filters={"name": ["in", ["test1@example.com", "test2@example.com"]]}



############List Filters (Alternative Format) ##################

# You can also provide a list containing filter lists [[fieldname, operator, value]].
# filters=[["creation", ">", "2023-01-01 00:00:00"]]

# filters=[
#         ["enabled", "=", 1],
#         ["user_type", "=", "System User"]
#     ]


# Filtering on Linked Document Fields 

query = frappe.qb.get_query(
    "Leave Application",
    fields=["name", "emp_name","role"],
    filters={"emp_name.role": "SE"} 
)
print(query.run(as_dict=True))

##filtering using child table fields
query=frappe.qb.get_query("student",fields=["name","student_name"],filters={"marksheet.subject":"sub2"})
print(query.run())


# Logical Operators (AND/OR) 
# filters_and = [
#     ["enabled", "=", 1],
#     "and",
#     ["first_name", "=", "Admin"],]





##ordering#####

query=frappe.qb.get_query("student",fields=["name",'Student_name','age'],filters={"address":"mkm"},order_by="student_name asc")
print(query.run())


#####Grouping#####
query=frappe.qb.get_query("Leave Application",fields=["emp_name","COUNT(*) as leaves_applied"],group_by="emp_name")
print(query.run())

####pagination##########
query=frappe.qb.get_query("student", limit=10 )
print(query.run())