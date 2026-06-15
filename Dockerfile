FROM python:3.10-slim

RUN apt-get update && apt-get install -y     git curl ffmpeg wget bash &&     apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -U -r requirements.txt

COPY . .

ENV PORT=7860
EXPOSE 7860

# Hugging Face Spaces expects a web server on PORT.
# app.py keeps the Space healthy; main.py runs the Telegram bot.
CMD ["sh", "-c", "python3 app.py & python3 main.py"]
