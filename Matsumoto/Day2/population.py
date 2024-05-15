import sys

POPULATION_RANKING = (
    "China", "India", "U.S.A", "Indonesia", "Pakistan",
    "Brazil", "Nigeria", "Bangladesh", "Russia", "Mexico"
)

rank = int(sys.argv[1])
print(POPULATION_RANKING[rank-1], end="")
