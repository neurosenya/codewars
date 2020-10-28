from itertools import groupby

class Dinglemouse:

    def __init__(self, queues, capacity):
        self.floors_queues = [list(floor) for floor in queues]
        self.capacity = capacity

    def theLift(self):
        # check left people on floors
        ZeroFloor, CurrFloor = 0, 0
        LastFloor = len(self.floors_queues)
        lift = []
        LiftStops = [0]
        # empty floors check
        while [True for floor in self.floors_queues
               if any( [isinstance(j, int) for j in floor] ) ]:
############################################################################################
#----------------------------------------- From Top to Bottom --------------------------------------------
            for i in range(ZeroFloor, LastFloor):
                visited = False
                CurrFloor = i
#------------------------------------------ take out people----------------------------------------------
                if any([True for person in lift if int(person) == CurrFloor]):
                    LiftStops.append(CurrFloor)
                    visited = True
                for person in lift:
                    if person == CurrFloor:
                        self.floors_queues[CurrFloor].append(str(person))
                lift[:] = [x for x in lift if x != CurrFloor]
#----------------------------------------- take in people--------------------------------------------
                entered_lift = []
                # lift stop
                if any([True for person in self.floors_queues[CurrFloor]
                    if int(person) > CurrFloor]):
                    if not visited:
                        LiftStops.append(CurrFloor)
                for person in self.floors_queues[CurrFloor]:
                    # full lift condition
                    if len(lift) < self.capacity:
                        if int(person) > CurrFloor:
                            lift.append(person)
                            entered_lift.append(person)
                    else: break

#------------------------------------- remove people from the floor----------------------------------
                for j in entered_lift:
                    self.floors_queues[CurrFloor].remove(j)
                # empty lift and floors above
                floors_above = [True for floor in self.floors_queues[i+1:]
                                if floor]
                if not lift and not floors_above:
                    break
##########################################################################################
#--------------------------------From Top to Bottom---------------------------------------
            print(self.floors_queues)
            for i in range(CurrFloor, ZeroFloor-1, -1):
                CurrFloor = i
                visited = False
#---------------------------------------take out people -----------------------------------------------
                if any([True for person in lift if int(person) == CurrFloor]):
                    LiftStops.append(CurrFloor)
                    visited = True
                for person in lift:
                    if person == CurrFloor:
                        self.floors_queues[CurrFloor].append(str(person))
                lift[:] = [x for x in lift if x != CurrFloor]
# ---------------------------------------take in people------------------------------------
                entered_lift = []
                if any([True for person in self.floors_queues[CurrFloor] if int(person) < CurrFloor]):
                    if  not visited:
                        LiftStops.append(CurrFloor)
                for person in self.floors_queues[CurrFloor]:
                    # full lift condition
                    if len(lift) < self.capacity:
                        if int(person) < CurrFloor:
                            lift.append(person)
                            entered_lift.append(person)
                    else: break
#--------------------------------  remove people from the floor -----------------------------------------
                for j in entered_lift:
                    self.floors_queues[CurrFloor].remove(j)
                # empty lift and floors below
                floors_below = [True for floor in self.floors_queues[:i]
                                if floor]
                if not lift and not floors_below:
                    break
            print(self.floors_queues)
        # remove consecutive duplicate elements
        LiftStops.append(ZeroFloor)
        LiftStops[:] = [i[0] for i in groupby(LiftStops)]
        return LiftStops


test0 = [ [], [6, 5, 2], [4], [], [0, 0, 0], [], [], [3, 6, 4, 5, 6], [], [10, 2], [1, 4, 3, 2]]
test1 = [ [], [], [5, 5, 5], [], [], [], [] ]
test2 = [ [], [], [1, 1], [], [], [], []]
test3 = [ [], [3], [4], [], [5], [], []]
test4 = [ [], [0], [], [], [2], [3], []]
lift = Dinglemouse(test0, 3)
print(test0)
print(lift.theLift())









