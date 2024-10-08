# student-records-management-system

## A CRUD Student Records Management System built with Django ... SSR

The Student Records Management System is an application built with Django, designed for administrative processes associated with managing student information. This system provides comprehensive support for Create, Read, Update, and Delete (CRUD) operations, offering administrators an efficient means to add, retrieve, modify, and remove student records. The system simplifies the tasks associated with handling student data.

## Table of Contents

- [student-records-management-system](#student-records-management-system)
  - [A CRUD Student Records Management System built with Django](#a-crud-student-records-management-system-built-with-django)
  - [Table of Contents](#table-of-contents)
  - [Screenshots](#screenshots)
    - [Home](#home)
    - [Create Student Record](#create-student-record)
    - [Read Student Record](#read-student-record)
    - [Update Student Record](#update-student-record)
    - [Delete Student Record](#delete-student-record)
  - [Installation](#installation)
  - [Database Setup](#database-setup)
  - [Usage](#usage)
    - [URL Views](#url-views)
      - [Homepage](#homepage)
      - [Add Student](#add-student)
      - [More...](#more)

## Screenshots

### Home
![Homepage](https://github.com/mujeeb-gh/student-records-management-system/blob/master/docs/images/homepage.png)

### Create Student Record
![Create Student Page](https://github.com/mujeeb-gh/student-records-management-system/blob/master/docs/images/add_student.png)

### Read Student Record
![Read Student Page](https://github.com/mujeeb-gh/student-records-management-system/blob/master/docs/images/read_student.png)

### Update Student Record
![Update Student Page](https://github.com/mujeeb-gh/student-records-management-system/blob/master/docs/images/edit_student.png)

### Delete Student Record
![Delete Student Page](https://github.com/mujeeb-gh/student-records-management-system/blob/master/docs/images/delete_student.png)


## Installation

1. Clone the repository.
   ```bash
   git clone https://github.com/mujeeb-gh/student-records-management-system.git

2. Navigate to the project directory
   ```bash
   cd student-records-management-system
   
3. Create a virtual environment
   ```bash
   python -m venv venv

4. Activate the virtual environmrnt
   ```bash
   .\venv\Scripts\activate # On Windows

   source venv/bin/activate # On Unix or MacOS

5. Install dependencies using the requirements.txt file:
   ```bash
   pip install -r requirements.txt

## Database Setup
1. Navigate to django project directory
   ```bash
   cd student_records


2. Make database Migrations
    ```bash
    python manage.py makemigrations
    python manage.py migrate

## Usage
1. Start the development server.
   ```bash
   python manage.py runserver

2. Open the development server URL in your web browser e.g (http://127.0.0.1:8000).

### URL Views

#### Homepage

- **URL:** `/records/homepage/`
- **Description:** Displays the homepage of the Student Records Management System.
- **Usage:** Access the main page to navigate to other sections of the system.

#### Add Student

- **URL:** `/records/add/`
- **Description:** Allows users to add a new student to the system.
- **Usage:** Fill in the student details and submit the form.

#### More...
