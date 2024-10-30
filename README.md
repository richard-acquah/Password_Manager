# Project Title: Password Manager
#### Video Demo: https://youtu.be/U_aFn99I4mw

## Description

The Password Manager project provides a secure, user-friendly web application designed for storing, retrieving, and managing user credentials (such as usernames and passwords) for various services. The application emphasizes security and user experience, implementing features like hover effects, responsive animations, and a database backend for efficient data management.

### Key Features

1. **Service-Specific Password Management**: Users can add, retrieve, and manage credentials for multiple services within a single, centralized application.
2. **Interactive UI/UX Design**: The user interface incorporates animations and hover effects, providing a dynamic, responsive experience.
3. **SQLite3 Database Integration**: All data is securely stored in a local SQLite3 database, ensuring persistent storage and retrieval of sensitive information.

This document outlines the structure, functionality, and purpose of each file in the project, offering a comprehensive overview of its components and their roles.

## Project Files

### 1. `app.py`

This file is the core backend of the application, built using the Flask framework. It manages the routing and processing of requests, interacting with the SQLite3 database to save and retrieve user credentials. Key routes and functions include:

- **Index Route (`/`)**: The home page displays general information and navigation links.
- **Add Password Route (`/add_passwd`)**: Enables users to add new credentials for a service.
- **Retrieve Password Route (`/retrieve`)**: Allows users to retrieve credentials for a specified service.

This file ensures that user inputs are securely processed and stored in the database.

### 2. `templates/base.html`

The `base.html` file serves as the main template that provides a shared layout structure for all pages in the application. This layout includes:

- A **header** with the application title and navigation links to different pages.
- A **footer** that displays attribution information and a brief project description.

The `base.html` template uses Jinja templating to incorporate dynamic content supplied by other templates or the application’s backend.

### 3. `templates/index.html`

The homepage content template is extended from `base.html`. It introduces users to the application’s purpose and offers guidance on using the tool for effective password management. This page highlights the importance of cybersecurity and best practices for password management.

### 4. `templates/add_password.html`

The `add_password.html` template presents a form allowing users to securely input credentials for various services. This page prompts users to enter the following details:

- **Service Name**: Name of the application or website.
- **Username**: Username associated with the service.
- **Password**: Password for the service.

Upon submission, the details are sent to the backend (`app.py`), where they are saved to the SQLite3 database.

### 5. `templates/retrieve_password.html`

This template enables users to retrieve credentials by entering the name of a service. If the service is found in the database, the application displays the username and password associated with it. If no matching record is found, a message is shown indicating that the service was not found.

### 6. `static/styles.css`

The `styles.css` file contains all the styling for the application, giving it a modern and clean appearance. Key styling elements include:

- **Body Styling**: A centered, fixed background image with general font styling applied throughout the app.
- **Text Animation**: An animation effect applied to the main text on the homepage for a subtle, fade-in effect, providing a more dynamic user experience.
- **Form Styling**: All form inputs and buttons are styled with rounded corners and padding for usability and aesthetics.
- **Hover Effects**: Adds an interactive scaling effect to various buttons and navigation links, improving the user experience.

### 7. `static/script.js`

The `script.js` file is a client-side JavaScript script that enhances the user experience by adding interactive effects. When the user hovers over the main centered text, it subtly scales up, creating an interactive visual effect. The code leverages the `DOMContentLoaded` event listener to ensure it only runs once the DOM is fully loaded, preventing potential timing issues.

### 8. SQLite Database (`password_manager.db`)

This SQLite3 database file securely stores all user credentials. The database schema includes fields for each service’s name, username, and password. It ensures that user data persists across sessions and can be retrieved when needed.


## Project Workflow

The workflow of this application is straightforward and user-friendly:

1. **Adding a Password**: Users navigate to the "Add Password" page, enter their service credentials, and submit. The backend validates and stores the data in the SQLite3 database.
2. **Retrieving a Password**: Users can retrieve previously saved credentials by entering the service name on the "Retrieve Password" page. If found, the credentials are displayed on the screen.

## Security and Limitations

While this project is a basic password management solution, it does not employ encryption for passwords or utilize advanced security features. Future enhancements could include:

- **Encryption** of passwords before storage.
- **User Authentication**: Adding user login to limit database access.
- **Secure HTTPS Connection**: Implementing SSL/TLS encryption for data transfer.

---

## Conclusion

This Password Manager project is an essential tool for safely storing and accessing user credentials. Its user-friendly interface, efficient SQLite3 database backend, and basic animations make it both practical and engaging. Though basic, the project provides a strong foundation for building a more advanced password management system.

