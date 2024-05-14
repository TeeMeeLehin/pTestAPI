# Psychometric Test Web App

This is a Django web application for conducting psychometric tests to suggest courses and career pathways for learners.

## Features

- Conduct psychometric tests to suggest courses and career pathways.
- Collect user responses for personality, digital literacy, and user interests.
- Generate test results based on user responses.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/TeeMeeLehin/pTestAPI.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run migrations:

    ```bash
    python manage.py migrate
    ```

4. Start the development server:

    ```bash
    python manage.py runserver
    ```

## Usage

### 1. Conduct Psychometric Tests

- Access the personality test questions at `/api/pq/`.
- Access the digital literacy test questions at `/api/dq/`.
- Access the user-interests options at `/api/interests/`.

### 2. Submit Test Responses

- Use the API endpoints `/api/pq-submit/`, `/api/dq-submit/`, and `/api/inte-submit/` to submit test responses.

### 3. View Test Results

- Access the test results at `/api/results/`.

## API Documentation

- Swagger UI documentation for the API endpoints is available at `/api/docs/`.
