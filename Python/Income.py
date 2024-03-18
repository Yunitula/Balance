class Income:
    def __init__(self, source , type, amount) -> None:
        self.source = source
        self.type = type
        self.amount = amount
    
    def __repr__(self) -> str:
        return f"<income {self.source}, {self.type} , npr:{self.amount:.2f}>"