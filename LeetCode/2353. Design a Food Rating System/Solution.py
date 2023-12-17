class Food:
    def __init__(self, name: str, cuisine: str, rating: int):
        self.name = name
        self.rating = rating
        self.cuisine = cuisine

    def __str__(self):
        return f"{self.name} | {self.cuisine} | {self.rating}"


class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.cuisines = {}
        self.foods = {}
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            tempFood = Food(food, cuisine, rating)

            if cuisine not in self.cuisines:
                self.cuisines[cuisine] = {}

            if rating not in self.cuisines[cuisine]:
                self.cuisines[cuisine][rating] = []

            self.cuisines[cuisine][rating].append(tempFood)

            self.foods[food] = tempFood

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.foods[food].rating
        
        # Removing the food from the old rating
        self.cuisines[self.foods[food].cuisine][oldRating].remove(self.foods[food])
        
        if len(self.cuisines[self.foods[food].cuisine][oldRating]) == 0:
            self.cuisines[self.foods[food].cuisine].pop(oldRating)
        
        # Adding the food to the new rating
        if newRating not in self.cuisines[self.foods[food].cuisine]:
            self.cuisines[self.foods[food].cuisine][newRating] = []

        self.cuisines[self.foods[food].cuisine][newRating].append(self.foods[food])
        self.foods[food].rating = newRating

    def highestRated(self, cuisine: str) -> str:

        maxRating = max(self.cuisines[cuisine].keys())
        foods = self.cuisines[cuisine][maxRating]

        print(maxRating)
        print(*[str(f) for f in foods])

        minFood = foods[0]
        for food in foods[1:]:
            if food.name < minFood.name:
                minFood = food

        return minFood.name


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
