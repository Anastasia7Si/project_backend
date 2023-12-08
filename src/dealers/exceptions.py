class NoDealer(Exception):
    def __init__(self, id: int):
        self.id = id


class NoDealers(Exception):
    pass


class NoDealerProduct(Exception):
    def __init__(self, id: int):
        self.id = id


class NoDealersProducts(Exception):
    pass


class NoBodyRequestException(Exception):
    pass
