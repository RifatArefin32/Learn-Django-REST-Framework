# Views

## Function based views
- For using API, we need to use `@api_view(['GET', 'POST'])` decorator

## Class based views
- It provides an object-oriented way to define views. 
- Instead of writing view logic in functions (as in function-based views), we write views as classes, where each HTTP method (e.g., GET, POST) corresponds to a method on the class. 
- HTTP methods like GET, POST, etc., are implemented as methods of the class (e.g., get(), post())
- For using API, `class ClassName(APIView)` is used. We need to inherit `APIView` class

## Generic views
- Generic Views are a set of pre-built views that provide common functionality for handling HTTP requests. 
- These views allow developers to quickly implement common operations like CRUD objects without needing to write the logic from scratch.
- Common Generic Views in DRF:
    - ListAPIView
    - CreateAPIView
    - RetrieveAPIView
    - UpdateAPIView
    - DestroyAPIView
    - ListCreateAPIView
    - RetrieveUpdateDestroyAPIView

## ViewSets
- A ViewSet combines the behavior of several generic views (e.g., ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView) into a single class and automatically provides methods for CRUD (Create, Read, Update, Delete) operations.