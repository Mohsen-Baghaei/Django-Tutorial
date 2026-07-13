class Employee():
    def __init__(self, name: str, lastname: str, salary: int = 3000) -> None:
        self.name = name
        self.lastname = lastname
        self.salary = salary
    
    def __str__(self) -> str:
        return f"{self.name} {self.lastname} salary: {self.salary}"
    