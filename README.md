# counter-service
Maintains a web page with a counter of the amount of POST requests it served that it returns on every GET request it gets.

# Dockerfile
Creates a web server (nginx, flask, uwsgi and redis) with the counter-service files.

# docker-compose.yml
Starts the web server and redis DB.
