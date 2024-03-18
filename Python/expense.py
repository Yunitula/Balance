class Expense:
   
    def  __init__(self, name, category, amount, type) -> None:
        self.name = name
        self.category = category
        self.amount = amount
        self.type = type

    def __repr__(self) -> str:
        return f"<expense: {self.name} ,{self.category},Npr{self.amount:.2f}, {self.type} "