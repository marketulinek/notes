# Classes
class Flight():
  def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []

  def add_passenger(self, name):
    if not self.open_seats():
      return False
    self.passengers.append(name)
    return True

  def open_seats(self):
    return self.capacity - len(self.passengers)

flight = Flight(3)

people = ['Harry', 'Ron', 'Hermione', 'Draco']
for person in people:
  success = flight.add_passenger(person)
  if success:
    print(f'Added {person} to flight successfully.')
  else:
    print(f'No available seats for {person}.')


# Decorators
def announce(f):
  def wrapper():
    print('About to run the function...')
    f()
    print('Done with the function.')
  return wrapper

@announce
def hello():
  print('Hello, world!')

hello()


# Lambda
people = [
  {'name': 'Harry', 'house': 'Gryffindor'},
  {'name': 'Cho', 'house': 'Ravenclaw'},
  {'name': 'Draco', 'house': 'Slytherin'}
]

# Version 1 of how to sort people
def f(person):
  return person['name']

people.sort(key=f)

# Version 2 of how to sort people (short version)
#                       input: output
people.sort(key=lambda person: person['name'])


# Exceptions
import sys

try:
  x = int(input('x: '))
  y = int(input('y: '))
except ValueError:
  print('Error: Invalid input.')
  sys.exit(1)

try:
  result = x / y
except ZeroDivisionError:
  print('Error: Cannot divide by 0.')
  sys exit(1)
print(people)
