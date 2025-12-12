
"""Importing all the necessary libraries..."""
import os
import requests
import pandas as pd


"""Checking the the excel file is present locally on your system or not.If not, using requests module 
download the excel file. Then create a new excel file using write mode and write the content which you got from downloaded file
into this excel file."""
if not os.path.isfile("Px-01/Airport_Data.xlsx"):
    r=requests.get("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/analysing-spreadsheet-data-with-python/Airport_Data.xlsx")
    f=open("Px-01/Airport_Data.xlsx","wb+")
    f.write(r.content)
    f.close()


"""Using pandas read the excel file and sheet name=Facilities and print it"""
df_facilities=pd.read_excel("Px-01/Airport_Data.xlsx",sheet_name="Facilities")
print("Printing the data values from the downloaded excel file...")
print(df_facilities)
print()


"""What are the types for aviation facilities in Alaska? that are unique no duplicate values"""
print("Printing unique values from the excel of *Type* attribute or column ")
print(df_facilities["Type"].unique())
print()


"""Provide a table containing the information for all Seaplane Bases in Alaska"""
print("table containing the information for all Seaplane Bases in Alaska")
print(df_facilities[df_facilities["Type"] == "SEAPLANE BASE"])
print()


"""What are the 5 highest aviation facilities in Alaska?"""
print("The 5 highest aviation facilities in Alaska?")
print(df_facilities.sort_values(by = "ARPElevation", ascending = False).head(n = 5))
print()


"""What is the average elevation of aviation facilities?"""
print("The average elevation of aviation facilities")
print(df_facilities["ARPElevation"].mean())
print()


"""Find the highest elevation value"""
print("Find the highest elevation value")
print(df_facilities["ARPElevation"].max())
print()


"""Find the lowest elevation value"""
print("Find the lowest elevation value")
print(df_facilities["ARPElevation"].min())
print()


"""Storing Seaplane bases information on a separate excel file."""
seaplane=df_facilities[df_facilities["Type"]=="SEAPLANE BASE"]
seaplane.to_excel("Px-01/seaplane.xlsx")

