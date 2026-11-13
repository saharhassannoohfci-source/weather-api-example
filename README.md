# Weather API example

Calls a public REST API, parses JSON into a small dataclass, and prints a summary.

1. Get an API key from https://www.weatherapi.com/ and replace the placeholder in `.env`.
2. In PowerShell, create the virtual environment and install dependencies:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

3. Run using the virtual environment's interpreter:

   ```powershell
   .\.venv\Scripts\python.exe test.py
   .\.venv\Scripts\python.exe test.py "New York"
   ```

The default city comes from `WEATHER_CITY` in `.env`. A command-line city overrides it.
The `.env` file is ignored by Git to keep your key private.

API documentation: https://www.weatherapi.com/docs/getting-started/
