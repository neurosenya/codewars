from itertools import groupby

class Dinglemouse:

    def __init__(self, queues, capacity):
        self.floors_queues = [list(floor) for floor in queues]
        self.capacity = capacity
    def onedirection(start_floor):
       for i in range(ZeroFloor, start_floor):
           CurrFloor = i
           LiftStops.append(CurrFloor)
           # take out people
           for person in lift:
               if person == CurrFloor:
                   self.floors_queues[CurrFloor].append(str(person))
           lift[:] = [x for x in lift if x != CurrFloor]
           # take in people
           entered_lift = []
           for person in self.floors_queues[CurrFloor]:
               # full lift condition
               if len(lift) < self.capacity:
                   if int(person) > CurrFloor:
                       lift.append(person)
                       entered_lift.append(person)
               else: break
           # remove people from the floor
           for j in entered_lift:
               self.floors_queues[CurrFloor].remove(j)
           # empty lift and floors above
           floors_above = [True for floor in self.floors_queues[i+1:]
                           if floor]
           if not lift and not floors_above:
               break
    def theLift(self):
        # check left people on floors
        ZeroFloor, CurrFloor = 0, 0
        LastFloor = len(self.floors_queues)
        lift = []
        LiftStops = []
        # empty floors check
        while [True for floor in self.floors_queues
               if any( [isinstance(j, int) for j in floor] ) ]:
            print(self.floors_queues)
            # bottom-top
            for i in range(ZeroFloor, LastFloor):
                CurrFloor = i
                LiftStops.append(CurrFloor)
                # take out people
                for person in lift:
                    if person == CurrFloor:
                        self.floors_queues[CurrFloor].append(str(person))
                lift[:] = [x for x in lift if x != CurrFloor]
                # take in people
                entered_lift = []
                for person in self.floors_queues[CurrFloor]:
                    # full lift condition
                    if len(lift) < self.capacity:
                        if int(person) > CurrFloor:
                            lift.append(person)
                            entered_lift.append(person)
                    else: break
                # remove people from the floor
                for j in entered_lift:
                    self.floors_queues[CurrFloor].remove(j)
                # empty lift and floors above
                floors_above = [True for floor in self.floors_queues[i+1:]
                                if floor]
                if not lift and not floors_above:
                    break
                # top-bottom
            print(self.floors_queues)
            for i in range(CurrFloor, ZeroFloor-1, -1):
                CurrFloor = i
                LiftStops.append(CurrFloor)
                # take out people
                for person in lift:
                    if person == CurrFloor:
                        self.floors_queues[CurrFloor].append(str(person))
                lift[:] = [x for x in lift if x != CurrFloor]
                # take in people
                entered_lift = []
                for person in self.floors_queues[CurrFloor]:
                    # full lift condition
                    if len(lift) < self.capacity:
                        if int(person) < CurrFloor:
                            lift.append(person)
                            entered_lift.append(person)
                    else: break
                # remove people from the floor
                for j in entered_lift:
                    self.floors_queues[CurrFloor].remove(j)
                # empty lift and floors below
                floors_below = [True for floor in self.floors_queues[:i]
                                if floor]
                if not lift and not floors_below:
                    break
            print(self.floors_queues)
        LiftStops.extend([x for x in range(CurrFloor, ZeroFloor-1, -1)])
        # remove consecutive duplicate elements
        LiftStops[:] = [i[0] for i in groupby(LiftStops)]
        return LiftStops


queues = [ [], [6, 5, 2], [4], [], [0, 0, 0], [], [], [3, 6, 4, 5, 6], [], [10, 2], [1, 4, 3, 2]] 
lift = Dinglemouse(queues, 3)
print(queues)
print(lift.theLift())









