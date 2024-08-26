# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy backend files
COPY app/ ./app/

# Copy frontend files
COPY frontend/ ./frontend/

# Install dependencies
RUN pip install --no-cache-dir -r app/requirements.txt
RUN pip install --no-cache-dir -r frontend/requirements.txt

# Expose ports
EXPOSE 8000 8501

# Start the application
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port 8000 & streamlit run frontend/streamlit_app.py"]