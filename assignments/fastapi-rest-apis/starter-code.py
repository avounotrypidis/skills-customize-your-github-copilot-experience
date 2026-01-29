"""
FastAPI REST API Starter Code

This starter code provides the basic structure for building a REST API with FastAPI.
Complete the tasks by implementing the required endpoints and data validation.
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Optional

# Initialize FastAPI application
app = FastAPI(title="Student API", version="1.0.0")

# TODO: Define a Pydantic model for your data structure
# Example: class Student(BaseModel):
#     id: int
#     name: str
#     email: str
#     grade: int

# TODO: Create a simple in-memory data storage (list or dictionary)
# Example: students = []

# TODO: Implement a GET endpoint that returns all items
# @app.get("/")
# async def read_items():
#     pass

# TODO: Implement a POST endpoint to create a new item
# @app.post("/")
# async def create_item():
#     pass

# TODO: Implement a GET endpoint with a path parameter to retrieve a specific item
# @app.get("/{item_id}")
# async def read_item(item_id: int):
#     pass

# TODO: Implement a PUT endpoint to update an item
# @app.put("/{item_id}")
# async def update_item(item_id: int):
#     pass

# TODO: Implement a DELETE endpoint to remove an item
# @app.delete("/{item_id}")
# async def delete_item(item_id: int):
#     pass

# Run the application with: uvicorn starter-code:app --reload
