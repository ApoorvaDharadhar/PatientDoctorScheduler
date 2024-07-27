import DBase as db;
from Location import Location


class Doctor(db.DBase):
    _firstName = None
    _lastName = None
    _gender = None
    _email_id = None
    _phone_number = None
    _date_of_birth = None
    _specialization = None
    _location_id = None

    _allowed_column_names = [
        'firstName', 'lastname', 'gender', 'email_id', 'phone_number', 'date_of_birth', 'specialization',
        'location_id'
    ]

    def __init__(self, firstName=None, lastName=None, date_of_birth=None, gender=None, email_id=None, phone_num=None, specialization =None, location_id=None):
        super().__init__("PatientDoctorScheduler.sqlite")
        self._firstName = firstName
        self._lastName = lastName
        self._gender = gender
        self._email_id = email_id
        self._phone_number = phone_num
        self._date_of_birth = date_of_birth
        self._specialization = specialization
        self._location_id = location_id



    def add_doctor(self):
        try:
            # Add the doctor with location details. Doctor table has the location_id as the foreign key.
            self.get_cursor.execute("""
                insert or ignore into Doctor (firstName, lastName, date_of_birth, gender, email_id, phone_number, specialization, location_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (
            self._firstName, self._lastName, self._date_of_birth, self._gender, self._email_id, self._phone_number, self._specialization, self._location_id ))
            self.get_connection.commit()
            print("Doctor record created successfully!")
        except Exception as e:
            print("An error has occurred: " + str(e))

    # county=None, city=None, state=None, zip =None, country=None, firstName=None, lastname =None, specialization=None
    def fetch_doctor_records(self, field, value):
        try:
            # Logic for fetching doctor data
            # We fetch the data by name of the county, state, city, zip, country
            loc = Location(None, None, None, None, None)
            if field is None and value is None:
                query = f"select * from Doctor"
                return self.get_cursor.execute(query).fetchall()
            elif field.lower() in ("firstname", "lastname", "specialization"):
                query = f"select * from Doctor where {field} like ?"
                return self.get_cursor.execute(query, (value + '%',)).fetchall()
            elif field.lower() == "county":
                loc = loc.fetch(county=value, city=None, state=None, country=None, zipcode=None)
                loc_ids = [location[0] for location in loc]
                if loc_ids:
                    placeholders = ', '.join('?' for _ in loc_ids)
                    query = f"select * from Doctor where location_id in ({placeholders})"
                    return self.get_cursor.execute(query, loc_ids).fetchall()
            elif field.lower() == "city":
                loc = loc.fetch(county=None, city=value, state=None, country=None, zipcode=None)
                loc_ids = [location[0] for location in loc]
                if loc_ids:
                    placeholders = ', '.join('?' for _ in loc_ids)
                    query = f"select * from Doctor where location_id in ({placeholders})"
                    return self.get_cursor.execute(query, loc_ids).fetchall()
            elif field.lower() == "state":
                loc = loc.fetch(county=None, city=None, state=value, country=None, zipcode=None)
                loc_ids = [location[0] for location in loc]
                if loc_ids:
                    placeholders = ', '.join('?' for _ in loc_ids)
                    query = f"select * from Doctor where location_id in ({placeholders})"
                    return self.get_cursor.execute(query, loc_ids).fetchall()
            elif field.lower() == "country":
                loc = loc.fetch(county=None, city=None, state=None, country=value, zipcode=None)
                loc_ids = [location[0] for location in loc]
                if loc_ids:
                    placeholders = ', '.join('?' for _ in loc_ids)
                    query = f"select * from Doctor where location_id in ({placeholders})"
                    return self.get_cursor.execute(query, loc_ids).fetchall()
            elif field.lower() == "zipcode":
                loc = loc.fetch(county=None, city=None, state=None, country=None, zipcode=value)
                loc_ids = [location[0] for location in loc]
                if loc_ids:
                    placeholders = ', '.join('?' for _ in loc_ids)
                    query = f"select * from Doctor where location_id in ({placeholders})"
                    return self.get_cursor.execute(query, loc_ids).fetchall()

        except Exception as e:
            print("An error has occurred: " + str(e))


    def update_doctor(self, doctor_id, parameter_to_update, value):

        try:
            if parameter_to_update not in self._allowed_column_names:
                raise ValueError(f"Invalid column name: {parameter_to_update}")
            self._cursor.execute(f"update Doctor set {parameter_to_update} = ? where doctor_id = ?", (value, doctor_id))
            self._conn.commit()
            print("Patient record updated successfully!")
        except Exception as e:
            print("An error has occurred: " + str(e))

    def delete_doctor(self, doctor_id):
        try:
            self._cursor.execute("delete from Doctor where doctor_id = ?", (doctor_id,))
            self._conn.commit()
            print(f"Deleted the patient with patient_id: {doctor_id} successfully!")
        except Exception as e:
            print("An error has occurred: " + str(e))

    # firstName, lastname, gender, email_id, phone_number, date_of_birth,specialization
    def reset_database(self):
        try:
            # To be called only once
            # print("Here")

            sql = """
            DROP TABLE IF EXISTS Doctor;

            CREATE TABLE Doctor(
            doctor_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            firstName TEXT,
            lastname TEXT,
            gender TEXT,
            email_id TEXT,
            phone_number TEXT,
            date_of_birth DATE,
            specialization TEXT,
            location_id INTEGER NOT NULL,
            FOREIGN KEY (location_id) REFERENCES Locations(location_id)
            );
            """
            self.execute_script(sql)

        except Exception as e:
            print("An error occurred" + e)
        finally:
            super().close_db()

