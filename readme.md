# Travel Planner with Vertex AI API Integration

This is a Travel Planner web application that utilizes Google Cloud's Vertex AI API to generate itineraries and provide destination search results based on user input. Users can sign up, log in, and access personalized dashboards to manage their itineraries. The application also provides an interactive map, reviews and ratings for destinations, and social sharing options.

## Overview

The Travel Planner web application is designed to help users plan their trips by generating custom itineraries for selected destinations. It also allows users to search for destinations based on keywords and retrieve relevant search results.

## Features

- Destination Search: Users can search for travel destinations based on keywords using the Vertex AI API's text search functionality.
- Itinerary Generation: Users can input their desired destination and the number of days they want to travel. The application will use the Vertex AI API's chat prompt functionality to generate a custom itinerary for the specified trip.
- User Authentication: The web application supports user registration and login features to save itineraries for future reference.
- Dashboard: Authenticated users can view their saved itineraries on the dashboard.

## Technologies Used

- Flask: The web application is built using the Flask web framework in Python.
- Firebase: User authentication and data storage are managed using Firebase's Firestore and Authentication services.
- Vertex AI API: The application integrates with Google Cloud's Vertex AI API to perform destination search and itinerary generation using the PaLM (Predictive Language Model) capabilities.
- HTML and CSS: The user interface is designed using HTML and CSS for a simple and visually appealing experience.

## Getting Started

### Prerequisites

- Python 3.x
- Google Cloud account with Vertex AI API enabled.
- Firebase account for authentication and data storage.

### Installation

1. Clone the repository and navigate to the project directory.

2. Set up a virtual environment (optional but recommended).

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Set up Firebase credentials for authentication and Firestore access. Save the service account key JSON file as `serviceAccountKey.json` in the project root directory.

5. Set up Google Cloud credentials for accessing the Vertex AI API. Make sure you have the necessary permissions and save the credentials as `google-credentials.json`[service_account.json] in the project root directory.


## Project Structure

The project follows a standard Flask project structure:

```
Travel Planner/
|-- app.py
|-- templates/
|   |-- landing_page.html
|   |-- itinerary.html
|   |-- dashboard.html
|   |-- signup.html
|   |-- login.html
|-- static/
|-- serviceAccountKey.json
|-- service_account.json
|-- README.md
```

### Running the Application

To run the Travel Planner web application, use the following command:

```bash
python app.py
```

The application will be available at `http://localhost:5000/` in your web browser.

## Usage

1. **Landing Page**: The home page of the application displays the search bar for destination search and an option to log in or sign up.

2. **Destination Search**: Enter a keyword in the search bar to find travel destinations. The Vertex AI API's text search functionality will retrieve relevant results.

3. **Itinerary Generation**: After selecting a destination, specify the number of days for your trip. The application will use the Vertex AI API's chat prompt functionality to generate a custom itinerary.

4. **User Authentication**: To save generated itineraries, users need to log in or sign up. Their saved itineraries will be accessible from the dashboard.

**TODO**

1. **User Dashboard:** A personalized dashboard is provided where users can view their saved itineraries and favorite spots.

2. **Interactive Map:** The application shows destinations, landmarks, and planned activities on an interactive map for better visualization.

3. **Reviews and Ratings:** Users can leave reviews and ratings for destinations and activities they have visited.

4. **Social Sharing:** Social media sharing options are implemented for users to share their planned trips with friends and family.

## API Usage

The application uses the VertexAI module for destination search and itinerary generation. The `get_search_results` and `get_itinerary` functions from the VertexAI module are integrated into the Flask application to handle destination search and itinerary generation.

## User Authentication and Data Storage

User authentication is implemented using Firebase Authentication. User data, including itineraries, is stored in Firestore, a NoSQL database provided by Firebase.
