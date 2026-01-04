# web-service-starter

A simple FastAPI web service that returns "Hello World" for GET requests.

## Running Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   ```
   
   **Windows (PowerShell):**
   ```bash
   .\venv\Scripts\Activate.ps1
   ```
   
   **Windows (CMD):**
   ```bash
   venv\Scripts\activate.bat
   ```
   
   **macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```
   
   **Note for Windows users:** If `uvicorn` is not recognized, use:
   ```bash
   python -m uvicorn main:app --reload
   ```
   
   **Note for IDE users:** If you see import errors in your IDE (like PyCharm), configure your IDE to use the Python interpreter from the `venv` folder:
   - **PyCharm**: File → Settings → Project → Python Interpreter → Select `venv\Scripts\python.exe`

   The `--reload` flag enables auto-reload on code changes (useful for development).

### Access the Application

Once running, the application will be available at:
- **API**: http://localhost:8000
- **Interactive API Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Documentation (ReDoc)**: http://localhost:8000/redoc

### Test the Endpoint

You can test the hello world endpoint by:
- Opening http://localhost:8000 in your browser
- Using curl: `curl http://localhost:8000`
- Using the interactive docs at http://localhost:8000/docs

## Running Tests

The project includes integration tests using pytest and FastAPI's TestClient.

### Run All Tests

```bash
pytest
```

### Run Tests with Verbose Output

```bash
pytest -v
```

### Run a Specific Test File

```bash
pytest tests/test_main.py
```

### Run Tests with Coverage

First install pytest-cov (optional):
```bash
pip install pytest-cov
```

Then run:
```bash
pytest --cov=main --cov-report=html
```

The tests verify:
- Root endpoint (`/`) returns "Hello World"
- `/hello/{name}` endpoint works with various names
- Proper status codes and response formats