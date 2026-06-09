# Python Projects (Summer, Age 12–13)

This repository is a collection of Python projects I built during the summers when I was 12–13 years old.  
It includes everything from simple games to early experiments with chatbots, web APIs, and front‑end integrations.

## Overview

These projects started as a way for me to learn Python by building things I thought were fun:

- Small games like hangman and number experiments.
- Simple ciphers and console programs.
- Early chatbots and AI experiments.
- Basic backend APIs with Flask.
- A first attempt at connecting Python backends to HTML frontends.

Most of the code lives directly in this root directory, with some additional structure in folders like `backend/`, `frontend/`, and `ollamaprj/`.

## Project highlights

Here are a few representative files and folders:

- `hangman.py`  
  A classic text‑based hangman game that uses random words and loops to handle guesses and track the game state.

- `ceaser_cipher.py`  
  A simple implementation of the Caesar cipher that helped me understand strings, character codes, and basic encryption ideas.

- `TTTAI.py`  
  A tic‑tac‑toe project where I experimented with basic AI logic to make the computer an opponent instead of just two human players.

- `chatbot.py`, `chatai.py`, `Nikhil_chatbot_backup.py`, `knowledge.pkl`  
  Early chatbot experiments using Python, where I started playing with storing information and responding to user input.

- `simpleapi.py`, `gemini.py`, `ollamaapi_orig.py`, `from flask import Flask, jsonify, reques.py`  
  Backend/API experiments, including Flask code and calls to external AI tools and APIs.

- `frontend_ollama_chatbot.html`, `frontend/`, `backend/`, `ollamaprj/`  
  First attempts at connecting a Python backend to a simple HTML frontend for a chatbot project.

- `cool_drawing.py`, `wow.py`, `numbers.py`, `hello.py`, `sherva.py`  
  Smaller experiments where I tried out new ideas, practiced syntax, or just had fun with Python.

(As I keep learning, I may add more comments and small notes to these files, but I plan to preserve the original structure as much as possible.)

## How to run these projects

All of the projects in this repository use Python 3.

1. Install Python 3  
   You can download it from https://www.python.org/ or install it with your system’s package manager.

2. Clone this repository:
   ```bash
   git clone https://github.com/Firegod-browser/Python-Projects.git
   cd Python-Projects
   ```

3. Run a simple script (for example, hangman):
   ```bash
   python hangman.py
   ```

4. For API / web projects (like the Flask or chatbot examples):
   - Check the top of the file for any import errors.
   - Install required packages, for example:
     ```bash
     pip install flask
     ```
   - Run the script, then open the URL it prints (often `http://127.0.0.1:5000/`) in your browser.
   - For HTML frontends (like `frontend_ollama_chatbot.html`), open the HTML file in your browser and make sure the backend is running.

Not every project has a full setup guide, because many started as experiments, but most are small enough to read and run with minimal setup.

## How to read this code

This repository is intentionally left close to how I originally wrote the code at 12–13:

- The style, naming, and structure are not always consistent.
- Some projects contain bugs, unfinished features, or experimental code.
- A few files are backups or prototypes from when I was trying something new.

Instead of rewriting everything to match my later skill level, I’m keeping this repo as a snapshot of how I learned and what I was curious about at that age.

## Why I’m keeping this public

This repository is part of my long‑term programming journey:

- It shows that I started exploring Python and AI tools on my own at a relatively young age.
- It documents my first attempts at building games, chatbots, and simple APIs.
- It reminds me how much I’ve improved over time and how important experimentation is to learning.

In the future, when I apply to college and share my coding portfolio, this repo will serve as evidence of my early interest, self‑teaching, and persistence in computer science.

## License
This repository is mainly for educational and portfolio purposes.  
You are welcome to read, run, and learn from the code. If you reuse significant portions in another project, please credit this repository.
