# Movie Profitability

## Setup
1. Ensure you are using python 3+
2. `pip install -r requirements.txt`
3. Run the tests to make sure everything is set up correctly - `pytest`
4. Run the API: `python run.py`
5. Use the below API documentation to make your requests about movies

### API Documentation
Base URL: http://localhost:5000/api

#### GET /genres
Retrieves the top ten movie genres in decreasing order by their net profitability as defined by `gross` minus `budget`.

```
{
  success: true
}

```

#### GET /actors
Retrieves the top ten actors in decreasing order by their net profitability as defined by `gross` minus `budget`.

```
{
  success: true
}

```

#### GET /directors
Retrieves the top ten directors in decreasing order by their net profitability as defined by `gross` minus `budget`.

```
{
  success: true
}

```
