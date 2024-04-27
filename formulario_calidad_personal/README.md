# Project Name

This is the README file for the project "formulario_calidad_personal".

## Description

This project is a Django web application that includes a login functionality using Cognito from AWS. It also features a form where users can input data, which is then stored in a SQL database.

## Project Structure

The project has the following directory structure:

```
mi-proyecto
├── mi_proyecto
|   ├── __init__.py
|   ├── settings.py
|   ├── urls.py
|   └── wsgi.py
├── app
|   ├── migrations
|   |   └── __init__.py
|   ├── admin.py
|   ├── apps.py
|   ├── forms.py
|   ├── models.py
|   ├── tests.py
|   ├── views.py
|   └── templates
|       ├── login.html
|       └── form.html
├── manage.py
├── db.sqlite3
├── .env
├── requirements.txt
└── README.md
```

## Installation and Setup

To run this project locally, follow these steps:

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the project dependencies by running `pip install -r requirements.txt`.
4. Set up the database by running `python manage.py migrate`.
5. Start the development server with `python manage.py runserver`.
6. Access the application in your browser at `http://localhost:8000`.

## Usage

- To access the login page, go to `/login` in your browser.
- To access the form page, go to `/form` in your browser.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or questions, please contact [email protected]

---

Feel free to modify this README file to fit your project's specific details and requirements.
