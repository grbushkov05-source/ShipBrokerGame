import random

def random_event():
    events = [
        ("Шторм", -0.3),
        ("Рост цен на топливо", -0.2),
        ("Плавное путешествие", 0),
        ("Высокий спрос — бонус", 0.2)
    ]
    return random.choice(events)
