# will run before file is written to disk
import frappe
import os

 

# before_write_file hook: use **kwargs
def before_write(**kwargs):
   print("before writing a file")

# will override the implementation of writing file to disk
# can be used to upload files to a CDN instead of writing
# the file to disk
# def write_file():
#     pass


# # will override the implementation of deleting file from disk
# # can be used to delete uploaded files from a CDN instead of
# # deleting file from disk
# def delete_file():
#     pass


