from .error import VectorError

__all__ = []

class Vector:
    """
    Implementation of a vector.
    """
    def __init__(self, row=None, column=None):
        if row and all(isinstance(k, list) for k in row):
            column = row
            row = None
        if row or column:
            self.row = row
            self.column = column
            self.__all__ = []
        else:
            self.row = self.column = None
            raise VectorError("Failed to parse vector: No arguments specified!")
        # self.size = [row, column]
    
    def transpose(self):
        if self.row: # Row vector
            return Vector(column=[[k] for k in self.row])
        return Vector(sum(self.column, []))
    
    def __add__(self, other):
        if self.row and other.row:
            return Vector([self.row[k] + other.row[k] for k in range(len(self.row))])
        if self.column and other.column:
            return (self.transpose() + other.transpose()).transpose()
        else:
            pass
    
    def subtract(self, other):
        pass

vector = Vector()
__all__.extend(vector.__all__)
