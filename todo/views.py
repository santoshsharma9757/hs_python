"""
Todo Views - Handles all CRUD operations for Todo items
This module uses JWT authentication to ensure only authenticated users can access todos
Each user can only see and modify their own todos (security feature)
"""

from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.views import APIView
# Import JWT authentication instead of Token authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class TodoView(APIView):
    """
    Todo View - Handles all HTTP methods for Todo operations
    
    Authentication: JWT (JSON Web Token) required
    - Include token in request header: Authorization: Bearer <access_token>
    
    Security: Users can only access their own todos
    """
    
    # Use JWT authentication instead of Token authentication
    # JWT tokens are more secure and scalable
    authentication_classes = [JWTAuthentication]
    
    # Require user to be authenticated to access any endpoint
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        """
        GET /api/todo/ - Get all todos for the authenticated user
        GET /api/todo/<id>/ - Get a specific todo by ID
        
        Returns:
        - 200 OK: List of todos or single todo
        - 404 Not Found: Todo not found or doesn't belong to user
        """
        if pk is not None:
            # Get a specific todo by ID
            try:
                # IMPORTANT: Filter by user to ensure users can only see their own todos
                # This is a security feature - prevents users from accessing others' todos
                todo = Todo.objects.get(pk=pk, user=request.user)
                
                # Convert Todo model instance to JSON format
                serializer = TodoSerializer(todo)
                
                return Response(
                    {
                        "success": True,
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            except Todo.DoesNotExist:
                # Todo doesn't exist or doesn't belong to this user
                return Response(
                    {
                        "success": False,
                        "message": "Todo not found or you don't have permission to view it"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
            except Exception as e:
                # Handle any other unexpected errors
                return Response(
                    {
                        "success": False,
                        "error": "An error occurred while retrieving the todo",
                        "details": str(e)
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            # Get all todos for the authenticated user
            # IMPORTANT: Filter by user - users should only see their own todos
            queryset = Todo.objects.filter(user=request.user).order_by('-created_at')
            
            # Convert multiple Todo instances to JSON format
            # many=True tells serializer we're serializing a list, not a single object
            serializer = TodoSerializer(queryset, many=True)
            
            return Response(
                {
                    "success": True,
                    "count": len(serializer.data),
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

    def post(self, request):
        """
        POST /api/todo/ - Create a new todo
        
        Request body:
        {
            "title": "My Todo Title",
            "description": "Detailed description of the todo"
        }
        
        Returns:
        - 201 Created: Todo successfully created
        - 400 Bad Request: Validation errors
        """
        try:
            # Get data from request body
            request_data = request.data
            
            # Validate the data using serializer
            # This checks if title and description are provided and valid
            serializer = TodoSerializer(data=request_data)
            
            if serializer.is_valid():
                # Save the todo and automatically assign it to the current user
                # request.user is set by JWT authentication
                serializer.save(user=request.user)
                
                return Response(
                    {
                        "success": True,
                        "message": "Todo created successfully",
                        "data": serializer.data
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                # Return validation errors if data is invalid
                return Response(
                    {
                        "success": False,
                        "message": "Validation failed",
                        "errors": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            # Handle unexpected errors
            return Response(
                {
                    "success": False,
                    "error": "An error occurred while creating the todo",
                    "details": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request, pk=None):
        """
        PUT /api/todo/<id>/ - Update an existing todo (full update)
        
        Request body:
        {
            "title": "Updated Title",
            "description": "Updated description"
        }
        
        Returns:
        - 200 OK: Todo successfully updated
        - 400 Bad Request: Validation errors
        - 404 Not Found: Todo not found or doesn't belong to user
        """
        # Check if todo ID is provided
        if pk is None:
            return Response(
                {
                    "success": False,
                    "message": "Todo ID is required to update"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Get the todo - IMPORTANT: Filter by user for security
            # This ensures users can only update their own todos
            todo = Todo.objects.get(pk=pk, user=request.user)
            
            # Update the todo with new data
            # The first argument (todo) is the instance to update
            # The second argument (request.data) is the new data
            serializer = TodoSerializer(todo, data=request.data)

            if serializer.is_valid():
                # Save the updated todo
                # user is preserved automatically since it's read-only
                serializer.save()
                
                return Response(
                    {
                        "success": True,
                        "message": "Todo updated successfully",
                        "data": serializer.data
                    },
                    status=status.HTTP_200_OK
                )
            else:
                # Return validation errors
                return Response(
                    {
                        "success": False,
                        "message": "Validation failed",
                        "errors": serializer.errors
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Todo.DoesNotExist:
            # Todo doesn't exist or doesn't belong to this user
            return Response(
                {
                    "success": False,
                    "message": "Todo not found or you don't have permission to update it"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            # Handle unexpected errors
            return Response(
                {
                    "success": False,
                    "error": "An error occurred while updating the todo",
                    "details": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def delete(self, request, pk=None):
        """
        DELETE /api/todo/<id>/ - Delete a todo
        
        Returns:
        - 200 OK: Todo successfully deleted
        - 404 Not Found: Todo not found or doesn't belong to user
        """
        # Check if todo ID is provided
        if pk is None:
            return Response(
                {
                    "success": False,
                    "message": "Todo ID is required to delete"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            # Get the todo - IMPORTANT: Filter by user for security
            # This ensures users can only delete their own todos
            todo = Todo.objects.get(pk=pk, user=request.user)
            
            # Delete the todo from database
            todo.delete()
            
            return Response(
                {
                    "success": True,
                    "message": "Todo deleted successfully"
                },
                status=status.HTTP_200_OK
            )
        except Todo.DoesNotExist:
            # Todo doesn't exist or doesn't belong to this user
            return Response(
                {
                    "success": False,
                    "message": "Todo not found or you don't have permission to delete it"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            # Handle unexpected errors
            return Response(
                {
                    "success": False,
                    "error": "An error occurred while deleting the todo",
                    "details": str(e)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
