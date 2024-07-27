import DBase as db


class Patient(db.DBase):
    _allowed_column_names = ['firstname', 'lastname', 'date_of_birth', 'gender',
                             'email_id', 'phone_number']
    _firstName = None
    _lastName = None
    _date_of_birth = None
    _gender = None
    _email_id = None
    _phone_num = None

    def __init__(self, firstName=None, lastName=None, date_of_birth=None, gender=None, email_id=None, phone_num=None):
        super().__init__("PatientDoctorScheduler.sqlite")
        self._firstName = firstName
        self._lastName = lastName
        self._date_of_birth = date_of_birth
        self._gender = gender
        self._email_id = email_id
        self._phone_num = phone_num

    def update_patient_name(self, patient_id, parameter, value):
        try:
            # Update the patient data
            if parameter not in self._allowed_column_names:
                raise ValueError(f"Invalid column name: {parameter}")
            self._cursor.execute(f"update Patients set {parameter} = ? where patient_id = ?", (value, patient_id))
            self._conn.commit()
            print("Patient record updated successfully!")
            # print(self.fetch(patient_id))
        except Exception as e:
            print("An error has occurred: " + str(e))

    def add_patient(self):
        try:
            # Add the patient data
            self._cursor.execute("""
                insert or ignore into Patients (firstName, lastName, date_of_birth, gender, email_id, phone_number)
                VALUES (?, ?, ?, ?, ?, ?)""", (
            self._firstName, self._lastName, self._date_of_birth, self._gender, self._email_id, self._phone_num))
            self._conn.commit()
            print("Patient record created successfully!")
        except Exception as e:
            print("An error has occurred: " + str(e))

    def delete(self, patient_id):
        try:
            self._cursor.execute("delete from Patients where patient_id = ?", (patient_id,))
            self._conn.commit()
            print(f"Deleted the patient with patient_id: {patient_id} successfully!")
        except Exception as e:
            print("An error has occurred: " + str(e))

    def fetch(self, patient_id=None, patient_first_name=None, patient_last_name=None):
        try:
            # Fetch the patient data using patient_id, firstname, lastname
            if patient_id is not None:
                # print("I am here")
                # print(patient_id)
                return self.get_cursor.execute("select * from Patients where patient_id = ?", (patient_id,)).fetchone()
            if patient_first_name is not None:
                query = "select * from Patients where firstname like ?"
                return self.get_cursor.execute(query, (patient_first_name + '%',)).fetchall()
            if patient_last_name is not None:
                query = "select * from Patients where lastname like ?"
                return self.get_cursor.execute(query, (patient_last_name + '%',)).fetchall()
            else:
                return self.get_cursor.execute("select * from Patients").fetchall()
        except Exception as e:
            print("An error has occurred: " + str(e))

    def reset_database(self):
        try:
            # To be called only once.
            sql = """
            drop table if exists Patients;

            create table Patients(
                patient_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                firstName TEXT,
                lastName TEXT,
                date_of_birth DATE,
                gender TEXT,
                email_id TEXT,
                phone_number TEXT
            )
            """
            self.execute_script(sql)
        except Exception as e:
            print("An error occurred: " + str(e))
        finally:
            self.close_db()

