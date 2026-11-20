# OOD (Object-Oriented Design)

**Core idea:** model the entities as classes, keep state in the right object, and use hash maps for lookups by id / code / ticket. Keep business rules (pricing, limits, exclusions) in their own methods so new rules don't touch the main flow.

**Common pieces across these problems:**
- Entity classes with a status flag (`occupied`, `active`)
- Hash map from an external id (code, ticket, vehicle number) to the object or its id
- Linear scan to find the first free resource of a type
- Rule methods separated from the public API

| Problem | Core design | Main operations |
|---------|-------------|-----------------|
| [Locker](locker.py) | box / token / locker; map code → token; token expiry | deposit, pickUp, expiredCleanUp |
| [Parking Lot](parking_lot.py) | parkingSpot / parkingLot; maps spot id → spot, ticket → spot id, vehicle → spot id | park, remove, searchVehicle, get_freeCounts |
| [Pizza Pricing](pizza.py) | pizza with topping counts; separate exclusion, pricing and tax rule methods | add_topping, final_price |
