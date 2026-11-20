"""
Locker (package locker)
Category: OOD
Core design: classes box / token / locker; hash map code -> token for O(1)
pickup; linear scan for a free box of the requested size; tokens expire after
7 days and expiredCleanUp frees their boxes.

Deposit into a free box of the requested size and get a 6-digit code; pick up
with the code. Invalid, reused and expired codes are rejected.
"""
from datetime import datetime, timedelta
import random

class box:
    def __init__(self, size):
        self.size = size
        self.occupied = False

class token:
    def __init__(self, code, box):
        self.code = code
        self.box = box
        self.expirary = datetime.now() + timedelta(days = 7)
    
    def isExpired(self):
        return datetime.now() >= self.expirary


class locker:
    def __init__(self, boxes:list[box]):
        self.boxes = boxes 
        self.dict = {}
    
    def deposit(self, size):
        for box in self.boxes:
            if box.size == size and box.occupied != True:
                box.occupied = True
                code = random.randint(100000, 999999)
                self.dict[code] = token(code, box)
                return code
        raise Exception(f"No avaliable {size} box")

    def pickUp(self, code):
        if code not in self.dict:
            raise Exception(f"Invalid Code")
        token = self.dict[code]
        if token.isExpired():
            raise Exception(f"Expired Code")
        token.box.occupied = False
        del self.dict[code]
    
    def expiredCleanUp(self):
        keys = [k for k, v in self.dict.items() if v.isExpired()]
        for key in keys:
            self.dict[key].box.occupied = False
            del self.dict[key]

boxes = [box("small"), box("small"), box("medium"), box("large")]
lkr = locker(boxes)

# 1. Basic deposit
code1 = lkr.deposit("small")
print(f"Deposit small: {code1}")

# 2. Successful pickup
lkr.pickUp(code1)
print("Pickup successful")

# 3. Reuse same code
try:
    lkr.pickUp(code1)
except:
    print("Reuse rejected")

# 4. Invalid code
try:
    lkr.pickUp(999999)
except:
    print("Invalid code rejected")

# 5. Fill all large then try again
code2 = lkr.deposit("large")
try:
    lkr.deposit("large")
except:
    print("No large available")

# 6. Expired code rejected
code3 = lkr.deposit("medium")
lkr.dict[code3].expirary = datetime.now() - timedelta(days=1)
try:
    lkr.pickUp(code3)
except:
    print("Expired rejected")

# 7. Cleanup frees expired boxes
lkr.expiredCleanUp()
code4 = lkr.deposit("medium")
print(f"After cleanup, medium works: {code4}")

# 8. Compartment reuse after pickup
lkr.pickUp(code2)
code5 = lkr.deposit("large")
print(f"Large reused: {code5}")

print("\nAll tests passed!")





