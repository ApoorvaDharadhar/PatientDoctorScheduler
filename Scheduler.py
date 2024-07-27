import DBase as db;
import Doctor as dc;
import Patient as pt;
import Appointment as at;
from Location import Location
import csv


while True:
    print("\n1. Manage Patients \n2. Manage Doctors \n3. Manage Appointments \n4. Import Data from CSV for Location table \n5. Exit")
    main_user_selection = input("Choose an option: ")

    # Making sure the user enters the valid choice in switch case.
    if not main_user_selection.isnumeric() or int(main_user_selection)>5:
        print("Please enter a valid ID!")
    else:
        # Converting the users selection to integer as we will be comparing the choice with integers in this while loop
        main_user_selection = int(main_user_selection)
        if main_user_selection == 1:
            p = pt.Patient()
            while True:
                print(
                    "\n1. Add Patient \n2. Update Patient Data \n3. Delete Patient Record \n4. Fetch Patient Record(s) \n5. Exit \n")
                user_selection = int(input("Choose an option: "))
                if user_selection == 1:
                    # Add Patient Logic
                    print("\nPlease enter the below patient information!")
                    firstName = input("\nFirst Name: ")
                    lastName = input("\nLast Name: ")
                    dob = input("\nDate of Birth (YYYY-MM-DD): ")
                    gender = input("\nGender: ")
                    emailID = input("\nEmail ID: ")
                    phone_num = input("\nPhone Number: ")

                    # Patient class's object patient
                    patient = pt.Patient(firstName, lastName, dob, gender, emailID, phone_num)
                    # Calling the add function from Patient class
                    patient.add_patient()

                if user_selection == 2:
                    # Displaying the patient list before the user can select what they intend to update for
                    # a particular patient
                    patients = p.fetch()

                    for patient in patients:
                        print(f"----- Patient Details -----")
                        print(f"  ID: {patient[0]}")
                        print(f"  First Name: {patient[1]}")
                        print(f"  Last Name: {patient[2]}")
                        print(f"  Date of Birth: {patient[3]}")
                        print(f"  Gender: {patient[3]}")
                        print(f"  Email: {patient[4]}")
                        print(f"  Phone: {patient[5]}")

                    id = int(input("Enter the patient_id you want to update: "))

                    parameter_to_update = ""
                    sequence_id = 0
                    # Choice of update
                    while (sequence_id != 7):
                        print(
                            "What do you want to update \nPlease enter the item number! \n1. First Name \n2. Last Name \n3. Date of Birth \n4. Gender \n5. Email ID \n6. Phone Number \n7. Exit")
                        sequence_id = int(input("\nPlease enter your choice: "))

                        if sequence_id == 1:
                            parameter_to_update = "firstname"
                        elif sequence_id == 2:
                            parameter_to_update = "lastname"
                        elif sequence_id == 3:
                            parameter_to_update = "date_of_birth"
                        elif sequence_id == 4:
                            parameter_to_update = "gender"
                        elif sequence_id == 5:
                            parameter_to_update = "email_id"
                        elif sequence_id == 6:
                            parameter_to_update = "phone_number"
                        elif sequence_id > 7:
                            print("Please enter a valid ID!")
                        elif sequence_id == 7:
                            break

                        value = input(f"\nNew Value for {parameter_to_update}:")
                        p.update_patient_name(id, parameter_to_update, value)

                if user_selection == 3:
                    # Patient deletion logic
                    patients = p.fetch()

                    for patient in patients:
                        print(f"----- Patient Details -----")
                        print(f"  ID: {patient[0]}")
                        print(f"  First Name: {patient[1]}")
                        print(f"  Last Name: {patient[2]}")
                        print(f"  Date of Birth: {patient[3]}")
                        print(f"  Gender: {patient[3]}")
                        print(f"  Email: {patient[4]}")
                        print(f"  Phone: {patient[5]}")

                    id = int(input("Enter the patient_id you want to delete: "))
                    p.delete(id)

                if user_selection == 4:
                    # Fetch patient logic. We can fetch the patient details using their firstName, lastName,
                    # fetch all patients with no filter or fetch using patient ID
                    print("\n1. Fetch by patient_id \n2. Fetch by First Name \n3. Fetch by Last Name \n4. Fetch All")
                    sequence_id = int(input("\nPlease enter your choice: "))
                    if sequence_id == 1:
                        pt_id = int(input("Please enter the PatientID: "))
                        patients  = p.fetch(pt_id, None, None)
                    elif sequence_id == 2:
                        pt_first_name = input("Please enter the FirstName: ")
                        patients = p.fetch(None, pt_first_name, None)
                    elif sequence_id == 3:
                        pt_last_name = input("Please enter the LastName: ")
                        patients = p.fetch(None, None, pt_last_name)
                    elif sequence_id == 4:
                        patients  = p.fetch(None, None, None)

                    # Check if 'patients' is a tuple or a list
                    if isinstance(patients, tuple):
                        # Single tuple case
                        if len(patients) == 7:  # Assuming a valid single tuple has exactly 7 elements
                            print("----- Patient Details -----")
                            print(f"  ID: {patients[0]}")
                            print(f"  First Name: {patients[1]}")
                            print(f"  Last Name: {patients[2]}")
                            print(f"  Date of Birth: {patients[3]}")
                            print(f"  Gender: {patients[4]}")
                            print(f"  Email: {patients[5]}")
                            print(f"  Phone: {patients[6]}")
                        else:
                            print("No record(s) found!")
                    elif isinstance(patients, list) and all(isinstance(p, tuple) for p in patients):
                        # List of tuples case
                        if len(patients) == 0:
                            print("No record(s) found!")
                        else:
                            for patient in patients:
                                print("----- Patient Details -----")
                                print(f"  ID: {patient[0]}")
                                print(f"  First Name: {patient[1]}")
                                print(f"  Last Name: {patient[2]}")
                                print(f"  Date of Birth: {patient[3]}")
                                print(f"  Gender: {patient[4]}")
                                print(f"  Email: {patient[5]}")
                                print(f"  Phone: {patient[6]}")
                    else:
                        print("Unexpected data format.")

                if user_selection == 5:
                    break;

        elif main_user_selection == 2:
            # CRUD operation on Doctor
            while True:
                print(
                    "\n1. Add Doctor \n2. Update Doctor Data \n3. Delete Doctor Record \n4. Fetch Doctor Record(s) \n5. Exit \n")
                user_selection = input("Choose an option: ")

                if not user_selection.isnumeric() or int(user_selection) > 5:
                    print("Make a valid choice!")
                else:
                    user_selection = int(user_selection)

                    if user_selection == 1:
                        print("\nPlease enter the below doctor's information!")
                        firstName = input("\nFirst Name: ")
                        lastName = input("\nLast Name: ")
                        gender = input("\nGender: ")
                        emailID = input("\nEmail ID: ")
                        phone_num = input("\nPhone Number: ")
                        dob = input("\nDate of Birth (YYYY-MM-DD): ")
                        specialization = input("\nSpecialization: ")
                        county = input("\nCounty: ")
                        city = input("\nCity: ")
                        state = input("\nState: ")
                        zip = int(input("\nZip: "))
                        country = input("\nCountry: ")
                        doc_loc = Location(county, state, city, zip, country)

                        location_id = doc_loc.fetch_by_all(county, city, state, zip, country)
                        # If user enters county, city, state, zip, country which is not present in the
                        # Location table in the database, then the program will prompt the user asking
                        # whether they want to create a record of this location in the database.
                        if location_id is None:
                            inp_select= input("Looks like we do not have this location in records! \n1. Do you want to add a new location? \n2. View the existing locations")
                            locte = Location(county, state, city, zip, country)
                            if not inp_select.isnumeric() or int(inp_select) > 3:
                                print("Please make a valid selection!")

                            inp_select = int(inp_select)
                            if inp_select == 1:
                                # Adding the location first and then finding the corresponding location_id to
                                # add the doctor's record to the database.
                                locte.add_location()
                                print("Location added successfully!")
                                location_id = doc_loc.fetch_by_all(county, city, state, zip, country)
                            elif inp_select == 2:
                                # Displaying all the records of the database and asking for user's input
                                locte.fetch(county=None, city=None, state=None, country=None, zipcode=None)
                                location_id = int(input("Please enter the location ID."))

                        doctor = dc.Doctor(firstName, lastName, dob, gender, emailID, phone_num, specialization, location_id[0])
                        doctor.add_doctor()

                    elif user_selection == 2:
                        # Logic for updating the doctor records
                        doc = dc.Doctor(None, None, None, None, None, None, None, None)

                        # We first display all doctor records and ask the user for doctor_id that
                        # they wish to update
                        docs_info = doc.fetch_doctor_records(field=None, value=None)

                        for doctor in docs_info:
                            print(f"----- Doctor Details -----")
                            print(f"  ID: {doctor[0]}")
                            print(f"  Name: {doctor[1]} {doctor[2]}")
                            print(f"  Gender: {doctor[3]}")
                            print(f"  Email: {doctor[4]}")
                            print(f"  Phone: {doctor[5]}")
                            print(f"  DOB: {doctor[6]}")
                            print(f"  Specialization: {doctor[7]}")
                            print(f"  Location ID: {doctor[8]}")

                        id = int(input("Enter the doctor_id you want to update: "))
                        parameter_to_update = ""
                        sequence_id = 0
                        while (sequence_id != 9):
                            print("What do you want to update \nPlease enter the item number! "
                            "\n1. First Name \n2. Last Name \n3. Gender \n4. Email ID \n5. Phone Number "
                            "\n6. Date of Birth \n7. Specialization \n8. Location Details \n9. Exit")
                            sequence_id = input("\nPlease enter your choice: ")

                            if not sequence_id.isnumeric():
                                print("Please enter a valid ID!")
                            #   Making sure that user selects a valid input
                            else:
                                sequence_id = int(sequence_id)
                            # firstName, lastname, gender, email_id, phone_number, date_of_birth, specialization
                            if sequence_id == 1:
                                parameter_to_update = "firstName"
                                value = input(f"\nNew Value for {parameter_to_update}:")
                                doc.update_doctor(id, parameter_to_update, value)
                            elif sequence_id == 2:
                                parameter_to_update = "lastname"
                                value = input(f"\nNew Value for {parameter_to_update}:")
                                doc.update_doctor(id, parameter_to_update, value)
                            elif sequence_id == 3:
                                parameter_to_update = "gender"
                                value = input(f"\nNew Value for {parameter_to_update}:")
                                doc.update_doctor(id, parameter_to_update, value)
                            elif sequence_id == 4:
                                parameter_to_update = "email_id"
                                value = input(f"\nNew Value for {parameter_to_update}:")
                                doc.update_doctor(id, parameter_to_update, value)
                            elif sequence_id == 5:
                                parameter_to_update = "phone_number"
                                value = input(f"\nNew Value for {parameter_to_update}:")
                                doc.update_doctor(id, parameter_to_update, value)
                            elif sequence_id == 6:
                                parameter_to_update = "date_of_birth"
                                value = input(f"\nNew Value for {parameter_to_update}:")
                                doc.update_doctor(id, parameter_to_update, value)
                            elif sequence_id == 7:
                                parameter_to_update = "specialization"
                                value = input(f"\nNew Value for {parameter_to_update}:")
                                doc.update_doctor(id, parameter_to_update, value)
                            elif sequence_id == 8:
                                county = input("\nNew Value for County: ")
                                city = input("\nNew Value for City: ")
                                state = input("\nNew Value for State: ")
                                zip = int(input("\nNew Value for Zip: "))
                                country = input("\nNew Value for Country: ")
                                doc_loc = Location(county, state, city, zip, country)

                                location_id = doc_loc.fetch_by_all(county, city, state, zip, country)

                                parameter_to_update = "location_id"
                                value =location_id[0]
                                doc.update_doctor(id, parameter_to_update, value)

                    elif user_selection == 3:
                        # Logic for deleting doctor's records
                        doc = dc.Doctor(None, None, None, None, None, None, None, None)

                        docs_info = doc.fetch_doctor_records(field=None, value=None)


                        for doctor in docs_info:
                            print(f"----- Doctor Details -----")
                            print(f"  ID: {doctor[0]}")
                            print(f"  Name: {doctor[1]} {doctor[2]}")
                            print(f"  Gender: {doctor[3]}")
                            print(f"  Email: {doctor[4]}")
                            print(f"  Phone: {doctor[5]}")
                            print(f"  DOB: {doctor[6]}")
                            print(f"  Specialization: {doctor[7]}")
                            print(f"  Location ID: {doctor[8]}")

                        doc_id_to_be_deleted = int(input("Please enter the doctor_id to delete: "))
                        doc.delete_doctor(doc_id_to_be_deleted)

                    elif user_selection == 4:
                        # Logic for fetching the doctors records.
                        # We can search the doctor by their firstname, lastName, date_of_birth, email_id,
                        # phone_num, specialization, location(county, state, city, country, zipode)

                        doc = dc.Doctor(None, None, None, None, None,
                                           None, None, None)
                        while True:
                            print(
                                "\n1. Fetch by County \n2. Fetch by City \n3. Fetch by State \n4. Fetch by Country \n5. Fetch by ZipCode \n6. Fetch by FirstName \n7. Fetch by LastName \n8. Fetch by Specialization \n9. Fetch All \n10. Exit")
                            user_selection = input("Choose an option: ")



                            if not user_selection.isnumeric() or int(user_selection) > 10:
                                print("Make a valid choice!")
                            else:
                                user_selection = int(user_selection)

                                if user_selection == 1:
                                    county_name = input("Please enter the name of the county to search by: ")
                                    if len(county_name) == 0:
                                        print("Please enter a county!!")
                                        break;
                                    else:
                                        docs_info = doc.fetch_doctor_records(field="county", value=county_name)
                                elif user_selection == 2:
                                    city_name = input("Please enter the name of the city to search by: ")
                                    if len(city_name)==0:
                                        print("Please enter a city!!")
                                    else:
                                        docs_info = doc.fetch_doctor_records(field="city", value=city_name)
                                elif user_selection == 3:
                                    state_name = input("Please enter the name of the state to search by: ")
                                    if len(state_name)==0:
                                        print("Please enter a state!!")
                                        break;
                                    else:
                                        docs_info = doc.fetch_doctor_records(field="state", value=state_name)
                                elif user_selection == 4:
                                    country_name = input("Please enter the name of the country to search by: ")
                                    if len(country_name) == 0:
                                        print("Please enter a country!!")
                                        break;
                                    else:
                                        docs_info = doc.fetch_doctor_records(field="country", value=country_name)
                                elif user_selection == 5:
                                    zip_code = int(input("Please enter the zipcode of the location to search by: "))
                                    if len(zip_code) == 0:
                                        print("Please enter a zipcode!!")
                                        break;
                                    else:
                                        docs_info = doc.fetch_doctor_records(field="zipcode", value=zip_code)
                                elif user_selection == 6:
                                    firstName = input("Please enter the firstName of the doctor to search by:")
                                    if len(firstName) == 0:
                                        print("Please enter a firstName!!")
                                        break;
                                    else:
                                        docs_info = doc.fetch_doctor_records(field="firstName", value=firstName)
                                elif user_selection == 7:
                                    lastName = input("Please enter the lastName of the doctor to search by:")
                                    # print(lastName+" lastName **")
                                    if len(lastName) == 0:
                                        print("Please enter a lastName!!")
                                        break;
                                    else:
                                        docs_info = doc.fetch_doctor_records(field="lastName", value=lastName)
                                elif user_selection == 8:
                                    specialization = input("Please enter the specialization of the doctor to search by:")
                                    if len(specialization) == 0:
                                        print("Please enter a specialization!!")
                                        break;
                                    else:
                                        docs_info = doc.fetch_doctor_records(field="specialization", value=specialization)
                                elif user_selection == 9:
                                    docs_info = doc.fetch_doctor_records(field=None, value=None)
                                elif user_selection == 10:
                                    break;
                                elif user_selection > 10:
                                    print("Please select a valid choice!")

                                for doctor in docs_info:
                                    print(f"----- Doctor Details -----")
                                    print(f"  ID: {doctor[0]}")
                                    print(f"  Name: {doctor[1]} {doctor[2]}")
                                    print(f"  Gender: {doctor[3]}")
                                    print(f"  Email: {doctor[4]}")
                                    print(f"  Phone: {doctor[5]}")
                                    print(f"  DOB: {doctor[6]}")
                                    print(f"  Specialization: {doctor[7]}")
                                    print(f"  Location ID: {doctor[8]}")


                    elif user_selection == 5:
                        break;

        elif main_user_selection == 3:
            app = at.Appointment()
            while True:
                print("\n1. Create Appointment \n2. Upate Appointment \n3. Cancel Appointment \n4. Fetch all Appointments \n5. Exit \n")
                user_selection = input("Choose an option: ")

                if not user_selection.isnumeric() or int(user_selection)>5:
                    print("Make a valid choice!")
                else:
                    user_select = int(user_selection)
                    print("You made a valid choice!")
                    if user_select == 1:
                        app.add_appointment()
                    elif user_select == 2:
                        app.fetch_appointments(None, None)
                        app.update_appointment()
                    elif user_select == 3:
                        app.cancel_appointment()
                    elif user_select == 4:
                        print("\n1. Fetch by Doctor_ID \n2. Fetch By Patient_ID \n3. Fetch All \n4. Exit")
                        fetch_select = input("Choose an option: ")
                        if not fetch_select.isnumeric() or int(fetch_select) > 4:
                            print("Make a valid choice!")
                        else:
                            fetch_select = int(fetch_select)
                            if fetch_select == 1:
                                dc_id = int(input("Please enter a doctor_id"))
                                app.fetch_appointments(field="doctor_id", value=dc_id)
                            elif fetch_select == 2:
                                pt_id = int(input("Please enter a patient_id"))
                                app.fetch_appointments(field="patient_id", value=pt_id)
                            elif fetch_select == 3:
                                app.fetch_appointments(field=None, value=None)
                            elif fetch_select == 4:
                                break;


                    else:
                        break;

        elif main_user_selection == 4:
            # Implemented the logic for importing the Location.csv file and saving the data in the database
            # Logic for insertion of only one table's data is implemented.

            file_path = input("Please enter the name of the file to be imported!")
            returned_val = []
            # file_path = 'Location.csv'
            with open(file_path, mode='r') as file:
                csv_reader = csv.reader(file)
                headers = next(csv_reader)
                rows = list(csv_reader)
                for row in rows:
                    county_from_csv = row[0]
                    state_from_csv = row[1]
                    city_from_csv = row[2]
                    zip_from_csv = row[3]
                    country_from_csv = row[4]
                    lc = Location(county_from_csv, state_from_csv, city_from_csv, zip_from_csv, country_from_csv)
                    returned_val.append(lc.add_location())
                if(len(returned_val) == len(rows)):
                    print("Records added successfully!")


        elif main_user_selection == 5:
            break;





