#!/bin/bash
source venv/bin/activate #Activate virtual environment
FLASK_ENV=production gunicorn -w 4 -b 0.0.0.0:8081 chat:app &
FLASK_ENV=production gunicorn -w 4 -b 0.0.0.0:8080 app:app & #Start Flask-SocketIO for real-time chat
echo "Project is running! Open index.html in a browser"
