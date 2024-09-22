# Quick Voice Bot Demo

This is a demo showcasing a bot that utilizes Text-To-Speech, Speech-To-Text, and a language model to have a conversation with a user.

## Features

- **Text-To-Speech**: Converts text input into spoken words using Deepgram's API.
- **Speech-To-Text**: Converts spoken words into text for processing.
- **Language Model**: Engages in conversation using Groq's language model.

## Requirements

Before running the demo, ensure you have the following:

- Python 3.x
- A Deepgram API key
- A Groq API key

## Setup Instructions

1. **Create a Virtual Environment**:
   ```bash
   python -m venv env

2. **Activate the Virtual Environment**:
   ```bash
    .\env\Scripts\activate
3. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
4. **Create a `.env` File**:
    In the same directory as `main.py`, create a `.env` file and add your API keys:
    ```bash
    DEEPGRAM_API_KEY=your_deepgram_api_key_here
    GROQ_API_KEY=your_groq_api_key_here

5. **Run the Demo**:
    Execute the main script to start the bot:
    ```bash
    python main.py


