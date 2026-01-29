# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You'll create a functional API with multiple endpoints, data validation, and proper HTTP status codes to understand core concepts of web service development.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with a simple endpoint that responds to GET requests. This is your foundation for building more complex APIs.

#### Requirements
Completed program should:

- Import FastAPI and create an application instance
- Define at least one GET endpoint that returns a JSON response
- Include appropriate response status codes (200 for success)
- Run the application using Uvicorn server


### 🛠️ Implement CRUD Operations

#### Description
Build endpoints that perform Create, Read, Update, and Delete (CRUD) operations on a simple data model. Work with a list or dictionary to store data in memory.

#### Requirements
Completed program should:

- Create a POST endpoint to add new items with request body validation
- Create a GET endpoint to retrieve all items
- Create a GET endpoint with a path parameter to retrieve a specific item
- Create a PUT endpoint to update an existing item
- Create a DELETE endpoint to remove an item
- Return appropriate HTTP status codes (201 for creation, 404 for not found, etc.)


### 🛠️ Add Data Validation with Pydantic Models

#### Description
Use Pydantic models to validate incoming request data, ensuring type safety and clear API documentation.

#### Requirements
Completed program should:

- Define Pydantic models for your data structure
- Use models in request body parameters for automatic validation
- Return validation error responses with helpful messages
- Document model fields with descriptions using Field()


### 🛠️ Test Your API

#### Description
Test your API endpoints using appropriate HTTP methods and verify the responses are correct.

#### Requirements
Completed program should:

- Test all endpoints with different scenarios (valid data, missing fields, invalid types)
- Verify correct status codes are returned for each operation
- Document test cases and results
- Use tools like curl, Postman, or Python requests library


