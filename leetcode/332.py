"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        def find_eulerian_tour(graph):
            tour = []
            find_tour('JFK', graph, tour)
            return tour

        def find_tour(u, E, tour):
            for (a, b) in E:
                if a == u:
                    E.remove((a, b))
                    #E.sort(reverse=False, key=lambda x: x[1])
                    find_tour(b, E, tour)
            # for (a, b) in E:
            #     if b == u:
            #         E.remove((a, b))
            #         #E.sort(reverse=False, key=lambda x: x[1])
            #         find_tour(a, E, tour)
            tour.insert(0, u)

        return (find_eulerian_tour(sorted([(el[0],el[1]) for el in tickets], key = lambda x:x[1])))

        #
        # from collections import defaultdict
        #
        # ticketsProcessed = defaultdict(list)
        # for ticket in tickets:
        #     ticketsProcessed[ticket[0]].append(ticket[1])
        #
        # # visited.add('JFK')
        #
        #
        # def DFS(node):
        #     def DFSUtil(node):
        #         visited.add(node)
        #         if node in ticketsProcessed.keys():
        #             for destanation in ticketsProcessed[node]:
        #                 if destanation not in visited:
        #                     DFSUtil(destanation)
        #             iteniary.insert(0, node)
        #
        #     visited = set()
        #     iteniary = []
        #
        #     for destanation in ticketsProcessed.keys():
        #         if destanation not in visited:
        #             DFSUtil(node)
        #     return iteniary
        #
        # return DFS('JFK')
        #
        # # while True:
        # #     currentcity = iteniaty[-1]
        # #     try:
        # #         connection = ticketsProcessed[currentcity][0]
        # #     except (KeyError, IndexError):
        # #         return iteniaty
        # #     iteniaty.append(connection)
        # #     # print( ticketsProcessed[currentcity])
        # #     ticketsProcessed[currentcity] = list(set(ticketsProcessed[currentcity]) - set([connection]))
        #

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
tickets = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]

#tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

print(Solution().findItinerary(tickets))


["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","ADL","TIA","AUA","AXA","TIA","EZE","HBA"]

["JFK","AXA","AUA","ADL","ANU","AUA","ANU","EZE","ADL","EZE","ANU","JFK","AXA","EZE","TIA","AUA","AXA","TIA","ADL","EZE","HBA"]

['JFK', 'AXA', 'AUA', 'ADL', 'ANU', 'AUA', 'ANU', 'EZE', 'ADL', 'EZE', 'ANU', 'JFK', 'AXA', 'EZE', 'ADL', 'TIA', 'AUA', 'AXA', 'TIA', 'EZE', 'HBA']