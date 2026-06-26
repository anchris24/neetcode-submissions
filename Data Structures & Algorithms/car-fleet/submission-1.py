class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)

        count = 1
        prev = cars[0][1]
        for i in range(1, len(cars)):
            _, t = cars[i]

            if t > prev:
                count += 1
                prev = t
        
        return count
