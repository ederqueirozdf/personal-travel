# Skill: travel-planner

## Summary
Use this skill to decide the best airfare option across money and miles.

## Decision rules
- compare all relevant windows within the accepted range
- prefer options with fewer stops when total cost is close
- include baggage in the total cost calculation
- penalize routes with unrealistic layovers or very long total travel time
- rank by real value, not only by base fare

## Response template
1. Best option in money
2. Best option in miles
3. Best mixed option if one is favorable
4. Summary of savings vs original dates
5. Risks and trade-offs
