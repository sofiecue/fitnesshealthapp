import psycopg2

try:
    # initialize connection object
    connection = psycopg2.connect(database = "health_fitness", 
                        user = "postgres", 
                        host= 'localhost',
                        password = "postgres",
                        port = 5432)

    # cursor is our tool to executes queries connection on db
    cursor = connection.cursor()

    print("PostgreSQL server connection to database A4 information:")
    print(connection.get_dsn_parameters(), "\n")
 
    # deleteHelper = helper function takes input and passes them to removeRecordWith() which deletes records
    def deleteHelper():
        table_name = input("Enter the table where you want to delete a record, you may decide from the following: \n billing \n equipment_condition \n room_bookings \n Enter choice: ")
        if table_name == "billing":
            Bill_ID = input("Enter Bill_ID of the record you would like to remove: ")
            removeRecordWith("Billing", "Bill_ID", Bill_ID)

        elif table_name == "equipment_condition":
            ECondition_ID = input("Enter ECondition_ID of the record you would like to remove: ")
            removeRecordWith("Equipment_Condition", "ECondition_ID", ECondition_ID)

        elif table_name == "room_bookings":
            Room_ID = input("Enter Room_ID of the record you would like to remove: ")
            removeRecordWith("Room_Booking", "Room_ID", Room_ID)
        else:
            endSession();
    
    # Deletes the record of a given table, using a unique identifier and its value to select that record
    def removeRecordWith(table, uniqueIdentifier, IDValue):
        delete_record_sql = f"DELETE FROM {table} WHERE {uniqueIdentifier} = {IDValue};"
        cursor.execute(delete_record_sql)
        connection.commit()
        print("Student removed successfully.")
        print("Updated table:")
        getAllRecordsOf(table);

    # takes input and passes them to respective update functions depending on what admin accessible table is chosen
    def updateRecordHelper():
        table_name = input("Enter the table where you want to update a record, you may decide from the following: \n billing \n equipment_condition \n room_bookings \n Enter choice: ")
        if table_name == "billing":
            field_to_change = input("Enter the column you would like to change from (Amount, Due_Date, Is_Paid, Loyalty_Points)")
            Bill_ID = input("Enter Bill_ID of the record you would like to update: ")
            new_value = input("Enter the new value: ")
            updateBillingRecord(field_to_change, Bill_ID, new_value)

        elif table_name == "equipment_condition":
            field_to_change = input("Enter the column you would like to change from (Date_Checked, Description, Is_Broken, Location, Equipment_Type)")
            ECondition_ID = input("Enter ECondition_ID ID of the record you would like to update: ")
            new_value = input("Enter the new value: ")
            updateEquipmentConditionRecord(field_to_change, ECondition_ID, new_value)

        elif table_name == "room_bookings":
            field_to_change = input("Enter the column you would like to change from (Purpose, Location, Date, Start_Time, End_Time)")
            Room_ID = input("Enter Room_ID of the record you would like to update: ")
            new_value = input("Enter the new value: ")
            updateRoomBookingRecord(field_to_change, Room_ID, new_value)
        else:
            endSession();

    # Updates any fields in billing entity and returns result of action
    def updateBillingRecord(field_to_change, Bill_ID, new_value):
        update_billing_sql = f"UPDATE Billing SET {field_to_change} = '{new_value}' WHERE Bill_ID = {Bill_ID};"
        cursor.execute(update_billing_sql)
        connection.commit()
        print("Email updated successfully.")
        print("Updated table:")
        getAllRecordsOf("Billing");

    # Updates any fields in equipment_condition entity and returns result of action
    def updateEquipmentConditionRecord(field_to_change, ECondition_ID, new_value):
        update_billing_sql = f"UPDATE Equipment_Condition SET {field_to_change} = '{new_value}' WHERE ECondition_ID = {ECondition_ID};"
        cursor.execute(update_billing_sql)
        connection.commit()
        print("Email updated successfully.")
        print("Updated table:")
        getAllRecordsOf("Equipment_Condition");

    # Updates any fields in room_bookings entity and returns result of action
    def updateRoomBookingRecord(field_to_change, Room_ID, new_value):
        update_roomBook_sql = f"UPDATE Room_Booking SET {field_to_change} = '{new_value}' WHERE Room_ID = {Room_ID};"
        cursor.execute(update_roomBook_sql)
        connection.commit()
        print("Email updated successfully.")
        print("Updated table:")
        getAllRecordsOf("Room_Booking");


        # helper for addBillRecord, addEquipmentConditionRecord, addRoomBookingRecord. Gets the necessary information for a record to be added
    def getInfoToAddRecord():
        table_name = input("Enter the table you want to add a record to, you may decide from the following: \n billing \n equipment_condition \n room_bookings \n Enter choice: ")
        if table_name == "billing":
            Member_id = input("Enter member ID: ")
            amount = input("Enter bill amount due: ")
            loyalty_pts = input("Enter loyalty points associated: ")
            is_paid = input("Enter true if the bill has been paid, or false otherwise: ")
            due_date = input("Enter due date for payment: ")
            addBillRecord(Member_id, amount, due_date, is_paid, loyalty_pts)

        elif table_name == "equipment_condition":
            admin_id = input("Enter admin ID: ")
            location = input("Enter location: ")
            equipment_type = input("Enter the equipment type: ")
            description = input("Enter condition description report: ")
            date_checked = input("Enter date checked: ")
            is_broken = input("Enter true if the equipment is broken, or false otherwise: ")
            addEquipmentConditionRecord(admin_id, date_checked, description, is_broken, location, equipment_type)

        elif table_name == "room_bookings":
            trainer_id = input("Enter trainer ID who is booking: ")
            location = input("Enter location: ")
            purpose = input("Enter the purpose of booking: ")
            date = input("Enter date of booking: ")
            start_time = input("Enter the start time of booking period: ")
            end_time = input("Enter the end time of booking period: ")        
            addRoomBookingRecord(trainer_id, purpose, location, date, start_time, end_time)
        else:
            endSession();

    # admin adds a record to billing functionality
    def addBillRecord(Member_id, amount, due_date, is_paid, loyalty_pts):
        add_billing_sql = f"INSERT INTO Billing (Member_ID, Amount, Due_Date, Is_Paid, Loyalty_Points) VALUES ('{Member_id}', '{amount}', '{due_date}', '{is_paid}', '{loyalty_pts}');"
        cursor.execute(add_billing_sql)
        connection.commit()

        print("Bill added to billing table successfully.")
        print("Updated table:")
        getAllRecordsOf("Billing")

    # admin adds a record to equipment management functionality
    def addEquipmentConditionRecord(admin_id, date_checked, description, is_broken, location, equipment_type):
        add_equipCondition_sql = f"INSERT INTO Equipment_Condition (Admin_ID, Date_Checked, Description, Is_Broken, Location, Equipment_Type) VALUES ('{admin_id}', '{date_checked}', '{description}', '{is_broken}', '{location}', '{equipment_type}');"
        cursor.execute(add_equipCondition_sql)
        connection.commit()

        print("Equipment Condition Check added to Equipment Condition table successfully.")
        print("Updated table:")
        getAllRecordsOf("Equipment_Condition")

    # admin adds a record to room booking records functionality
    def addRoomBookingRecord(trainer_id, purpose, location, date, start_time, end_time):
        add_roomBooking_sql = f"INSERT INTO Room_Booking (Trainer_ID, Purpose, Location, Date, Start_Time, End_Time) VALUES ('{trainer_id}', '{purpose}', '{location}', '{date}', '{start_time}', '{end_time}');"
        cursor.execute(add_roomBooking_sql)
        connection.commit()

        print("Room booking added to room booking table successfully.")
        print("Updated table:")
        getAllRecordsOf("Room_Booking")

    # kicks user out of session, ends CL interface
    def endSession():
        raise Exception;

        # getAllRecordsOf = Shows all records of a given table name, taken by input (usually by a helper)
    def getAllRecordsOf(table_name):
        query = f"SELECT * FROM {table_name};"
        cursor.execute(query)
        records = cursor.fetchall()

        connection.commit()
        # loops through all records to display on each line
        for record in records:
            print(record)
        print("\n")
        return;

    def main():
        print("Welcome to the admin application for managing the fitness system admin work!")
        choice = input("Pick one of the following admin activities: \n0. Exit session \n1. Display all records of a table \n2. Add a new record to a table \n3. Update a column value of a record of a table \n4. Delete a record from a table\n")
        while (choice != 0):

            if choice =="1":
                table_name = input("Enter the table you want to query: ")
                getAllRecordsOf(table_name)
                choice = input("Pick one of the following admin activities: \n0. Exit session \n1. Display all records of a table \n2. Add a new record to a table \n3. Update a column value of a record of a table \n4. Delete a record from a table\n")

            elif choice =="2":
                getInfoToAddRecord()
                choice = input("Pick one of the following admin activities: \n0. Exit session \n1. Display all records of a table \n2. Add a new record to a table \n3. Update a column value of a record of a table \n4. Delete a record from a table\n")
            elif choice =="3":
                updateRecordHelper()
                choice = input("Pick one of the following admin activities: \n0. Exit session \n1. Display all records of a table \n2. Add a new record to a table \n3. Update a column value of a record of a table \n4. Delete a record from a table\n")
            elif choice =="4":
                deleteHelper()
                choice = input("Pick one of the following admin activities: \n0. Exit session \n1. Display all records of a table \n2. Add a new record to a table \n3. Update a column value of a record of a table \n4. Delete a record from a table\n")
            elif choice =="0":
                endSession();

    main()

except (Exception) as e:
    print("Some error occurred while attempting to connect to PostgreSQL", e)

finally:
    if (1):
        #close everything when done
        cursor.close()
        connection.close()
        exit()

