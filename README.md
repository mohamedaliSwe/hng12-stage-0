# HNG12 Stage 0

This a simple API that return registered email address, current datetime as an ISO 8601, GitHub URL of this project.

## Requirements

- Python 3.*
- Flask
- Flask-Cors

## Set Up

To run this project locally

### Prerequisites

Ensure that you have python 3 install. you can verify by running.

```bash
python3 --version
```

### Installation

1. Clone the project repository.

```bash
git clone https://github.com/mohamedaliSwe/hng12-stage-0.git
cd hng12-stage-0
```

2. Create a virtual environment and activate it.

- If you are on linux do the following:

```bash
python3 -m venv myenv
source myenv/bin/activate
```

- If you are using windows do the following:

```bash
python -m venv myenv
venv\Scripts\activate
```

3. Intall the required dependencies.

```bash
pip install Flask Flask-Cors
```

4. Run the application.

```bash
python3 app.py
```

## API Documentation

### Endpoint

- GET /

### Response format

A successful request will return the following JSON response:

```bash
{
  "email": "mohamedcali350@gmail.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/mohamedaliSwe/hng12-stage-0.git"
}
```

### Usage

To use the API, send a GET request to the deployed endpoint.

```bash
curl https://your-deployed-url.com/
```

## Backlinks

https://hng.tech/hire/python-developers

## License

This project is licensed under the MIT License