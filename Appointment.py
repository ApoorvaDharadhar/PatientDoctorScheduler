from datetime import datetime, date

import DBase as db;
import Doctor as dc;
import Patient as pt;


class Appointment(db.DBase):

    _appointment_id = None
    _doctor_id = None
    _patient_id = None
    _appointment_date = None
    _status = None
    _notes = None


    def __init__(self, appointment_id=None, doctor_id=None, patient_id=None,appointment_date=None, status=None ,notes = None):
        super().__init__("PatientDoctorScheduler.sqlite")
        self._appointment_id = appointment_id
        self._doctor_id = doctor_id
        self._patient_id = patient_id
        self._appointment_date = appointment_date
        self._status = status
        self._notes = notes


    def reset_database(self):
        try:
            # print("Here")
            # doctor_id, patient_id,appointment_date, status ,notes
            sql = """
            DROP TABLE IF EXISTS Appointment;

            CREATE TABLE Appointment(
            appointment_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            doctor_id Integer,
            patient_id Integer,
            appointment_date DATE,
            appointment_time TEXT,
            status TEXT,
            notes TEXT,
            FOREIGN KEY (doctor_id) REFERENCES Doctor(doctor_id),
            FOREIGN KEY (patient_id) REFERENCES Doctor(patient_id)
            );
            """

            self.execute_script(sql)

        except Exception as e:
            print("An error occurred" + e)
        finally:
            super().close_db()


    def select_doctor(self):
        print("Please select the doctor based on your need!")

        doc = dc.Doctor(firstName=None, lastName=None, date_of_birth=None, gender=None, email_id=None, phone_num=None,
                        specialization=None, location_id=None)

        print(
            "\n1. Fetch by County \n2. Fetch by City \n3. Fetch by State \n4. Fetch by Country \n5. Fetch by ZipCode \n6. Fetch by FirstName \n7. Fetch by LastName \n8. Fetch by Specialization \n9. Fetch All \n10. Exit")
        user_selection = int(input("Choose an option: "))
        if user_selection == 1:
            county_name = input("Please enter the name of the county to search by: ")
            doctors = doc.fetch_doctor_records(field="county", value=county_name)
        elif user_selection == 2:
            city_name = input("Please enter the name of the city to search by: ")
            doctors = doc.fetch_doctor_records(field="city", value=city_name)
        elif user_selection == 3:
            state_name = input("Please enter the name of the state to search by: ")
            doctors = doc.fetch_doctor_records(field="state", value=state_name)
        elif user_selection == 4:
            country_name = input("Please enter the name of the country to search by: ")
            doctors = doc.fetch_doctor_records(field="country", value=country_name)
        elif user_selection == 5:
            zip_code = int(input("Please enter the zipcode of the location to search by: "))
            doctors = doc.fetch_doctor_records(field="zipcode", value=zip_code)
        elif user_selection == 6:
            firstName = input("Please enter the firstName of the doctor to search by:")
            doctors = doc.fetch_doctor_records(field="firstName", value=firstName)
        elif user_selection == 7:
            lastName = input("Please enter the lastName of the doctor to search by:")
            doctors = doc.fetch_doctor_records(field="lastName", value=lastName)
        elif user_selection == 8:
            specialization = input("Please enter the specialization of the doctor to search by:")
            doctors = doc.fetch_doctor_records(field="specialization", value=specialization)
        elif user_selection == 9:
            doctors = doc.fetch_doctor_records(field=None, value=None)

        for doctor in doctors:
            print(f"----- Doctor Details -----")
            print(f"  ID: {doctor[0]}")
            print(f"  Name: {doctor[1]} {doctor[2]}")
            print(f"  Gender: {doctor[3]}")
            print(f"  Email: {doctor[4]}")
            print(f"  Phone: {doctor[5]}")
            print(f"  DOB: {doctor[6]}")
            print(f"  Specialization: {doctor[7]}")
            print(f"  Location ID: {doctor[8]}")

        doc_id_user_inp = int(input("Please enter the doctor_id: "))
        return doc_id_user_inp


    def select_patient(self):
        p = pt.Patient(firstName=None, lastName=None, date_of_birth=None, gender=None, email_id=None, phone_num=None)

        print("\n1. Fetch by patient_id \n2. Fetch by First Name \n3. Fetch by Last Name \n4. Fetch All")
        sequence_id = int(input("\nPlease enter your choice: "))
        if sequence_id == 1:
            pt_id = int(input("Please enter the PatientID: "))
            patients = p.fetch(pt_id, None, None)
        elif sequence_id == 2:
            pt_first_name = input("Please enter the FirstName: ")
            patients = p.fetch(None, pt_first_name, None)
            # print("Here")
            print(p.fetch(None, pt_first_name, None))
        elif sequence_id == 3:
            pt_last_name = input("Please enter the LastName: ")
            patients = p.fetch(None, None, pt_last_name)
        elif sequence_id == 4:
            patients =p.fetch(None, None, None)
        else:
            print("Please enter a valid choice!!")

        for patient in patients:
            print(f"----- Patient Details -----")
            print(f"  ID: {patient[0]}")
            print(f"  First Name: {patient[1]}")
            print(f"  Last Name: {patient[2]}")
            print(f"  Date of Birth: {patient[3]}")
            print(f"  Gender: {patient[3]}")
            print(f"  Email: {patient[4]}")
            print(f"  Phone: {patient[5]}")

        # firstName=None, lastName=None, date_of_birth=None, gender=None, email_id=None, phone_num=None
        patient_id_user_inp = int(input("Please enter the patient_id: "))
        return patient_id_user_inp

    def show_doctors_schedule(self, doctor_id):
        try:
            if doctor_id is not None:
                return self.get_cursor.execute("select * from Appointment where doctor_id = ?", (doctor_id,)).fetchone()
            else:
                raise ValueError("Doctor ID must not be None")
        except Exception as e:
            print("An error has occurred: " + str(e))

    def add_appointment(self):

        # First select the doctor based on firstname/lastname/specialization/location/fetch all doctors
        doctor_id = self.select_doctor()

        #Select the patient by searching using the available filters
        patient_id = self.select_patient()

        #Show available slots to the user for the selected Doctor
        print(self.show_doctors_schedule(doctor_id))

        from datetime import datetime, date

        # Let the user select the date for which they want to book the appointment
        # Formatting the date in the correct format "YYYY-MM-DD"
        user_inp_appt_date = input("Please select the date for appointment: (YYYY-MM-DD) ")
        appointment_date = datetime.strptime(user_inp_appt_date, "%Y-%m-%d")

        # The selected date by the user should be today's or future. Making sure that the user does not
        # select any previous dates.
        if appointment_date.date() < date.today():
            print("The selected date must be in the future. Please choose a different date.")
            return

        # Making sure that the time selected is between 8 am an 16:45(working hours)
        time_str = input("Please select the time between 08:00 to 16:45 for the appointment (HH:MM): ")
        available_slot_1 = datetime.strptime("08:00", "%H:%M").time()
        available_slot_2 = datetime.strptime("16:45", "%H:%M").time()
        appointment_time = datetime.strptime(time_str, "%H:%M").time()
        if(appointment_time>=available_slot_1 and appointment_time<=available_slot_2):
            appointment_time_str = appointment_time.strftime("%H:%M:%S")
        else:
            print("The selected time slot should be between 08:00 to 16:45. Please choose a different time.")
            return


        try:
            # Checking if the selected doctor has an already scheduled appointment at the selected time and date
            self.get_cursor.execute("""
                select * from Appointment WHERE doctor_id = ? AND appointment_date = ? AND appointment_time = ? """,
            (doctor_id, appointment_date, appointment_time_str))

            existing_appointment = self.get_cursor.fetchone()

            if existing_appointment:
                print("The selected time slot is already taken. Please choose a different time.")
                return

            # If there is no appointment scheduled for the selected time, date for the selected doctor, we
            # go ahead and schedule an appointment for the selected patient.
            self.get_cursor.execute("""
                insert or ignore into Appointment (doctor_id, patient_id,appointment_date, appointment_time, status ,notes)
                VALUES (?, ?, ?, ?, ?, ?)""", (
            doctor_id, patient_id, appointment_date, appointment_time_str, "Scheduled", None ))
            self.get_connection.commit()
            print("Appointment created successfully!")
        except Exception as e:
            print("An error has occurred: " + str(e))


    def cancel_appointment(self):
        # Cancelling the appointment by taking appointment ID as the input.
        user_inp_appt_id = int(input("Please enter the appointment ID for cancellation: "))

        try:
            self._cursor.execute("delete from Appointment where appointment_id = ?", (user_inp_appt_id,))
            self._conn.commit()
            print(f"Deleted the Appointment (Appointment ID: {user_inp_appt_id} ) successfully!")
        except Exception as e:
            print("An error has occurred: " + str(e))

    def fetch_appointments(self, field, value):
            try:

                if field is None or value is None:
                    query = """
                            SELECT 
                                  apt.appointment_id,
                                  apt.appointment_date,
                                  apt.appointment_time,
                                  apt.status,
                                  apt.notes,
                                  doc.firstName || ' ' || doc.lastName AS doctor_name,
                                  pt.firstName || ' ' || pt.lastName AS patient_name
                            FROM Appointment apt
                            INNER JOIN Doctor doc ON apt.doctor_id = doc.doctor_id
                            INNER JOIN Patients pt ON apt.patient_id = pt.patient_id;
                            """
                    params = ()
                else:
                    query = f"""
                            SELECT 
                                apt.appointment_id,
                                apt.appointment_date,
                                apt.appointment_time,
                                apt.status,
                                apt.notes,
                                doc.firstName || ' ' || doc.lastName AS doctor_name,
                                pt.firstName || ' ' || pt.lastName AS patient_name
                            FROM Appointment apt
                            INNER JOIN Doctor doc ON apt.doctor_id = doc.doctor_id
                            INNER JOIN Patients pt ON apt.patient_id = pt.patient_id
                            WHERE apt.{field} = ?
                            """
                    params = (value,)

                    # Execute the query
                appointments = self.get_cursor.execute(query, params).fetchall()
                #
                for apt in appointments:
                    print(f"----- Appointment Details -----")
                    print(f"  Appointment ID: {apt[0]}")
                    print(f"  Appointment Date: {apt[1]} ")
                    print(f"  Appointment Time: {apt[2]}")
                    print(f"  Status: {apt[3]}")
                    print(f"  Notes: {apt[4]}")
                    print(f"  Doctor Name: {apt[5]}")
                    print(f"  Patient Name: {apt[6]}")

            except Exception as e:
                print("An error has occurred."+e)


    def update_appointment(self):
        # print("In the Appointment class")
        user_inp_appt_id = int(input("Please enter the appointment ID for updation: "))



        sequence_id = 0
        while (sequence_id != 7):
            # Setting the status on each condition to update in the database.
            print("What do you want to update \nPlease enter the item number! \n1. Appointment Date \n2. Appointment Time \n3. Notes \n4. Exit")
            sequence_id = int(input("\nPlease enter your choice: "))

            if sequence_id == 1:
                parameter_to_update = "appointment_date"
                status = "Appointment Date Updated"
            elif sequence_id == 2:
                parameter_to_update = "appointment_time"
                status = "Appointment Time Updated"

            elif sequence_id == 3:
                parameter_to_update = "notes"
                status = "Noes Updated"

            else:
                break

            value = input(f"\nNew Value for {parameter_to_update}:")

            try:

                self.get_cursor.execute(f"update Appointment set {parameter_to_update} = ?, status = ? where appointment_id = ?", (value,status, user_inp_appt_id))
                self.get_connection.commit()
                print("Appointment record updated successfully!")

            except Exception as e:
                print("An error has occurred: " + str(e))


