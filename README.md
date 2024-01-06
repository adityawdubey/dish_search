# Django Search Application

This Django application allows users to search for dishes based on their names. It uses a file-based SQLite database to store and retrieve dish information.

<img width="1438" alt="Screenshot 2024-01-06 at 11 22 45 PM" src="https://github.com/adityawdubey/dish_search/assets/88245579/dc135a33-8f18-4e84-b8d3-f0acc2986bfa">
<img width="1438" alt="Screenshot 2024-01-06 at 11 23 01 PM" src="https://github.com/adityawdubey/dish_search/assets/88245579/7fc84bee-aa0c-42f8-ab78-b23f410bd222">


## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/adityawdubey/dish_search.git
   cd django-search-app


2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate
    # On Windows, use venv\Scripts\activate

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    
4. Apply database migrations:

    ```bash
    python manage.py migrate

5. Import sample data from the CSV file:

    ```bash
    python import_data.py
    
6. Run the development server:

    ```bash
    python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/dish_search/search/ to access the search application.

### Usage
Enter a search query in the search bar and press "Search" to find dishes based on their names.
Explore the search results.

### Features
Responsive UI: The application provides a responsive user interface for a seamless experience on various devices.

CSS Styling: The search form and results are styled using CSS for a visually appealing look.


### To be Implemented

❏ Advanced Search Features:

  Enhance the search functionality by implementing advanced features such as autocomplete, filtering, or sorting options.
  Use Django's built-in search capabilities or integrate third-party search libraries for improved search performance.

❏ Pagination:

  Implement pagination for the search results to improve the user experience, especially if there are many results.

### Fork the repository.
Create a new branch for your feature: git checkout -b feature-name.

Implement your feature and commit changes: git commit -m "Add feature".

Push your branch to your fork: git push origin feature-name.

Open a pull request on GitHub.


