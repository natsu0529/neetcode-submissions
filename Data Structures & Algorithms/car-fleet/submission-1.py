class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - p) / s for p,s in sorted(zip(position,speed),reverse=True)]
        maxi = 0
        fleet = 0
        print(times)
        for t in times:
            if t > maxi:
                fleet += 1
                maxi = t
        return fleet
        