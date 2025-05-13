# Serializer
Serializers allow complex data such as `querysets` and `model instances` to be converted to native `Python datatypes` that can then be easily rendered into `JSON`, `XML` or other content types. 

Serializers also provide `deserialization`, allowing parsed data to be converted back into complex types, after `first validating the incoming data`.

The serializers in REST framework work very similarly to `Django's Form `and `ModelForm` classes. 

DRF provides,
- A `Serializer` class which gives us a powerful, generic way to control the output of our responses
- A `ModelSerializer` class which provides a useful shortcut for creating serializers that deal with model instances and querysets.

[Serializer fields](https://www.django-rest-framework.org/api-guide/fields/) handle,
- Converting between primitive values and internal datatypes. 
- Validating input values, retrieving and setting the values from their parent objects.

