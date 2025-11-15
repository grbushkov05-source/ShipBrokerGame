import random

class Route:
    def __init__(self, origin, destination, cargo_type, tonnage, reward):
        self.origin = origin
        self.destination = destination
        self.cargo_type = cargo_type
        self.tonnage = tonnage
        self.reward = reward

    def __str__(self):
        return f"{self.origin} → {self.destination}, {self.cargo_type}, {self.tonnage}т, Прибыль: {self.reward}$"

def generate_routes():
    ports = ["Rotterdam", "Singapore", "Shanghai", "Hamburg", "Dubai"]
    cargoes = ["Oil", "Grain", "Containers", "Electronics"]
    routes = []
    for _ in range(5):
        origin = random.choice(ports)
        dest = random.choice([p for p in ports if p != origin])
        cargo = random.choice(cargoes)
        tonnage = random.randint(1000, 7000)
        reward = tonnage * random.randint(10, 20)
        routes.append(Route(origin, dest, cargo, tonnage, reward))
    return routes
