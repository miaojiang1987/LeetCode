class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        m = 0
        for i in range(len(trips)):
            dropoff = trips[i][2]
            if m < dropoff:
                m = dropoff

		# Step 2: Mark the map locations where drop offs and pickups occur
        map = [0] * (m+1)
        for trip in trips:
            new_passengers, curr_loc, dropoff_loc = trip
            map[curr_loc] += new_passengers
            map[dropoff_loc] -= new_passengers
        
		# Step 3: Now we traverse in a linear fashion and see whether at any given point, we exceed the car's limits
        curr = 0
        for p in map:
            curr += p
            if curr > capacity:
                return False
        return True