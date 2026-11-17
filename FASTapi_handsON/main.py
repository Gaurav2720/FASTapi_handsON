@app.get("/new")
def new_route():
    return {
        "message": "Updated automatically using GitHub Actions!"
    }