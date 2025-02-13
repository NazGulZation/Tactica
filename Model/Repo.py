class Repo:
    def __init__(self):
        # Internal list to store objects
        self._data = []
    
    def create(self, obj):
        """Insert the object into the repository."""
        self._data.append(obj)
    
    def get(self, type=None):
        """Return the list of all objects in the repository.
        
        Args:
            type (optional): A specific type to filter objects.
                             Only objects that are instances of this type will be returned.
        
        Returns:
            list: A list of objects in the repository, filtered by type if provided.
        """
        if type is None:
            return self._data
        return [obj for obj in self._data if isinstance(obj, type)]
    
    def delete(self, obj):
        """Remove the object from the repository.
        
        Raises:
            ValueError: If the object is not found in the repository.
        """
        try:
            self._data.remove(obj)
        except ValueError:
            print("Object not found in the repository.")