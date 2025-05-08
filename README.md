# 🩺 Hermes - Final Year Project Chatbot

Hermes is an intelligent chatbot developed as the final project for my university degree for the Consult system. It was designed to assist users in identifying possible health symptoms and suggesting appropriate next steps, including recommending nearby clinics. Built with **Rasa**, **Python**, and **Docker**, this chatbot acts as a **consultant**, not a diagnostic tool.

## 📱 Overview

The chatbot is integrated with both:
- A **mobile front-end** (for user interaction).
- A **back-end** (for data management and analysis).

### 🧠 Functionality
- Users can interact with the chatbot via a conversational interface.
- The chatbot gathers information on user-reported symptoms.
- Based on the conversation, it provides **suggestions** and **guides** users to seek professional help if necessary.
- **No medical diagnosis is made** — the chatbot simply assists in directing users to appropriate healthcare options.

### 🔄 Data Handling
- The chatbot sends user data to a back-end system for secure storage and analysis.
- It also retrieves relevant information to display to users (e.g., symptom explanations, clinic directions, etc.).

## 🛠️ Technologies Used
- **Rasa** – for building conversational AI with intents and entity extraction.
- **Python** – as the core programming language.
- **Docker** – for containerized deployment and portability.

## ⚠️ Disclaimer
DoctorBot is intended for **educational and consultative purposes only**. It does not provide medical diagnoses or treatments. Users are always advised to consult a licensed medical professional or visit a healthcare facility for any medical concerns.

## 🚀 Getting Started
To run the project locally:
1. Clone the repository.
2. Ensure Docker is installed.
3. Use the provided Docker Compose file to start the services.

```
docker-compose up
```
## 📚 Project Structure
```
.
├── data/              # Rasa chatbot files (domain, stories, etc.)
├── actions/              # API and data handling logic
├── docker-compose.yml    # Docker configuration
└── README.md
```
## 📩 Contact
Feel free to reach out for questions, feedback, or collaboration!
