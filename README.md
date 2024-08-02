# Mental Health Support API

## Introduction

This API provides an automated mental health support system that aims to assist users facing mental health issues. It combines the power of Large Language Models (LLMs) and machine learning to offer conversational responses, relevant article suggestions, and sentiment analysis of movie reviews.

## Requirements

- Python 3.x
- FastAPI
- Pydantic
- dotenv
- google.generativeai
- joblib
- uvicorn

## Installation and Setup

Follow these steps to install and set up the Mental Health Support API:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/mental-health-support-api.git
   ```

2. Navigate to the project directory:
   ```
   cd mental-health-support-api
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv env
   ```

   Then, activate the virtual environment:
   ```
   source env/bin/activate  # On Windows
   source env/bin/activate  # On macOS and Linux
   ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Set up your environment variables:
   Create a `.env` file in the root directory and add your Google Cloud API key:
   ```
   GOOGLE_API_KEY=your_api_key
   ```

6. Start the API server:
   ```
   uvicorn main:app --reload
   ```

   The `--reload` flag automatically restarts the server when changes are detected in the code.

## API Endpoints

### Mental Health Support Endpoint (`/rag`)

This endpoint utilizes the Gemini chat model from Google Cloud to generate conversational responses and provide relevant article suggestions based on the user's query.

#### Request Format

```json
{
  "question": "How can I manage my anxiety?"
}
```

#### Response Format

```json
{
  "responses": [
    "Here are some strategies to manage your anxiety...",
    "Remember to practice deep breathing and relaxation techniques.",
    "Consider seeking professional help if your anxiety is impacting your daily life."
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

### Sentiment Analysis Endpoint (`/classification`)

This endpoint performs sentiment analysis on movie reviews using a pre-trained machine learning model.

#### Request Format

```json
{
  "text": "I loved the movie! It was captivating from start to finish."
}
```

#### Response Format

```json
{
  "predicted_sentiment": "positive"
}
```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## Credits

This project was made possible by the contributions of the open-source community. A special thanks to the developers of FastAPI, Pydantic, and Google Cloud AI for providing the tools and models used in this API.
