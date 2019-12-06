# orbit count checksums 
# the total number of direct orbits (like the one shown above) and indirect orbits.
from collections import defaultdict
from typing import List, Dict


T1 = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN""".split('\n')


def orbit_count_checksums(maps: List[str]) -> List:
    orbit_dict = {}
    
    for case in maps:
        left, right = case.split(')')
        orbit_dict[right] = left
    
    # total = 0
    # for key in orbit_dict.keys():
    set_list = []
    for key in ['YOU', 'SAN']:
        results = []
        find_orbits(orbit_dict, key, results)
        set_list.append(set(results))

    print(len(set_list[0] ^ set_list[1]))

    return results

def find_orbits(orbit_dict: Dict, key: str, results: List) -> List:
    try:
        results.append(orbit_dict[key])
        find_orbits(orbit_dict, orbit_dict[key], results)
    except:
        pass

# assert orbit_count_checksums(T1) == 42

with open('data/day6.txt') as f:
    lines = [line.strip() for line in f]

print(orbit_count_checksums(lines))
# print(orbit_count_checksums(T1))

