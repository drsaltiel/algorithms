'''
solution to the knapsack problem
'''

import sys
import random


def make_random_sack(l):
  items = []
  for i in range(l):
    items.append((random.randint(0,100), random.randint(0,100)))
  return items


possible_sack = {}

def m(n, cap):
    if cap == 0 or len(n) == 0:
        return 0
    else:
        best_item = 0
        for value, weight in n:
            if cap-weight < 0:
                continue
            _   = n.remove((value, weight))
            if possible_sac.has_key(str((n.sort(), cap-weight))):
                new_value = possible_sac[str((n.sort(), cap-weight))] + value
            else:
                m_score =  m(n, cap-weight)
                new_value = m_score + value
                possible_sac[str((n.sort(), cap-weight))] = m_score
            n.append((value, weight))
            if new_value > best_item:
                best_item = new_value
        return best_item

if __name__ == "__main__":
    print m(make_random_sac(10), int(sys.argv[1]))
