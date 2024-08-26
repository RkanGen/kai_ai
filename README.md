#  Kai_ai is AI-Powered Resume Builder

This project is an AI-powered resume builder that customizes resumes based on job descriptions. It uses the Groq API to generate tailored resumes, and is built with FastAPI for the backend, Streamlit for the frontend, and Docker for containerization.

## Features

- Upload your existing resume
- Input job descriptions
- Generate customized resumes using AI
- User-friendly web interface
- Dockerized application for easy deployment

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker and Docker Compose installed on your system
- A Groq API key

## Installation and Setup

1. Clone the repository:
git clone https://github.com/RkanGen/kai_ai.git
cd kai_ai


Copier

2. Create a `.env` file in the root directory and add your Groq API key:
`GROQ_API_KEY=your_groq_api_key_here`


Copier

3. Build and run the Docker containers:
 - `docker-compose up --build`



Copier

## Usage

1. Once the application is running, open your web browser and go to `http://localhost:8501`.

2. In the web interface:
- Paste your current resume into the first text area.
- Paste the job description into the second text area.
- Click the "Generate Custom Resume" button.

3. The application will generate a customized resume based on your input and the job description.

4. Review the generated resume and make any necessary adjustments before using it.



## Technologies Used

- FastAPI: Backend API framework
- Streamlit: Frontend web application
- Groq API: AI-powered text generation
- Docker: Containerization and deployment

## Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License .

## Acknowledgments

- Groq for providing the AI API
- The FastAPI and Streamlit communities for their excellent documentation and tools
