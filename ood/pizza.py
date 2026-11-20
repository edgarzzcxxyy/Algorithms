"""
Pizza Pricing
Category: OOD
Core design: pizza class holding topping counts in a dict; rule methods
(multiExclude, toppingPricingRule, taxRate) kept separate from add_topping and
final_price.

Rules: mushroom and cheeseburst exclude each other; cheeseburst capped at 1 on
small and 2 on medium; per-topping pricing (cheeseburst 100 then 70 each, corn
cheaper on medium / large); tax x1.3 with cheeseburst, x0.9 with mushroom;
final price rounded.
"""
import collections

Topping = {
    "cheeseburst":100, "corn": 50, "onion": 30,
    "capsicum": 50, "pineapple": 60, "mushroom": 40,
}


class pizza:
    def __init__(self, price, size, taxPercent):
        self.base = price
        self.size = size
        self.toppings = collections.defaultdict(int)
        self.taxPercent = taxPercent 

    
    def multiExclude(self, topping, count):
        if topping == "mushroom" and "cheeseburst" in self.toppings:
            return False
        if topping == "cheeseburst":
            if "mushroom" in self.toppings:return False 
        
            existing = self.toppings.get("cheeseburst", 0)
            if self.size == "small" and existing + count > 1:
                return False
            if self.size == "medium" and existing + count > 2:
                return False 
        
        return True
    
    def toppingPricingRule(self, topping):
        if topping == "cheeseburst":
            return 100 + (self.toppings[topping] - 1) * 70
    
        if topping == "corn":
            if self.size == "medium":
                return 50 + (self.toppings[topping] - 1) * 40
            if self.size == "large":
                return 20 * (self.toppings[topping]) 
        
        return Topping[topping] * self.toppings[topping]
    
    def taxRate(self):
        rate = self.taxPercent
        if "cheeseburst" in self.toppings:
            rate *= 1.3
        if "mushroom" in self.toppings:
            rate *= 0.9
        return rate

    def add_topping(self, topping, count):
        if self.multiExclude(topping, count):
            self.toppings[topping] += count
            return True
        return False
    
    def final_price(self):
        toppingPrice = sum(
            self.toppingPricingRule(topping) for topping in self.toppings
        )
        rate = self.taxRate()
        total = self.base + toppingPrice
        return int((total) * (rate/100) + total + 0.5)

# 1. Cheeseburst uplift + onion
p = pizza(200, "medium", 10)
assert p.add_topping("cheeseburst", 1) == True
assert p.add_topping("onion", 2) == True
assert p.final_price() == 407
print(f"1: {p.final_price()}")

# 2. Mushroom blocks cheeseburst
q = pizza(350, "medium", 8)
assert q.add_topping("mushroom", 2) == True
assert q.add_topping("cheeseburst", 1) == False
assert q.final_price() == 461
print(f"2: {q.final_price()}")

# 3. Cheeseburst capped at 1 on small
s = pizza(200, "small", 10)
assert s.add_topping("cheeseburst", 1) == True
assert s.add_topping("cheeseburst", 1) == False
print("3: small cap passed")

# 4. Cheeseburst capped at 2 on medium
m = pizza(200, "medium", 10)
assert m.add_topping("cheeseburst", 2) == True
assert m.add_topping("cheeseburst", 1) == False
print("4: medium cap passed")

# 5. Mushroom tax reduction: 10 → 9
mr = pizza(200, "large", 10)
mr.add_topping("mushroom", 1)
assert mr.final_price() == 262
print(f"5: {mr.final_price()}")

# 6. Corn on medium: 50 + 40 + 40 = 130
cm = pizza(200, "medium", 0)
cm.add_topping("corn", 3)
assert cm.final_price() == 330
print(f"6: {cm.final_price()}")

# 7. Corn on large: 20 * 3 = 60
cl = pizza(200, "large", 0)
cl.add_topping("corn", 3)
assert cl.final_price() == 260
print(f"7: {cl.final_price()}")

# 8. Calling final_price twice gives same result
p2 = pizza(200, "medium", 10)
p2.add_topping("cheeseburst", 1)
assert p2.final_price() == p2.final_price()
print("8: idempotent passed")

# 9. No toppings — just base + tax
plain = pizza(200, "small", 10)
assert plain.final_price() == 220
print(f"9: plain pizza: {plain.final_price()}")

# 10. Reverse exclusion — cheeseburst blocks mushroom
r = pizza(200, "large", 10)
r.add_topping("cheeseburst", 1)
assert r.add_topping("mushroom", 1) == False
print("10: reverse exclusion passed")

print("\nAll tests passed!")