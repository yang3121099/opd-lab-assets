import sys
import json

def process_data(records):
    results = []
    total = 0
    for record in records:
        name = record.get('name', 'Unknown')
        value = record.get('value', 0)
        category = record.get('category', 'misc')
        adjusted = value * 1.1 if category == 'premium' else value * 0.9
        total += adjusted
        results.append({
            'name': name,
            'original': value,
            'adjusted': round(adjusted, 2),
            'category': category
        })
    return results, round(total, 2)

def summarize(results, total):
    categories = {}
    for r in results:
        cat = r['category']
        if cat not in categories:
            categories[cat] = {'count': 0, 'sum': 0.0}
        categories[cat]['count'] += 1
        categories[cat]['sum'] = round(categories[cat]['sum'] + r['adjusted'], 2)
    print('=== Summary ===')
    for cat, stats in sorted(categories.items()):
        print(f"Category '{cat}': {stats['count']} items, total={stats['sum']}")
    print(f'Grand total: {total}')
    print(f'Record count: {len(results)}')

if __name__ == '__main__':
    data = [
        {'name': 'Alpha', 'value': 100, 'category': 'premium'},
        {'name': 'Beta', 'value': 200, 'category': 'standard'},
        {'name': 'Gamma', 'value': 150, 'category': 'premium'},
        {'name': 'Delta', 'value': 80, 'category': 'misc'},
        {'name': 'Epsilon', 'value': 300, 'category': 'standard'},
    ]
    results, total = process_data(data)
    summarize(results, total)
