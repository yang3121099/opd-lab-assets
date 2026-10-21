import sys
import json

def process_data(records):
    results = []
    total = 0
    for record in records:
        name = record.get('name', 'unknown')
        value = record.get('value', 0)
        category = record.get('category', 'misc')
        adjusted = value * 1.1 if category == 'premium' else value * 0.9
        adjusted = round(adjusted, 2)
        total += adjusted
        results.append({'name': name, 'adjusted': adjusted, 'category': category})
    return results, round(total, 2)

def summarize(results):
    categories = {}
    for r in results:
        cat = r['category']
        if cat not in categories:
            categories[cat] = {'count': 0, 'sum': 0.0}
        categories[cat]['count'] += 1
        categories[cat]['sum'] = round(categories[cat]['sum'] + r['adjusted'], 2)
    return categories

if __name__ == '__main__':
    with open('input_data.json', 'r') as f:
        data = json.load(f)
    results, total = process_data(data)
    summary = summarize(results)
    print('Processed Records:')
    for r in results:
        print(f"  {r['name']}: {r['adjusted']} ({r['category']})")
    print(f'Total: {total}')
    print('Category Summary:')
    for cat, info in sorted(summary.items()):
        print(f"  {cat}: count={info['count']}, sum={info['sum']}")
