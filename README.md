Certainly! Here is the complete `README.md` file in a single markdown format:

```markdown
# Mental Health Support and Sentiment Analysis API

This FastAPI project provides two main functionalities: mental health support through article recommendations and sentiment analysis of movie reviews using a machine learning model.

## Table of Contents

- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Endpoints](#endpoints)
  - [/rag](#rag)
  - [/classification](#classification)
- [Running the Application](#running-the-application)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/mental-health-support-sentiment-analysis.git
   cd mental-health-support-sentiment-analysis
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables

Create a `.env` file in the root directory of your project and add your Google API key:

```
GOOGLE_API_KEY=your_google_api_key
```

## Endpoints

### /rag

Provides mental health support by recommending relevant articles.

- **URL**: `/rag`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "question": "I am feeling anxious, what should I do?"
  }
  ```
- **Response**:
  ```json
  {
    "responses": [
      "response_from_gemini_model"
    ],
    "articles": [
      {
        "title": "Understanding Anxiety",
        "url": "https://newsinhealth.nih.gov/2016/03/understanding-anxiety-disorders",
        "summary": "A comprehensive guide on anxiety disorders."
      },
      {
        "title": "Coping with Depression",
        "url": "https://www.helpguide.org/articles/depression/coping-with-depression.htm",
        "summary": "Effective strategies for dealing with depression."
      }
    ]
  }
  ```

### /classification

Classifies the sentiment of a given movie review.

- **URL**: `/classification`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "text": "The movie was fantastic and thrilling!"
  }
  ```
- **Response**:
  ```json
  {
    "predicted_sentiment": "positive"
  }
  ```

## Running the Application

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

The application will be available at `http://localhost:8000`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Make sure to replace `your-username` with your actual GitHub username if you are uploading this to your GitHub repository. Additionally, ensure that you have a `requirements.txt` file listing all the dependencies required for your project.
