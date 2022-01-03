from os import path
from pathlib import Path

#my_path = Path("emails")

#print(my_path.rmdir())

my_path = Path()
for file in my_path.glob('*.py'):
    print(file)


