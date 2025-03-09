#!/bin/bash
source venv/bin/activate #Activate virtual environment
FLASK_ENV=production gunicorn -w 4 -b "[::]:8081" chat:app &
FLASK_ENV=production gunicorn -w 4 -b "[::]:8080" --log-level debug app:app & #Start Flask-SocketIO for real-time chat
echo "Project is running! Open index.html in a browser"
