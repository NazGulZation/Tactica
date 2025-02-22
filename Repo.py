import pickle
import os

class Repo:
    def __init__(self):
        # Internal list to store objects
        self._data = []
    
    def create(self, obj):
        """Insert the object into the repository."""
        self._data.append(obj)
    
    def delete(self, obj):
        """Remove the object from the repository.
        
        Raises:
            ValueError: If the object is not found in the repository.
        """
        try:
            self._data.remove(obj)
        except ValueError:
            print("Object not found in the repository.")
    
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

    def load(self, filename, dir="."):
        """Load repository data from a file using pickle.

        Args:
            filename (str): The name of the file to load from (without extension).
            dir (str, optional): The directory to load the file from. Defaults to the current directory.
        """
        full_filename = os.path.join(dir, filename + ".pkl")
        try:
            with open(full_filename, 'rb') as f:
                self._data = pickle.load(f)
            print(f"Repository data loaded from '{full_filename}'")
        except FileNotFoundError:
            print(f"File '{full_filename}' not found. Repository data not loaded.")
        except Exception as e:
            print(f"Error loading repository data from '{full_filename}': {e}")

    def save(self, filename, dir="."):
        """Save the current repository data to a file using pickle.

        Args:
            filename (str): The name of the file to save to (without extension).
            dir (str, optional): The directory to save the file in. Defaults to the current directory.
        """
        full_filename = os.path.join(dir, filename + ".pkl")
        try:
            os.makedirs(dir, exist_ok=True) # Ensure directory exists
            with open(full_filename, 'wb') as f:
                pickle.dump(self._data, f)
            print(f"Repository data saved to '{full_filename}'")
        except Exception as e:
            print(f"Error saving repository data to '{full_filename}': {e}")