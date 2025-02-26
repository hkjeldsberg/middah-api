# Middah

## Prerequisites

The project relies on the following Python dependencies, also listed in `pyproject.toml`:

- Python => 3.7
- FastAPI
- Uvicorn
- Scikit-learn
- Pandas

## Running locally

To run the service locally, follow these steps:

### Step 1: Install dependencies

1. Create a virtual environment (optional but recommended). You can use `venv` or `conda` to create a virtual
   environment:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```


2. Install the necessary dependencies from `pyproject.toml`:

   ```bash
   pip install -r requirements.txt 
   ```

3. Run the application locally by executing the following command:

```bash
uvicorn app.main:app --reload
```

Endpoints will be accessible at: `http://localhost:8000/`

## API Documentation

## TODOs

### Web hosting (Webhuset)

- [ ] Setup domain and hosting through Webhuset

### Database (Postgres)

- [ ] Setup database
- [ ] Host database with Neon

### Backend (FastAPI)

- [ ] Create backend API for fetching recipes

### Frontend (Next)

- [ ] Create frontend for displaying recipes
- [ ] Add search functionality
- [ ] Add filter functionality
- [ ] Add pagination
- [ ] Add recipe scaling 

