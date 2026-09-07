# Movie Recommendation System

A content-based movie recommendation system built using Python, Scikit-learn, FastAPI, Streamlit, and the TMDB API.

The system recommends movies based on the similarity between movie content such as genres, keywords, overview, and tagline.

## Features

- Content-based movie recommendations
- Movie search
- TF-IDF based text vectorization
- Cosine similarity for finding similar movies
- FastAPI backend
- Streamlit web interface
- TMDB API integration for movie information
- Deployed backend and frontend

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- FastAPI
- Streamlit
- TMDB API
- Git
- GitHub

## How It Works

The recommendation system uses a content-based filtering approach.

### 1. Data Processing

Movie information is loaded from the movie dataset and the required data is cleaned.

The following movie information is used for creating movie tags:

- Overview
- Genres
- Keywords
- Tagline

### 2. Text Preprocessing

The movie text is processed using:

- Lowercasing
- Punctuation removal
- Stopword removal
- Lemmatization

### 3. TF-IDF Vectorization

The processed movie tags are converted into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency).

### 4. Cosine Similarity

Cosine similarity is used to compare the vector of a selected movie with the vectors of other movies.

The movies with the highest similarity scores are returned as recommendations.

### 5. FastAPI Backend

FastAPI is used to create the backend API.

The backend handles movie searches, recommendations, and communication with the TMDB API.

### 6. Streamlit Frontend

Streamlit is used to create the web interface through which users can search for movies and receive recommendations.

### 7. TMDB API

The TMDB API is used to retrieve additional movie information such as posters, ratings, release dates, and other movie details.

## Project Structure

    movie-recommendetion/
    |
    |-- app.py
    |-- main.py
    |-- movies_metadata.csv
    |
    |-- df.pkl
    |-- indices.pkl
    |-- tfidf.pkl
    |-- tfidf_matrix.pkl
    |
    |-- requirements.txt
    |-- .gitignore
    |-- .python-version

### File Description

`app.py`  
Streamlit frontend of the application.

`main.py`  
FastAPI backend containing API endpoints and recommendation logic.

`movies_metadata.csv`  
Movie dataset used by the recommendation system.

`df.pkl`  
Saved processed movie dataframe.

`indices.pkl`  
Saved mapping between movie titles and dataframe indices.

`tfidf.pkl`  
Saved TF-IDF vectorizer.

`tfidf_matrix.pkl`  
Saved TF-IDF matrix containing numerical representations of movie tags.

`requirements.txt`  
Contains the Python dependencies required to run the project.

## Running the Project Locally

### 1. Clone the Repository

    git clone https://github.com/1682003/movie-recommendetion.git

    cd movie-recommendetion

### 2. Create a Virtual Environment

    python -m venv .venv

### 3. Activate the Virtual Environment

For Windows:

    .venv\Scripts\Activate.ps1

### 4. Install Dependencies

    pip install -r requirements.txt

### 5. Configure TMDB API

Create a `.env` file in the project root directory and add your TMDB API key:

    TMDB_API_KEY=your_tmdb_api_key

Do not commit the `.env` file to GitHub.

### 6. Start the FastAPI Backend

    uvicorn main:app --reload

The backend will run at:

    http://127.0.0.1:8000

FastAPI documentation is available at:

    http://127.0.0.1:8000/docs

### 7. Start the Streamlit Frontend

Open another terminal and run:

    streamlit run app.py

The Streamlit application will open in your browser.

## Project Architecture

    User
      |
      v
    Streamlit Frontend
    app.py
      |
      | HTTP Requests
      v
    FastAPI Backend
    main.py
      |
      +----------------------+
      |                      |
      v                      v
    Recommendation Engine    TMDB API
      |
      v
    TF-IDF
      |
      v
    Cosine Similarity
      |
      v
    Recommended Movies

## Deployment

The project is deployed using two separate services:

- FastAPI backend deployed on Render
- Streamlit frontend deployed on Streamlit Cloud

## Future Improvements

- Improve recommendation quality using additional movie features
- Add collaborative filtering
- Add personalized recommendations
- Add user authentication
- Add watchlist functionality
- Improve the user interface
- Implement more advanced recommendation techniques

## Author

Anuj Mulha Tamrakar

GitHub: https://github.com/1682003
