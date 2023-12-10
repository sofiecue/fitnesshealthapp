# Health and Fitness Club Management System

Demo Link: https://vimeo.com/893139489/8c07ca09c3?share=copy (demo is also added as an MP4 backup in github)

The system created designs and implements a Health and Fitness Club Management System. The designs are outlined in the 
report primarily and accompanying diagrams and database schemas.

The implementation and code portion of the system is organized into parts: 
- DDL & SQL Queries for preliminary database population
- A CLI application for Admin to navigate the database and conduct duties in billing, room booking & equipment maintenance
- A GUI for Club Members which currently include a login and central dashboard
- Images and diagrams mockups for the GUI

## Directory Structure

[directory structure image in images/structure.png](images/structure.png)


## Setup Instructions:
**Prerequisites**
As a prerequisite I will run through the tooling used briefly, the report goes into further detail.
The CLI application is python-based and makes use of [psycopg2](https://pypi.org/project/psycopg2/) and Python. If you havent, you can install psycopg2 using: pip install psycopg2
Equally, if you do not have python installed, that can be done by downloading from [here] (https://www.python.org/downloads/).

The GUI makes use of bootstrap and requires a npm init/npm install.

**How to run the applications:**
1. Navigate to the correct directory, you should be in admin_app as an Admin to run Admin user roles.
    You should be in Fitness_App to run the GUI Member views.
2. First, to test the CLI, in admin_app, enter: python3 app.py
3. A command line interface will pop up, continue to follow the instructions given there to operate the functions
and make changes to the database.
4. Secondly, to test the GUI you can right-click and "open in browser" the login_form.html and dashboard.html after having setup with npm install/npm init


**Brief Explanation of Functions in CLI app.py**

- deleteHelper() - takes input and passes them to removeRecordWith()
- removeRecordWith() - deletes a record from the given table with the given parameters
- updateRecordHelper() - takes input and passes them to the correct function, either: updateBillingRecord, updateEquipmentConditionRecord or updateRoomBookingRecord
- updateBillingRecord() - updates any field of billing
- updateEquipmentConditionRecord() - updates any field of equipment_condition
- updateRoomBookingRecord() - updates any field of room_bookings
- getInfoToAddRecord() - takes input and passes them to the correct function, either: addBillRecord, addEquipmentConditionRecord or addRoomBookingRecord
- addBillRecord() - adds a record to billing
- addEquipmentConditionRecord() - adds a record to equipment_condition
- addRoomBookingRecord() - adds a record to room_bookings
- endSession() - raises exception to exit looping the interface
- getAllRecordsOf() - retrieves and displays all records of a given table
- main() - prints the main interface instructions and calls other functions


