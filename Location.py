import DBase as db


class Location(db.DBase):

    _county = None
    _state = None
    _city = None
    _zip = None
    _country = None

    def __init__(self, _county, _state, _city, _zip, _country):
        super().__init__("PatientDoctorScheduler.sqlite")
        self._county = _county
        self._state = _state
        self._city = _city
        self._zip = _zip
        self._country = _country


    def reset_database(self):
        try:
            # To be called only once.
            sql = """
            drop table if exists Location;

            create table Location(
                location_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                county TEXT,
                state TEXT,
                city TEXT,
                zip INTEGER,
                country TEXT
            )
            """
            self.execute_script(sql)
        except Exception as e:
            print("An error occurred: " + str(e))
        finally:
            self.close_db()

    def add_location(self):
        try:
            # Add the location
            self.get_cursor.execute("""
                insert or ignore into Location (county, state, city, zip, country)
                VALUES (?, ?, ?, ?, ?)""", (
            self._county, self._state, self._city, self._zip, self._country))
            self.get_connection.commit()
            return "Location added successfully!"
        except Exception as e:
            print("An error has occurred: " + str(e))

    def fetch(self, county=None, city=None, state=None, country =None, zipcode=None):
        try:
            # Fetch the data using county, city, state, country, zipcode
            if county != None:
                return self.get_cursor.execute("select * from Location where county = ?", (county,)).fetchall()
            elif city !=None:
                return self.get_cursor.execute("select * from Location where city = ?", (city,)).fetchall()
            elif state !=None:
                return self.get_cursor.execute("select * from Location where state = ?", (state,)).fetchall()
            elif country !=None:
                return self.get_cursor.execute("select * from Location where country = ?", (country,)).fetchall()
            elif zipcode !=None:
                return self.get_cursor.execute("select * from Location where zip = ?", (zipcode,)).fetchall()
            else:
                return self.get_cursor.execute("select * from Location").fetchall()
        except Exception as e:
            print("An error has occurred: " + str(e))

    def fetch_by_all(self, county, city, state, zip, country):
        if county is not None and city is not None and state is not None and zip is not None and country is not None:

            return self.get_cursor.execute("select location_id from Location where county =? and city=? and state =? and country=? and zip =?;", (county,city,state,country,int(zip))).fetchone()


loc = Location(None, None, None , None, None)


