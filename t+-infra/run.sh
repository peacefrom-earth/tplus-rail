\#!/bin/bash
#!/bin/bash
echo "Activating virtual environment..."
source venv/bin/activate
echo "Starting Gunicorn on port $PORT..."
FLASK_ENV=production gunicorn -w 4 -b "0.0.0.0:$PORT" app:app
echo "Gunicorn process ended unexpectedly."
sleep 1000

echo "Project is running! Open index.html in a browser"
