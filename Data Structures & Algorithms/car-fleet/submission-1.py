class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #sort by posn
        #time to reach posn is: (tgt - pos) / speed
        #u join fleet if u start before but ur time faster
        #"next car" is a car that starts before. if its slower than the curr slowest it starts its own fleet, 
        #else it joins up with an existing fleet
        cars = sorted(zip(position,speed),reverse=True)

        numfleets = 0
        slowest_time = 0

        for pos, vel in cars:
            time = (target - pos) / vel

            if time > slowest_time:
                numfleets += 1
                slowest_time = time
        
        return numfleets