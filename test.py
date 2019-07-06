from utils.roll import roll
import logging


logging.basicConfig(
    format='%(asctime)s : %(message)s',
    level=logging.INFO)

print(roll('D6'))
print(roll(''))
print(roll(''))
print(roll(''))
print(roll('D12'))
