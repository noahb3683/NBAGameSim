from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
from basketball_reference_web_scraper.errors import InvalidDate
from datetime import date

y, m, d = str(date.today()).split('-')
y = int(y)
m = int(m)
d = int(d)
msg = "file created"


def player_box():
    print("retrieving player box scores")
    try:  # hard code hell yeh
        for month in range(10, 13):
            # print("searching in month {} of 2019".format(month))
            for day in range(1, 32):
                # print("searching on day {}".format(day))
                client.player_box_scores(
                    day=day, month=month, year=2019,
                    output_type=OutputType.CSV,
                    output_file_path="C:\\Users\\NWHAL\\Documents\\nba_project\\player_scores_2019_{}_{}.csv".format(month,day)
                )
                print(msg)
    except InvalidDate:
        pass

    try:
        for month in range(1, m + 1):
            # print("searching in month {} of 2020".format(month))
            for day in range(1, 32):
                # print("searching on day {}".format(day))
                client.player_box_scores(
                    day=d, month=m, year=2020,
                    output_type=OutputType.CSV,
                    output_file_path="C:\\Users\\NWHAL\\Documents\\nba_project\\player_scores_2020_{}_{}.csv".format(month, day)
                )
                print(msg)
    except InvalidDate:
        pass


def team_box():
    print("retrieving team box scores")
    try:  # hard coded 2019 team box scores
        for month in range(10, 13):
            # print("searching in month {}".format(month))
            for day in range(1, 32):
                # print("searching on day {}".format(day))
                client.team_box_scores(
                    day=1, month=1, year=2020,
                    output_type=OutputType.CSV,
                    output_file_path="C:\\Users\\NWHAL\\Documents\\nba_project\\team_scores_2019_{}_{}.csv".format(month, day)
                )
                print(msg)
    except InvalidDate:
        pass

    try:
        for month in range(1, m + 1):
            # print("searching in month {}".format(month))
            for day in range(1, 32):
                # print("searching on day {}".format(day))
                client.team_box_scores(
                    day=1, month=1, year=2020,
                    output_type=OutputType.CSV,
                    output_file_path="C:\\Users\\NWHAL\\Documents\\nba_project\\team_scores_2020_{}_{}.csv".format(month, day)
                )
                print(msg)
    except InvalidDate:
        pass


'''client.season_schedule(
    season_end_year=2018, 
    output_type=OutputType.CSV, 
    output_file_path="./2017_2018_season.csv"
)'''


def player_stats():
    print("collecting player season totals")
    client.players_season_totals(
        season_end_year=2020,
        output_type=OutputType.CSV,
        output_file_path="C:\\Users\\NWHAL\\Documents\\nba_project\\2020_player_season_totals.csv"
    )

    print("collecting advanced player stats")
    client.players_advanced_season_totals(
        season_end_year=2020,
        output_type=OutputType.CSV,
        output_file_path="C:\\Users\\NWHAL\\Documents\\nba_project\\2020_advanced_player_season_totals.csv"
    )


'''client.play_by_play(
    home_team=Team.BOSTON_CELTICS, 
    year=2018, month=10, day=16, 
    output_type=OutputType.CSV, 
    output_file_path="./2018_10_06_BOS_PBP.csv"
)

client.regular_season_player_box_scores(
    player_identifier="westbru01", 
    season_end_year=2018, 
    output_type=OutputType.CSV, 
    output_file_path="./2017_2018_russell_westbrook_regular_season_box_scores.csv"
)

client.search(
    term="Ko",
    output_type=OutputType.CSV, 
    output_file_path="./1_1_2017_box_scores.csv"
)
'''

if __name__ == "__main__":
    player_box()
    team_box()
    player_stats()
    print("Complete!")
