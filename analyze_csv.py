import csv
import statistics as stats
import sys

if len(sys.argv) < 2:
    print('Usage: python3 analyze_csv.py <csv_file>')
    sys.exit(1)

csv_file = sys.argv[1]

results = []  # list of tuples (feature, mean, median, stdev, min, max)
with open(csv_file, newline='') as f:
    reader = csv.reader(f)
    header = next(reader)  # sample identifiers
    _ = next(reader)       # class row or metadata
    for row in reader:
        label = row[0]
        try:
            values = [float(x) for x in row[1:] if x != '']
        except ValueError:
            continue
        if not values:
            continue
        mean = stats.mean(values)
        median = stats.median(values)
        stdev = stats.stdev(values) if len(values) > 1 else 0.0
        results.append((label, mean, median, stdev, min(values), max(values)))

output_file = 'analysis_summary.csv'
with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Feature', 'Mean', 'Median', 'Stdev', 'Min', 'Max'])
    writer.writerows(results)

print(f'Saved analysis to {output_file}')
