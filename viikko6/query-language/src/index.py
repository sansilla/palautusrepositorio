from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    #matcher = And(
        #HasAtLeast(5, "goals"),
        #HasAtLeast(20, "assists"),
        #PlaysIn("PHI")
    #)

    #matcher = And(
        #Not(HasAtLeast(2, "goals")),
        #PlaysIn("NYR")
    #)

    #filtered_with_all = stats.matches(All())
    #print(len(filtered_with_all))

    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )


    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
