class Car:
    def __init__(self, comfort_class: int, clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center: float, clean_power: int,
                 average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def rate_service(self, new_rate: float) -> None:
        total_score = self.average_rating * self.count_of_ratings
        total_score += new_rate
        self.count_of_ratings += 1
        self.average_rating = round(total_score / self.count_of_ratings, 1)

    def calculate_washing_price(self, car: Car) -> float:
        """Calcula o custo de uma única lavagem sem modificar o carro."""
        if car.clean_mark >= self.clean_power:
            return 0.0  # não precisa de lavagem

        price = (
            car.comfort_class 
            * (self.clean_power - car.clean_mark) 
            * self.average_rating 
            / self.distance_from_city_center
        )
        return round(price, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        """
        Atende uma lista de carros, lavando-os via
        wash_single_car e somando a renda.
        """
        total_income = 0.0
        for car in cars:
            total_income += self.wash_single_car(car)  # chama o método aqui
        return round(total_income, 1)

    def wash_single_car(self, car: Car) -> float:
        """Lava um único carro e retorna o preço da lavagem."""
        if car.clean_mark < self.clean_power:
            price = self.calculate_washing_price(car)
            car.clean_mark = self.clean_power
            return price
        return 0.0
