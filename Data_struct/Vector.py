class Vector:
    def __init__(self, *args):
        self._coords=list(args)

    def __str__(self):
        return str(tuple(self._coords))

    def __len__(self): #객체의 길이 받기
        return len(self._coords)

    def __getitem__(self, item):
        return self._coords[item]

    def __setitem__(self, key, value):
        self._coords[key] = value