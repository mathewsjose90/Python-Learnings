# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # TODO: create an ordered dictionary of the teams
    teams=OrderedDict(sortedTeams)
    print(teams)

    # TODO: Use popitem to remove the top item
    team,win_lose=teams.popitem(False) #first item
    print(team,win_lose)

    # TODO: What are next the top 4 teams?
    for pos,team in enumerate(teams,start=1):
        print("Team Pos ",pos," Team is ",team)
        if pos==4:
            break

    # TODO: test for equality
    a=OrderedDict({1:'one',2:'two',3:'three'})
    b=OrderedDict({1:'one',2:'two',3:'three'})
    c=OrderedDict({1:'one',3:'three',2:'two'})
    d={1:'one',3:'three',2:'two'}
    print("a==b :",a==b)
    print("a==c :",a==c)
    print("a==d :",a==d)


if __name__ == "__main__":
    main()
