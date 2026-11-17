from fastapi import FastAPI

# Step 1: Create FastAPI application
app = FastAPI()


# Step 2: Home route
@app.get("/")
def home():
    return {
        "message": "FastAPI is running"
    }


# Step 3: Health check route
@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# Step 4: New route added for GitHub Actions testing
@app.get("/new")
def new_route():
    return {
        "message": "Updated automatically using GitHub Actions!"
    }