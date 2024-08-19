# Project Status
The model has issued some error it will be committed to later date 


# Music Recommendation System

This project is a comprehensive music recommendation system developed using machine learning algorithms and integrated into a Django web application. The system recommends music to users based on their preferences, utilizing both Content-Based Filtering and Matrix Factorization techniques.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Data](#data)
- [Machine Learning Algorithms](#machine-learning-algorithms)
- [Django Web Application](#django-web-application)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Music Recommendation System aims to enhance user experience by providing personalized music recommendations. It leverages machine learning techniques to analyze a user's listening history and preferences, then suggests tracks that align with their tastes. This project includes data processing, feature engineering, model building, and a fully functional web application using the Django framework.

## Features

- **Personalized Recommendations**: Generates music recommendations tailored to individual user preferences.
- **User Registration & Login**: Secure user authentication and account management.
- **Content-Based Filtering**: Recommends songs similar to those a user has previously liked or listened to.
- **Matrix Factorization**: Utilizes collaborative filtering to identify patterns in user interactions and suggest new music.
- **Django Integration**: User-friendly web interface for interacting with the recommendation system.

## Tech Stack

- **Programming Language**: Python
- **Framework**: Django
- **Machine Learning Libraries**: Scikit-learn, Pandas, NumPy
- **Database**: SQLite (can be configured to use other databases like PostgreSQL)
- **Frontend**: HTML, CSS, JavaScript

## Data

The system uses a subset of the Spotify Million dataset, which contains rich metadata about various songs and user interactions.

- **Data Source**: Spotify Million Dataset
- **Feature Engineering**: Relevant features were extracted and selected to optimize the recommendation process. Techniques such as normalization, scaling, and dimensionality reduction were applied to enhance model performance.

## Machine Learning Algorithms

- **Content-Based Filtering**: This algorithm recommends tracks based on the characteristics of the songs the user has previously enjoyed. It considers features like genre, artist, tempo, and more.
  
- **Matrix Factorization**: A collaborative filtering technique that decomposes the user-item interaction matrix into lower-dimensional matrices. It helps in discovering latent factors that influence user preferences and generates recommendations based on these factors.

## Django Web Application

The web application was built using the Django framework and includes the following functionalities:

- **User Registration & Login**: Allows users to create accounts and securely log in to access personalized features.
- **Music Recommendations**: Displays a list of recommended tracks based on the user's listening history and preferences.
- **User Interface**: A clean and intuitive interface that provides easy access to the recommendation system.

## Installation

### Prerequisites

- Python 3.x
- Django
- Scikit-learn
- Pandas
- NumPy

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/music-recommendation-system.git
   cd music-recommendation-system
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:

   ```bash
   python manage.py migrate
   ```

5. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Usage

- **Sign Up/Login**: Create an account or log in to access personalized recommendations.
- **Receive Recommendations**: Once logged in, you will receive music recommendations based on your listening history and preferences.
- **Explore & Enjoy**: Browse through the recommended tracks and discover new music tailored to your tastes.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue to suggest improvements or report bugs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This README should provide a clear and comprehensive overview of your project, making it easy for others to understand and use your music recommendation system.
