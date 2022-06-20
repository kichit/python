duration = int(input('Введите количество секунд: '))
seconds = 1
minutes = 60
hour = 3600
day = 86400

if 0 < duration < 60:
    print(duration, 'sec')
if duration == 60:
    print('1 min')
if 60 < duration < 3600:
    print(round(duration/60), 'min', duration % 60, 'sec')
if duration == 3600:
    print('1 hour')
if 3600 < duration < 86400:
    print(round(duration/3600), 'hours', round(duration/3600), 'min', duration % 60, 'sec')

if duration == 86400:
    print('1 day')

if 86400 < duration < 31556952:
    print(round(duration/86400), ' days', round(duration/86400), 'hours', round(duration/86400), 'min', duration % 60, 'sec')