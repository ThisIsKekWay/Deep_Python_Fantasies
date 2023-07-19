names = ['pupa', 'lupa', 'bugalter']
payments = [120, 50, 300]
percents = ['15%', '12.8%', '13%']

print({names[i]: payments[i] * 0.01 * float(percents[i].replace('%', '')) for i in range(len(names))})
