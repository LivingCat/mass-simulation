"""
Class to represent an Actor, its information, decision-making process, and behaviour.
"""

from abc import ABC
from typing import List, Tuple
from collections import defaultdict


class AbstractActor(ABC):

    TIME_INDEX = 0
    NODE_INDEX = 1

    base_route: List[int]

    # Tuple[time actor arrived to node, node]
    traveled_nodes: List[Tuple[float, int]]

    route_travel_time: defaultdict
    total_travel_time: float

    static_model_id = 1

    def __init__(self, route: List[int]):
        self.base_route = route
        self.route_travel_time = defaultdict(lambda: 0.0)
        self.total_travel_time = 0.0
        self.start_time = 0.0
        """"Initializer for the ID of all actor models"""
        self.actor_id = AbstractActor.static_model_id
        AbstractActor.static_model_id += 1

    def __repr__(self):
        return "A%d :: TI %.4f :: TTT %.4f" % (self.actor_id, round(self.start_time, 4), round(self.total_travel_time, 4))

    def add_time_for_edge(self, edge: Tuple[int, int], tt: float):
        self.route_travel_time[edge] = tt

    def update_total_tt(self):
        self.total_travel_time = sum(self.route_travel_time.values())

    def reached_dest(self) -> bool:
        """Check whether this actor reached its destination"""
        return self.base_route[-1] == self.traveled_nodes[-1][self.NODE_INDEX]

    def get_next_travel_edge(self, timestamp: float) -> Tuple[int, int]:
        """Gets the next edge to be traveled"""
        return (self.traveled_nodes[-1][self.NODE_INDEX],
                self.base_route[len(self.traveled_nodes)])

    def start_trip(self, at_time: float):
        """Make the actor start the route, at the given time"""
        self.start_time = at_time
        self.traveled_nodes = [(at_time, self.base_route[0])]   # Start node

    def travel(self, at_time: float, edge: Tuple[int, int]):
        """Makes the Actor travel the given edge"""
        if not self.traveled_nodes[-1][self.NODE_INDEX] == edge[0]:
            raise Exception

        self.traveled_nodes.append((at_time, edge[1]))

    def print_traveled_route(self):
        """Pretty printing of the Actor's traveled route"""
        print("Actor #%d:" % self.actor_id)
        print("\tNode: %d, timestamp: %f" %
              (self.traveled_nodes[0][self.NODE_INDEX],
               self.traveled_nodes[0][self.TIME_INDEX]))

        for i in range(1, len(self.traveled_nodes)):
            print("\tNode: %d, timestamp: %f (+%f)" %
                  (self.traveled_nodes[i][self.NODE_INDEX],
                   self.traveled_nodes[i][self.TIME_INDEX],
                   self.traveled_nodes[i][self.TIME_INDEX]
                   - self.traveled_nodes[i-1][self.TIME_INDEX]))

class CarActor(AbstractActor):

    emission : float
    total_route_emissions : float
    
    def __init__(self, route: List[int]):
        
        super().__init__(route)
        self.emission = 0.0
        self.total_route_emissions = 0.0

class BusActor(AbstractActor):

    emission: float
    total_route_emissions: float

    def __init__(self, route: List[int]):
        super().__init__(route)
        self.emission = 0.0
        self.total_route_emissions = 0.0


class SharedCarActor(AbstractActor):

    emission: float
    total_route_emissions: float

    def __init__(self, route: List[int]):
        super().__init__(route)
        self.emission = 0.0
        self.total_route_emissions = 0.0

