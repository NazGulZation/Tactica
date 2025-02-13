class Repo:
    def __init__(self):
        # Internal list to store objects
        self._data = []
    
    def create(self, obj):
        """Insert the object into the repository."""
        self._data.append(obj)
    
    def get(self, type=None, condition=None):
        """
        Retrieve objects from the repository, filtering by type and an optional condition.

        Args:
            type (optional): A specific type to filter objects. Only objects that are instances
                             of this type will be returned.
            condition (optional): A function that takes an object and returns a boolean. Only objects
                                  for which the function returns True are included.

        Returns:
            list: A list of objects in the repository matching the criteria.
        """
        # Use a default condition that always returns True if none is provided.
        condition = condition or (lambda x: True)
        if type is not None:
            return [obj for obj in self._data if isinstance(obj, type) and condition(obj)]
        return [obj for obj in self._data if condition(obj)]
    
    def delete(self, obj):
        """Remove the object from the repository.
        
        Raises:
            ValueError: If the object is not found in the repository.
        """
        try:
            self._data.remove(obj)
        except ValueError:
            print("Object not found in the repository.")