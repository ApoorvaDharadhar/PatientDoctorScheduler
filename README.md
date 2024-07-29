# Patient Doctor Scheduler using Python and SQLite

The Scheduler application provides a comprehensive solution for managing patients, doctors, and appointments. It allows users to add, update, delete, and fetch records for both patients and doctors, ensuring efficient management of medical data.

## Features

- **CRUD Operations**: Add, update, delete, and fetch records for patients and doctors.
- **Appointment Scheduling**: Schedule, update, and cancel appointments, ensuring the selected time is within working hours and avoiding overbooking. If the selected time slot is already taken, users are prompted to choose a different time.
- **Search Functionality**: Search for doctors based on various filters, including county, state, city, zip code, and country, making it easier to find the right medical professional based on location. 
- **Dynamic Location Management**: When adding a new doctor and specifying a location (county, state, city, zip) that does not exist in the database, the system prompts users to decide whether to add a new record to the locations table.

## Database Structure

The project’s database is structured around four main tables:
- **Location**
- **Doctor**
- **Patient**
- **Appointment**

SQLite was used to manage the database.

## Additional Functionalities

- **Versatile Appointment Search**: Fetch appointments by Doctor_ID, Patient_ID, view all appointments, or exit the search menu.
- **Appointment Status Updates**: Reflect changes such as "Appointment Date Updated" or "Appointment Time Updated."
- **Note Management**: Add or update notes about patients and appointments.
- **Name-Based Searches**: Look up names using patient_id, patient_first_name, patient_last_name, and similarly for doctors. Supports searches for records starting with a specific letter.
- **CSV Import**: Import location data from CSV files, streamlining the process of updating location information in the database.

By integrating these features, the Scheduler application offers a robust tool for managing healthcare-related data and appointments, enhancing operational efficiency and data accuracy.
