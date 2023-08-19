# Heart Attack Prediction

This repository contains code for a heart attack prediction application using Streamlit and FastAPI. The application allows users to input various parameters related to heart health and receive a prediction on the probability of experiencing a heart attack.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:

```git
git clone https://github.com/
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv env
```

- On Windows:

```bash
env\Scripts\activate
```

- On macOS and Linux:

```bash
source env/bin/activate
```

Note: Using a virtual environment is optional but recommended to isolate project dependencies.

3. Install the required Python libraries:

```git
pip install -r requirements.txt
```

## Usage

### FastAPI Server

1. Start the FastAPI server by running the following command:

```bash
uvicorn fastapi_app:app --reload
```

The server will start running at `http://localhost:8000`.

### Streamlit App

1. Open a new terminal and navigate to the project directory.

2. Start the Streamlit app by running the following command:

```bash
streamlit run streamlit_app.py
```

The Streamlit app will open in your default web browser.

3. In the Streamlit app, enter the required information such as age, sex, chest pain type, and other parameters related to heart health.

4. Click the "Predict" button to send the data to the FastAPI server for prediction.

5. The predicted probability of a heart attack will be displayed on the Streamlit app.

## Project Structure

- `fastapi_app.py`: Contains the FastAPI server code for handling requests and generating predictions.
- `streamlit_app.py`: Contains the Streamlit app code for user interaction and displaying predictions.
- `openai_integration.py`: Contains the code for integrating with OpenAI to generate predictions based on user inputs.
- `requirements.txt`: Lists the required Python libraries for the project.

## Customization

- You can modify the prompt string in `fastapi_app.py` to customize the message shown to the OpenAI model.
- Feel free to modify the Streamlit app in `streamlit_app.py` to add more input fields or enhance the user interface.

## Credits

This project utilizes the OpenAI GPT-3 model for generating predictions. Visit the [OpenAI website](https://openai.com/) to learn more about their model and obtain an API key.

## License

This project is licensed under the [MIT License](LICENSE).
