# Control Structure - Task 2
def calculate_ticket_cost(category, num_tickets):
    prices = {
        'silver': 100,
        'gold': 200,
        'diamond': 500
    }

    category = category.lower()
    if category not in prices:
        return False, "Invalid category selected!", 0

    price = prices[category]
    total_cost = price * num_tickets
    return True, f"Total cost for {num_tickets} {category} tickets: ₹{total_cost}", total_cost