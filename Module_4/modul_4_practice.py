"""import sys

for path in sys.path:
    print(path)"""
from datetime import datetime
from dis import dis

def divide(divident, divisor):
    if divisor == 0:
        return 'Ошибка'
    else:
        return divident / divisor

print(divide(5, 6))

