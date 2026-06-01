
def with_garage(cls):
    class building_class(cls):
        def __init__(self,n_rooms):
            super().__init__(n_rooms)
            self.has_garage=True

    return building_class

@with_garage
class House:
    def __init__(self,n_rooms):
        self.n_rooms=n_rooms

