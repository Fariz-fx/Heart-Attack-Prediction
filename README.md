# Heart Attack Prediction

This repository contains code for a heart attack prediction application using Streamlit and FastAPI. The application allows users to input various parameters related to heart health and receive a prediction on the probability of experiencing a heart attack.

## Want to know more
Click this [link](https://youtu.be/L5G2noJiUeU) for checking out 19 min Demo on Purpose, Setup and Usage

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository and Navigate to the folder:

```bash
git clone https://github.com/Fariz-fx/Heart-Attack-Prediction.git
cd .\Heart-Attack-Prediction\
```

2. (Optional) Create and activate a virtual environment:

You can leverage either conda or venv. We recommend to use conda

a. [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)

Create conda environment

```bash
conda create -n "env" python=3.11
```

Activate conda

```bash
conda activate venv
```

b. [Venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

```bash
python -m venv venv
```

- On Windows:

In Bash:

```bash
env\Scripts\activate
```

In Powershell:

```powershell
venv\Scripts\Activate.ps1
```

- On macOS and Linux:

```bash
source venv/bin/activate
```

Note: Using a virtual environment is optional but recommended to isolate project dependencies.

3. Install the required Python libraries:

```git
pip install -r requirements.txt
```

4. Rename from .env.sample to .env

Rename the file .env.sample to .env and get the API key from [OpenAI](https://platform.openai.com/account/api-keys)

5. Run Uvicorn Locally

```bash
cd .\app\
uvicorn fastapi_app:app --reload
```

Visit [Swagger to test API](http://localhost:8000/docs#/)

6. Run Streamlit Locally

Open New Terminal and ensure uvicorn is running in another terminal

```bash
cd .\client\
streamlit run Home.py
```

Visit [Streamlit locally to test frontend](http://localhost:8501/)

## Usage

We have FastAPI installed as Backend to work on API's and Streamlit as Frontend where user interacts

### Run FastAPI Server

1. Start the FastAPI server by running the following command:

```bash
uvicorn fastapi_app:app --reload
```

The server will start running at `http://localhost:8000`.

### Run Streamlit App

1. Open a new terminal and navigate to the project directory.

2. Start the Streamlit app by running the following command:

```bash
streamlit run streamlit_app.py
```

The Streamlit app will open in your default web browser.

3. In the Streamlit app, enter the required information such as age, sex, chest pain type, and other parameters related to heart health.

4. Click the "Predict" button to send the data to the FastAPI server for prediction.

5. The predicted probability of a heart attack will be displayed on the Streamlit app.

### To Train your lightweight model

To train your model with your own data, place the data in data folder and run train_model.py

```python
python3 train_model.py
```

Note: For Huge Data training recommend to use Notebook like Jupiter to get more benefit out of it

## Project Structure

- `fastapi_app.py`: Contains the FastAPI server code for handling requests and generating predictions.
- `streamlit_app.py`: Contains the Streamlit app code for user interaction and displaying predictions.
- `openai_integration.py`: Contains the code for integrating with OpenAI to generate predictions based on user inputs.
- `requirements.txt`: Lists the required Python libraries for the project.

## Customization

- You can modify the prompt string in `fastapi_app.py` to customize the message shown to the OpenAI model.
- Feel free to modify the Streamlit app in `streamlit_app.py` to add more input fields or enhance the user interface.

## Credits

1. This project utilizes the OpenAI GPT-3 model for generating predictions. Visit the [OpenAI website](https://openai.com/) to learn more about their model and obtain an API key.

2. This project utilizes the [Data Model csv file from rashikrahmanpritom which is available in Kaggle.com](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset?resource=download)

## License

This project is licensed under the [MIT License](LICENSE).
