#!/bin/bash
source venv/bin/activate #Activate virtual environment
FLASK_ENV=production gunicorn -w 4 -b 0.0.0.0:5007 backend.chat:app &
FLASK_ENV=production gunicorn -w 4 -b 0.0.0.0:5006 backend.app:app & #Start Flask-SocketIO for real-time chat
echo "Project is running! Open index.html in a browser"
