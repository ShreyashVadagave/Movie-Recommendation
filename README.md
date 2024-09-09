# Movie Recommendation System

## Overview

This project is a full-stack movie recommendation system that utilizes machine learning to provide personalized movie suggestions. The backend is developed in Python using a machine learning model, while the frontend is built with Streamlit, allowing for an interactive user experience. Users can select a movie and receive recommendations based on their choice.

## Project Structure

```
movie_recommendation_system/
│
├── backend/
│   ├── app.py                # Streamlit app to serve the recommendation
│   ├── model.py              # Python script for the ML model
│   ├── movies.csv            # Dataset containing movie information
│   └── recommendation.pkl     # Saved model using pickle
│
└── frontend/
    ├── templates/
    │   └── index.html        # HTML file for Flask frontend (if needed)
    ├── static/
    │   ├── css/              # CSS files for styling
    │   └── js/               # JavaScript files for interactivity
    └── app.py                # Flask server for frontend (if needed)
```

## Features

- **Machine Learning Model**: Utilizes cosine similarity to recommend movies based on user input.
- **Interactive Web Interface**: Built with Streamlit, allowing users to select a movie and view recommendations instantly.
- **Data Handling**: The dataset includes movie titles, genres, and overviews, which are used for generating recommendations.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/movie_recommendation_system.git
   cd movie_recommendation_system
   ```

2. **Install the required packages**:

   ```bash
   pip install pandas scikit-learn streamlit
   ```

3. **Run the backend application**:

   Navigate to the `backend` directory and run:

   ```bash
   streamlit run app.py
   ```

4. **Access the application**:

   Open your web browser and go to `http://localhost:8501` to interact with the movie recommendation system.

## Usage

- Select a movie from the dropdown menu.
- Click the "Recommend" button to view a list of recommended movies based on your selection.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional features, please create a pull request or open an issue.

