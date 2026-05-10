class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(0, len(position)):
            cars.append([position[i], speed[i]])

        cars.sort(key=lambda pair:pair[0], reverse=True)

        fleetTimes = [(target - cars[0][0]) / cars[0][1]]

        for i in range(1, len(cars)):
            if (target - cars[i][0]) / cars[i][1] > fleetTimes[-1]:
                fleetTimes.append((target - cars[i][0]) / cars[i][1])
                print("appending: ", (target - cars[i][0]) / cars[i][1])
            else:
                print("NOT appending: ", (target - cars[i][0]) / cars[i][1])

        return len(fleetTimes)