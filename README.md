# Selenium API Test Project

This project demonstrates API testing using Selenium WebDriver in a Docker environment. It includes a simple API service and automated tests to verify its functionality.

## Project Structure

- `api/` - Contains the API service implementation
  - `app.py` - Main API application
  - `requirements.txt` - Python dependencies
  - `Dockerfile` - Container configuration for the API service
- `selenium-tests/` - Contains the Selenium test suite
  - `test_api.py` - Test cases for the API endpoints

## Setup and Running

1. Make sure you have Docker and Docker Compose installed
2. Run the following command to start the services:
   ```bash
   docker-compose up
   ```
3. The tests will run automatically when the services are up

## API Endpoints

- `GET /api/data` - Returns a simple JSON response
- `GET /api/check/{number}` - Checks if a number is even

## Testing

The project uses Selenium WebDriver to test the API endpoints. Tests are configured to run in a headless Chrome browser within a Docker container. 