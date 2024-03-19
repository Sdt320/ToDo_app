

# Todo App with Django

This is a simple Todo application built using Django. It allows users to create, update, and delete tasks, as well as mark them as completed.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/todo-app-django.git
    ```

2. Navigate into the project directory:

    ```bash
    cd todo-app-django
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply the migrations:

    ```bash
    python manage.py migrate
    ```

7. Run the development server:

    ```bash
    python manage.py runserver
    ```

8. Access the application at [http://localhost:8000](http://localhost:8000) in your web browser.

## Usage

- Visit the homepage to view all tasks.
- To create a new task, click on the "Add Task" button and fill in the details.
- To edit a task, click on the task name and update the information.
- To mark a task as completed, click on the checkbox beside the task.
- To delete a task, click on the trash icon next to the task.

## Contributing

Contributions are welcome! If you have any ideas, enhancements, or bug fixes, feel free to open an issue or create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
