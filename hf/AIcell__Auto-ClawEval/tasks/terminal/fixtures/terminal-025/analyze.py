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
        results.append({
            'name': name,
            'original': value,
            'adjusted': adjusted,
            'category': category
        })
    summary = {
        'count': len(results),
        'total': round(total, 2),
        'average': round(total / len(results), 2) if results else 0
    }
    return results, summary

def main():
    with open('input_data.json', 'r') as f:
        data = json.load(f)
    records = data.get('records', [])
    results, summary = process_data(records)
    print('Processed Records:')
    for r in results:
        print(f"  {r['name']}: original={r['original']}, adjusted={r['adjusted']}, category={r['category']}")
    print()
    print('Summary:')
    print(f"  Count: {summary['count']}")
    print(f"  Total: {summary['total']}")
    print(f"  Average: {summary['average']}")

if __name__ == '__main__':
    main()
