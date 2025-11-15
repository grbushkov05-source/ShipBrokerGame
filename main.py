from game.fleet import Fleet
from game.routes import generate_routes
from game.events import random_event
from game.utils import print_header, choose_from_list

def main():
    fleet = Fleet()
    balance = 5000
    weeks = 10

    print_header("Ship Broker Simulator")
    print(f"Стартовый баланс: {balance}$\nСезон: {weeks} недель\n")

    for week in range(1, weeks + 1):
        print_header(f"Неделя {week}")
        routes = generate_routes()

        # Выбор рейса
        route_idx = choose_from_list(routes, "Доступные рейсы. Выберите рейс: ")
        route = routes[route_idx]

        # Выбор судна
        ship_idx = choose_from_list(fleet.ships, "Доступные суда. Выберите судно: ")
        ship = fleet.ships[ship_idx]

        # Расчёт прибыли
        profit = route.reward - ship.cost_per_week
        event_name, impact = random_event()
        profit += profit * impact
        balance += profit

        print(f"\nСобытие недели: {event_name}")
        print(f"Прибыль за рейс: {profit:.2f}$")
        print(f"Баланс: {balance:.2f}$\n")

    print_header("Игра окончена")
    print(f"Итоговый баланс: {balance:.2f}$")

if __name__ == "__main__":
    main()
