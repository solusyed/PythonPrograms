from src.inheritance.Multiplr.parent1_file import Parent1File
from src.inheritance.Multiplr.parent_file import ParentFile


class ChildFile(ParentFile, Parent1File):

    def __init__(self, name, value, start, end, mid):
        ParentFile.__init__(self, name, value)
        Parent1File.__init__(self, start, end, mid)


