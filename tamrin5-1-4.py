
import json

class PromaxList(list):
    """A list-like class with an additional method to convert itself to JSON."""
   
    def to_json(self):
        """Convert the list and its data to a JSON string.
       
        Returns:
        str: JSON representation of the list.
        """
        return json.dumps(self)  # Use the json.dumps() to serialize list data

class PromaxDict(dict):
    """A dict-like class with an additional method to convert itself to JSON."""
   
    def to_json(self):
        """Convert the dictionary and its data to a JSON string.
       
        Returns:
        str: JSON representation of the dictionary.
        """
        return json.dumps(self)  # Use the json.dumps() to serialize dict data

# Example Usage:
# Test for PromaxList
my_list = PromaxList([1, 2, 3, {"key": "value"}])
print(my_list.to_json())  # Output: [1, 2, 3, {"key": "value"}]

# Test for PromaxDict
my_dict = PromaxDict({"name": "Reza", "age": 30, "languages": ["Python", "C++"]})
print(my_dict.to_json())  # Output: {"name": "Reza", "age": 30, "languages": ["Python", "C++"]}

