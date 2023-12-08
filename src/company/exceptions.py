class NoProductException(Exception):
    def __init__(self, id: int):
        self.id = id


class NoAllProductsException(Exception):
    pass
