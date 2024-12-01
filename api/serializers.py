from rest_framework import serializers
from .models import Task, Book, Author

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'price', 'author']

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('Title must be at least 3 characters long.')
        return value
    
    def validate_price(self, value):
        if value < 1:
            raise serializers.ValidationError('Price must be greater than 0.')
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'books']