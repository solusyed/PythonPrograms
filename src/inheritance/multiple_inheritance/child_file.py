from src.inheritance.multiple_inheritance.parent1_file import Parent1File
from src.inheritance.multiple_inheritance.parent_file import ParentFile


class ChildFile(ParentFile, Parent1File):

    def __init__(self, name, value, start, end, mid):
        ParentFile.__init__(self, name, value)
        Parent1File.__init__(self, start, end, mid)


