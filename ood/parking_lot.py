"""
Parking Lot
Category: OOD
Core design: parkingSpot / parkingLot classes; hash maps spot id -> spot,
ticket -> spot id, vehicle number -> spot id; linear scan for the first free
spot of the vehicle type.

Lot is floors x rows x cols; each spot is "type-active" (e.g. "4-1" = 4-wheeler,
active). park() returns the spot id "floor-row-col"; remove / search by spot id,
vehicle number or ticket id; free-spot count per floor and vehicle type.
"""
class parkingSpot:
    def __init__(self, floor, row, col, active, spot_type):
        self.floor = floor 
        self.row = row
        self.col = col
        self.spot_type = spot_type
        self.active = active
        self.occupied = False 

    def get_id(self):
        return f"{self.floor}-{self.row}-{self.col}"
    
    def is_free(self):
        return self.active and self.occupied == False

class parkingLot:
    def __init__(self, parking):
        self.floors = []
        self.spotId = {}
        self.ticketMap = {}
        self.veichleMap = {}

        for i in range(len(parking)):
            floorSpots = []
            for j in range(len(parking[0])):
                for k in range(len(parking[0][0])):
                    parts = parking[i][j][k].split("-")
                    spot_type = int(parts[0])
                    active = parts[1] == "1"
                    spot = parkingSpot(i,j,k,active, spot_type)
                    floorSpots.append(spot)
                    self.spotId[spot.get_id()] = spot
            self.floors.append(floorSpots)
    
    def park(self, vehicle_type, vehicle_number, ticket_id):
        for floor in self.floors:
            for s in floor:
                if s.spot_type == vehicle_type and s.is_free():
                    s.occupied = True
                    sid = s.get_id()
                    self.ticketMap[ticket_id] = sid
                    self.veichleMap[vehicle_number] = sid
                    return sid
        return ""
    
    def resolve(self,spot_id, vehicle_number, ticket_id):
        if spot_id: return spot_id
        if vehicle_number:
            return self.veichleMap.get(vehicle_number, "")
        if ticket_id:
            return self.ticketMap.get(ticket_id, "")
        return ""
    
    def remove(self, spot_id, vehicle_number, ticket_id):
        sid = self.resolve(spot_id, vehicle_number, ticket_id)
        if not sid:
            return 404
        spot = self.spotId.get(sid, None)
        if not spot or not spot.occupied:
            return 404
        spot.occupied = False
        return 201

    def searchVehicle(self, spot_id, vehicle_number, ticket_id):
        if spot_id:
            return spot_id if spot_id in self.spotId else ""
        if vehicle_number:
            return self.veichleMap.get(vehicle_number, "")
        if ticket_id:
            return self.ticketMap.get(ticket_id, "")
        return ""
    
    def get_freeCounts(self, floor, vehicle_type):
        return sum(1 for spot in self.floors[floor] if spot.spot_type == vehicle_type and spot.is_free())

parking = [[
    ["4-1", "4-1", "2-1", "2-0"],
    ["2-1", "4-1", "2-1", "2-1"],
    ["4-0", "2-1", "4-0", "2-1"],
    ["4-1", "4-1", "4-1", "2-1"]
]]
lot = parkingLot(parking)

# 1. Park 4-wheeler
s1 = lot.park(4, "bh234", "tkt4534")
assert s1 != ""
print(f"1: parked at {s1}")

# 2. Search by vehicle number
assert lot.searchVehicle("", "bh234", "") == s1
print("2: search by number passed")

# 3. Search by ticket
assert lot.searchVehicle("", "", "tkt4534") == s1
print("3: search by ticket passed")

# 4. Free count after parking
count = lot.get_freeCounts(0, 4)
print(f"4: free 4-wheeler: {count}")

# 5. Remove by vehicle number
assert lot.remove("", "bh234", "") == 201
assert lot.get_freeCounts(0, 4) == count + 1
print("5: remove passed")

# 6. Search after removal still works
assert lot.searchVehicle("", "bh234", "") == s1
print("6: search after removal passed")

# 7. Remove non-existent
assert lot.remove("9-9-9", "", "") == 404
print("7: non-existent = 404")

# 8. Park 2-wheeler
s2 = lot.park(2, "bike1", "t2")
assert s2 != ""
print(f"8: 2-wheeler at {s2}")

# 9. Remove by ticket
assert lot.remove("", "", "t2") == 201
print("9: remove by ticket passed")

# 10. Remove by spot_id
s3 = lot.park(4, "car2", "t3")
assert lot.remove(s3, "", "") == 201
print("10: remove by spot_id passed")

# 11. Inactive spot not assigned
lot2 = parkingLot([[["2-0"]]])
assert lot2.park(2, "x", "y") == ""
print("11: inactive spot skipped")

# 12. Two-floor counts
parking2 = [
    [["2-1", "4-1", "2-1", "4-1"],
     ["2-1", "2-1", "4-1", "4-1"]],
    [["2-1", "2-1", "4-1", "2-1"],
     ["4-1", "4-1", "2-1", "2-1"]]
]
lot3 = parkingLot(parking2)
assert lot3.get_freeCounts(0, 2) == 4
assert lot3.get_freeCounts(0, 4) == 4
assert lot3.get_freeCounts(1, 2) == 5
assert lot3.get_freeCounts(1, 4) == 3
print("12: two-floor counts correct")

print("\nAll tests passed!")

 



    