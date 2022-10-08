
class Writer:

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
        
    def __str__(self) -> str:
        return f"{self.full_name}"

