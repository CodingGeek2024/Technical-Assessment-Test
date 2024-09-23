from typing import List, Dict, Callable
from collections import defaultdict

def aggregate_data(data: List[Dict], key: str, aggregator: Callable):
    # Create a defaultdict to group values by key
    grouped_data = defaultdict(list)

    # Group the data by the specified key
    for item in data:
        if key in item:
            grouped_data[item[key]].append(item)

    # Apply the aggregator function to each group
    result = {}
    for group_key, group_items in grouped_data.items():
        # Extract the values to aggregate (all items except the grouping key)
        values_to_aggregate = [
            {k: v for k, v in item.items() if k != key}
            for item in group_items
        ]
        # Apply the aggregator function
        result[group_key] = aggregator(values_to_aggregate)

    return result
