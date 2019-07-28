class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        # corner case when source == destination and no edges
        if source == destination and len(edges) == 0:
            return True
        # record the adjacent nodes for each node
        connections = []
        for i in range(n):
            connections.append([])
        for src, desc in edges:
            connections[src].append(desc)
        # when destination has adjacent nodes, it must fail
        if len(connections[destination]) > 0:
            return False
        # for each adjacent nodes from source, dfs
        count = 0
        for child in connections[source]:
            # cache visited nodes for cycle detection
            hs = set()
			# dfs
            stack = [child]
            while len(stack) > 0:
                pop = stack.pop()
                # cycle detection
                if pop != destination and pop in hs:
                    return False
                hs.add(pop)
                # when we reach to a leaf, check if it is our destination
                if len(connections[pop]) == 0:
                    if pop == destination:
                        count += 1
                    else:
                        return False
                # traverse
                for node in connections[pop]:
                    stack.append(node)
		# count of paths must be > 0
        return count > 0