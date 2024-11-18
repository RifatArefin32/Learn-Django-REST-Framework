# Serializer

In Django REST Framework (DRF), a serializer is a mechanism for converting complex data types (like Django models) into native Python datatypes (e.g., dictionaries, lists) that can then be easily converted to JSON, XML, or other content types suitable for APIs. 

- Complex datatype (model) to Python Datatypes (dictionary, list etc.)
- Python datatype to JSON, XML etc.

Similarly, serializers also validate and convert incoming data (e.g., JSON) into Python objects or Django models for further processing which is called `Deserialization`.

# Types of Serializers in DRF

### serializers.Serializer
- A manually defined serializer where we specify every field and write the logic for serialization and deserialization.
- Provides fine-grained control over how the data is processed.
- Example
```python
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
```

### serializers.ModelSerializer
- Automatically maps Django models to serializer fields, greatly simplifying the code.
- Suitable for most cases when working with Django models.
- Example
```python
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email']
```