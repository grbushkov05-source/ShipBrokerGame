class Ship:
    def __init__(self, name, capacity, speed, cost_per_week):
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.cost_per_week = cost_per_week

    def __str__(self):
        return f"{self.name} (Груз: {self.capacity}т, Скорость: {self.speed} км/нед, Расход: {self.cost_per_week}$)"

class Fleet:
    def __init__(self):
        self.ships = [
            Ship("Neptune", 5000, 20, 1000),
            Ship("Poseidon", 3000, 25, 800),
            Ship("Odyssey", 7000, 18, 1500)
        ]
