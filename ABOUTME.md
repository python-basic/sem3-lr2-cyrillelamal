## Кирилл

* Python3
* Django
* Flask
* Пережил пары Швецкого
* etc

[Portfolio](https://github.com/cyrillelamal/cyrillelamal.github.io "Cyrille's portfolio")

![my motivation](https://pp.userapi.com/c848732/v848732714/8bab4/NC3mRisWX2k.jpg "Motivation")

### Task
```Python
import math

def get_sides():
  a = float(input('a side: '))
  b = float(input('b side: '))
  c = float(input('c side: '))
  return a, b, c


def heron(a, b, c):
  p = 1/2 * (a + b + c)
  return math.sqrt(p*(p-a)*(p-b)*(p-c))
```
