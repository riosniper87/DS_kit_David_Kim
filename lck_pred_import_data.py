import logging
import warnings
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from mwrogue.esports_client import EsportsClient
from mwrogue.auth_credentials import AuthCredentials
import datetime as dt
import pandas as pd 

warnings.simplefilter("ignore")

@dataclass
class Config:
    """
    Arguments pertaining to import data by mwlogue.
    """
    
    Date: str = field(
        default=dt.datetime.today().date(),
        metadata={
            "help": "The end date of data."
        }
    )
        
    Year: Optional[int] = field(
        default=4,
        metadata={
            "help": "number of years to data-gather."
        }
    )
        
    Region: str = field(
        default=None,
        metadata={
            "help": "Region filter for gathering data."
        }
    )
        
    Fields: str = field(
        default="PB.Team1Ban1,PB.Team1Ban2,PB.Team1Ban3,PB.Team1Ban4,PB.Team1Ban5,PB.Team1Pick1,PB.Team1Pick2,PB.Team1Pick3,PB.Team1Pick4,PB.Team1Pick5,PB.Team2Ban1,PB.Team2Ban2,PB.Team2Ban3,PB.Team2Ban4,PB.Team2Ban5,PB.Team2Pick1,PB.Team2Pick2,PB.Team2Pick3,PB.Team2Pick4,PB.Team2Pick5,PB.Team1,PB.Team2,PB.Winner ,PB.Team1Score ,PB.Team2Score ,PB.Team1PicksByRoleOrder,PB.Team2PicksByRoleOrder,PB.OverviewPage,PB.Phase,PB.UniqueLine,PB.IsComplete ,PB.Tab,PB.N_Page ,PB.N_TabInPage ,PB.N_MatchInPage ,PB.N_GameInPage ,PB.N_GameInMatch ,PB.N_MatchInTab ,PB.N_GameInTab ,PB.GameId,PB.MatchId,PB.GameID_Wiki, SG.Team1, SG.Team2, SG.DateTime_UTC,SG.Patch, T.League, T.Region, T.TournamentLevel, T.IsQualifier, T.IsPlayoffs, T.IsOfficial",
        metadata={
            "help": "columns of data. Base query consists of PB.GameId = MG.GameId, MG.GameId = SG.GameId, PB.OverviewPage = T.OverviewPage."
        }
    )
        
logger = logging.getLogger(__name__)

def get_data(form):
    site = EsportsClient("lol")
    res = site.cargo_client.query(
    tables="PicksAndBansS7=PB, MatchScheduleGame = MG, ScoreboardGames = SG, Tournaments = T",
    fields=Config.Fields,
    join_on="PB.GameId = MG.GameId, MG.GameId = SG.GameId, PB.OverviewPage = T.OverviewPage",
    # where="PB.MatchId = '2017 LoL KeSPA Cup_Quarterfinals_1'"
    where="SG.DateTime_UTC <= '" + str(form.Date) + " 00:00:00' AND SG.DateTime_UTC >= '" + str(form.Date-dt.timedelta(365*form.Year)) + " 00:00:00' AND PB.Team1Pick5 != '' AND T.TournamentLevel = 'Primary'"
    )
    data = pd.DataFrame(res)
    return data
print("aaaaa")
# if __name__ == "__main__":
#     main()
