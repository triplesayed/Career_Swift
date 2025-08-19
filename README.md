# Job Board Web Application

## Overview
This is a web application designed to serve as a job board platform where both employers and job seekers can interact. It allows users to register, create profiles, post job listings, apply for jobs, and manage their accounts.


## Features
- User Authentication:
  - Users can register for an account and log in as either Employers or Job Seekers.
- Job Listings:
  - Employers can create job listings with detailed information such as title, description, requirements, and location.
- Job Details:
  - Users can view detailed information about job listings and apply by uploading resumes and providing necessary information.
- User Dashboard:
  - Employers can manage their posted job listings, view applications, and update job details.
  - Job seekers can track their applications and update their profiles.
- Job Categories:
  - Jobs are categorized based on industries to facilitate easy navigation for users.
- Email Notifications:
  - Users receive email notifications upon successful job applications or when an employer receives a new application.
- CRUD Operations:
  - Create, Read, Update, and Delete operations are supported for both job listings and user profiles.
- Deployment
  - This project is deployed on Onrender Pages for easy access- https://careerswift.onrender.com/

## Getting Started
1. **Clone this repository:**
   ```bash
    https://github.com/Sayed161/CareerSwift.git 
**To run this project locally, follow these steps:**

2. **Navigate to the project directory: `cd your-repository`**

3. **Install dependencies:**
   ```bash
       pip install -r requirements.txt
4. **Apply migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
5. **Start the development server:**
    ```bash
    python manage.py runserver
6. **Open your browser and visit `http://127.0.0.1:8000/` to view the application.**


## Technologies Used
- Frontend: HTML, CSS
- Backend: Django
- Database: Sqlite3 (or other supported databases)
- Authentication: Django authentication system
- Email Notifications: Django's built-in email functionality
- Hosting:Onrender
