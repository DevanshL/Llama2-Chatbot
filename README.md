# Llama2 Chatbot

Welcome to the **Llama2 Chatbot** application! This chatbot is designed to provide informative and engaging responses to your queries using the advanced Llama2 language model.

## Features

- **User-Friendly Interface**: The chatbot interface is simple and intuitive, making it easy for anyone to use.
- **Advanced Language Model**: Utilizes the powerful Llama2 language model to generate human-like responses.
- **Customizable**: Various settings and options available in the sidebar to tailor the chatbot's behavior.

## Installation

To install the necessary dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage
1. Clone the repository:
```
bash
git clone https://github.com/yourusername/llama2-chatbot.git
cd llama2-chatbot
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```
3. Create a config.json file to store your Hugging Face API credentials.
4. Run the Streamlit application:
   
```
bash
streamlit run app.py
```
5. Open your browser and go to http://localhost:8501 to interact with the chatbot.

## API Integration with Hugging Face
To use the Hugging Face API in your Streamlit application, follow these steps:

### Step 1: Obtain API Credentials from Hugging Face
Sign up/Login to Hugging Face: Go to the Hugging Face website and sign up or log in to your account.
Create an API Token: Navigate to your account settings and create an API token.

### Step 2: Create a config.json File
Create a config.json file in the root directory of your project to store your API token and other configurations.

Example config.json file:
```
json
{
  "hf_api_token": "YOUR_HUGGING_FACE_API_TOKEN"
}
```
Replace YOUR_HUGGING_FACE_API_TOKEN with your actual API token.

### Step 3: Modify app.py to Use the Configuration
In your app.py file, add code to read the config.json file and use the configurations.

## Screenshots

Figure 1: The main interface of the Llama2 Chatbot.


Figure 2: An example conversation with the Llama2 Chatbot.

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License
This project is licensed under the MIT License. See the LICENSE file for details.



