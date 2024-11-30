from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Expense, Income
from .serializers import ExpenseSerializer, IncomeSerializer

@api_view(['POST'])
def save_item(request):
    if request.data['type'] == 'exp':
        serializer = ExpenseSerializer(data=request.data)
    elif request.data['type'] == 'inc':
        serializer = IncomeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_item(request):
    model = Expense if request.data['type'] == 'exp' else Income
    try:
        item = model.objects.get(id=request.data['id'], user_id=request.data['userId'])
        item.delete()
        return Response({'message': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except model.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)