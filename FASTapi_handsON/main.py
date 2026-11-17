@app.get("/new")
def new_route():
    return {
        "message": "Updated through GitHub Actions!"
    }