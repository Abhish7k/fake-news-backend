# Fake News Detection

Fake News Detection is a web application built with Flask that aims to classify news articles as either real or fake using machine learning techniques.

## Installation

To run the Fake News Detection application locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fake-news-detection.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fake-news-detection
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once you have installed the dependencies, you can run the Flask application using the following command:

```bash
python app.py
```

This will start the server locally, and you can access the application in your web browser at http://127.0.0.1:5000.

## API Endpoint

The Fake News Detection application provides a simple API endpoint for classifying news articles. You can send a POST request to /detect with a JSON payload containing the news article text, and the API will return whether the article is classified as "Fake" or "Real".

Example:

```bash
curl -X POST http://127.0.0.1:5000/detect -H "Content-Type: application/json" -d '{"article": "This is a fake news article."}'
```

Response:

```json
{
  "result": "Fake"
}
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

