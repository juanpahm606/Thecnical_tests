import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
#Creacion de tablas
datos_1=pd.read_csv("appearances.csv",sep=",")
datos_2=pd.read_csv("games.csv")
datos_3=pd.ExcelFile("UEFA5.xlsx")
datos_3_1=pd.read_excel(datos_3,'teams')
datos_3_2=pd.read_excel(datos_3,'players')
datos_3_3=pd.read_excel(datos_3,'leagues')
lista_1='"gameID","playerID","goals","ownGoals","shots","xGoals","xGoalsChain","xGoalsBuildup","assists","keyPasses","xAssists","position","positionOrder","yellowCard","redCard","time","substituteIn","substituteOut","leagueID"'
datos_1=datos_1[lista_1].str.split(',', expand=True)
datos_1.columns=["gameID","playerID","goals","ownGoals","shots","xGoals","xGoalsChain","xGoalsBuildup","assists","keyPasses","xAssists","position","positionOrder","yellowCard","redCard","time","substituteIn","substituteOut","leagueID"]
#Primera a quinta pregunta
#Premier League
leagues_id=pd.merge(datos_2,datos_3_3,on='leagueID')
premier_league = leagues_id[leagues_id['leagueNAME'] == 'Premier League']
premier_league_2016=premier_league.loc[premier_league['season']==2016]

premier_league_2016['homePoints'] = premier_league_2016.apply(
    lambda goals: 3 if goals['homeGoals'] > goals['awayGoals'] else (1 if goals['homeGoals'] == goals['awayGoals'] else 0),
    axis=1
)
premier_league_2016['awayPoints'] = premier_league_2016.apply(
    lambda goals: 3 if goals['awayGoals'] > goals['homeGoals'] else (1 if goals['homeGoals'] == goals['awayGoals'] else 0),
    axis=1
)
PL_homePoints=premier_league_2016.groupby('homeTeamID')['homePoints'].sum().reset_index()
PL_awayPoints=premier_league_2016.groupby('awayTeamID')['awayPoints'].sum().reset_index()
PL_homeGoals=premier_league_2016.groupby('homeTeamID')['homeGoals'].sum().reset_index()
PL_awayGoals=premier_league_2016.groupby('awayTeamID')['awayGoals'].sum().reset_index()
PL_homeGoalsAgainst=premier_league_2016.groupby('homeTeamID')['awayGoals'].sum().reset_index()
PL_awayGoalsAgainst=premier_league_2016.groupby('awayTeamID')['homeGoals'].sum().reset_index()
PL_2016_table=pd.DataFrame()
PL_2016_table['teamID']=PL_homePoints['homeTeamID']
PL_2016_table=pd.merge(PL_2016_table,datos_3_1,on='teamID')
PL_2016_table['Points']=PL_homePoints['homePoints']+PL_awayPoints['awayPoints']
PL_2016_table['Goals']=PL_homeGoals['homeGoals']+PL_awayGoals['awayGoals']
PL_2016_table['Goals Against']=PL_homeGoalsAgainst['awayGoals']+PL_awayGoalsAgainst['homeGoals']
PL_2016_table['Goal Difference']=PL_2016_table['Goals']-PL_2016_table['Goals Against']
PL_2016_table=PL_2016_table.sort_values(by='Points',ascending=False).reset_index(drop=True)
print(PL_2016_table.iloc[0])
#Serie A
serie_a= leagues_id[leagues_id['leagueNAME'] == 'Serie A']
serie_a_2017=serie_a.loc[serie_a['season']==2017]
serie_a_2017['homePoints'] = serie_a_2017.apply(
    lambda goals: 3 if goals['homeGoals'] > goals['awayGoals'] else (1 if goals['homeGoals'] == goals['awayGoals'] else 0),
    axis=1
)
serie_a_2017['awayPoints'] = serie_a_2017.apply(
    lambda goals: 3 if goals['awayGoals'] > goals['homeGoals'] else (1 if goals['homeGoals'] == goals['awayGoals'] else 0),
    axis=1
)
SA_homePoints=serie_a_2017.groupby('homeTeamID')['homePoints'].sum().reset_index()
SA_awayPoints=serie_a_2017.groupby('awayTeamID')['awayPoints'].sum().reset_index()
SA_homeGoals=serie_a_2017.groupby('homeTeamID')['homeGoals'].sum().reset_index()
SA_awayGoals=serie_a_2017.groupby('awayTeamID')['awayGoals'].sum().reset_index()
SA_homeGoalsAgainst=serie_a_2017.groupby('homeTeamID')['awayGoals'].sum().reset_index()
SA_awayGoalsAgainst=serie_a_2017.groupby('awayTeamID')['homeGoals'].sum().reset_index()
SA_2017_table=pd.DataFrame()
SA_2017_table['teamID']=SA_homePoints['homeTeamID']
SA_2017_table=pd.merge(SA_2017_table,datos_3_1,on='teamID')
SA_2017_table['Points']=SA_homePoints['homePoints']+SA_awayPoints['awayPoints']
SA_2017_table['Goals']=SA_homeGoals['homeGoals']+SA_awayGoals['awayGoals']
SA_2017_table['Goals Against']=SA_homeGoalsAgainst['awayGoals']+SA_awayGoalsAgainst['homeGoals']
SA_2017_table['Goal Difference']=SA_2017_table['Goals']-SA_2017_table['Goals Against']
SA_2017_table=SA_2017_table.sort_values(by='Points',ascending=False).reset_index(drop=True)
print(SA_2017_table.iloc[1])
#Bundesliga

bundesliga = leagues_id[leagues_id['leagueNAME'] == 'Bundesliga']
bundesliga_2018=bundesliga.loc[bundesliga['season']==2018]

bundesliga_2018['homePoints'] = bundesliga_2018.apply(
    lambda goals: 3 if goals['homeGoals'] > goals['awayGoals'] else (1 if goals['homeGoals'] == goals['awayGoals'] else 0),
    axis=1
)
bundesliga_2018['awayPoints'] = bundesliga_2018.apply(
    lambda goals: 3 if goals['awayGoals'] > goals['homeGoals'] else (1 if goals['homeGoals'] == goals['awayGoals'] else 0),
    axis=1
)
B_homePoints=bundesliga_2018.groupby('homeTeamID')['homePoints'].sum().reset_index()
B_awayPoints=bundesliga_2018.groupby('awayTeamID')['awayPoints'].sum().reset_index()
B_homeGoals=bundesliga_2018.groupby('homeTeamID')['homeGoals'].sum().reset_index()
B_awayGoals=bundesliga_2018.groupby('awayTeamID')['awayGoals'].sum().reset_index()
B_homeGoalsAgainst=bundesliga_2018.groupby('homeTeamID')['awayGoals'].sum().reset_index()
B_awayGoalsAgainst=bundesliga_2018.groupby('awayTeamID')['homeGoals'].sum().reset_index()
B_2018_table=pd.DataFrame()
B_2018_table['teamID']=B_homePoints['homeTeamID']
B_2018_table=pd.merge(B_2018_table,datos_3_1,on='teamID')
B_2018_table['Points']=B_homePoints['homePoints']+B_awayPoints['awayPoints']
B_2018_table['Goals']=B_homeGoals['homeGoals']+B_awayGoals['awayGoals']
B_2018_table['Goals Against']=B_homeGoalsAgainst['awayGoals']+B_awayGoalsAgainst['homeGoals']
B_2018_table['Goal Difference']=B_2018_table['Goals']-B_2018_table['Goals Against']
B_2018_table=B_2018_table.sort_values(by='Points',ascending=False).reset_index(drop=True)
print(B_2018_table.iloc[2])
#La Liga
la_liga = leagues_id[leagues_id['leagueNAME'] == 'La Liga']
la_liga_2019=la_liga.loc[la_liga['season']==2019]
la_liga_2019['homePoints'] = la_liga_2019.apply(
    lambda goals: 3 if goals['homeGoals'] > goals['awayGoals'] else (1 if goals['homeGoals'] == goals['awayGoals'] else 0),
    axis=1
)
la_liga_2019['awayPoints'] = la_liga_2019.apply(
    lambda goals: 3 if goals['awayGoals'] > goals['homeGoals'] else (1 if goals['homeGoals'] == goals['awayGoals'] else 0),
    axis=1
)
LL_homePoints=la_liga_2019.groupby('homeTeamID')['homePoints'].sum().reset_index()
LL_awayPoints=la_liga_2019.groupby('awayTeamID')['awayPoints'].sum().reset_index()
LL_homeGoals=la_liga_2019.groupby('homeTeamID')['homeGoals'].sum().reset_index()
LL_awayGoals=la_liga_2019.groupby('awayTeamID')['awayGoals'].sum().reset_index()
LL_homeGoalsAgainst=la_liga_2019.groupby('homeTeamID')['awayGoals'].sum().reset_index()
LL_awayGoalsAgainst=la_liga_2019.groupby('awayTeamID')['homeGoals'].sum().reset_index()
LL_2019_table=pd.DataFrame()
LL_2019_table['teamID']=LL_homePoints['homeTeamID']
LL_2019_table=pd.merge(LL_2019_table,datos_3_1,on='teamID')
LL_2019_table['Points']=LL_homePoints['homePoints']+LL_awayPoints['awayPoints']
LL_2019_table['Goals']=LL_homeGoals['homeGoals']+LL_awayGoals['awayGoals']
LL_2019_table['Goals Against']=LL_homeGoalsAgainst['awayGoals']+LL_awayGoalsAgainst['homeGoals']
LL_2019_table['Goal Difference']=LL_2019_table['Goals']-LL_2019_table['Goals Against']
LL_2019_table=LL_2019_table.sort_values(by='Points',ascending=False).reset_index(drop=True)
print(LL_2019_table.iloc[3])
#Ligue 1
ligue_1 = leagues_id[leagues_id['leagueNAME'] == 'Ligue 1']
ligue_1_2020=ligue_1.loc[ligue_1['season']==2020]
ligue_1_2020['homePoints'] = ligue_1_2020.apply(
    lambda goals: 3 if goals['homeGoals'] > goals['awayGoals'] else (1 if goals['homeGoals'] == goals['awayGoals'] else 0),
    axis=1
)
ligue_1_2020['awayPoints'] = ligue_1_2020.apply(
    lambda goals: 3 if goals['awayGoals'] > goals['homeGoals'] else (1 if goals['homeGoals'] == goals['awayGoals'] else 0),
    axis=1
)
L1_homePoints=ligue_1_2020.groupby('homeTeamID')['homePoints'].sum().reset_index()
L1_awayPoints=ligue_1_2020.groupby('awayTeamID')['awayPoints'].sum().reset_index()
L1_homeGoals=ligue_1_2020.groupby('homeTeamID')['homeGoals'].sum().reset_index()
L1_awayGoals=ligue_1_2020.groupby('awayTeamID')['awayGoals'].sum().reset_index()
L1_homeGoalsAgainst=ligue_1_2020.groupby('homeTeamID')['awayGoals'].sum().reset_index()
L1_awayGoalsAgainst=ligue_1_2020.groupby('awayTeamID')['homeGoals'].sum().reset_index()
L1_2020_table=pd.DataFrame()
L1_2020_table['teamID']=L1_homePoints['homeTeamID']
L1_2020_table=pd.merge(L1_2020_table,datos_3_1,on='teamID')
L1_2020_table['Points']=L1_homePoints['homePoints']+L1_awayPoints['awayPoints']
L1_2020_table['Goals']=L1_homeGoals['homeGoals']+L1_awayGoals['awayGoals']
L1_2020_table['Goals Against']=L1_homeGoalsAgainst['awayGoals']+L1_awayGoalsAgainst['homeGoals']
L1_2020_table['Goal Difference']=L1_2020_table['Goals']-L1_2020_table['Goals Against']
L1_2020_table=L1_2020_table.sort_values(by='Points',ascending=False).reset_index(drop=True)
print(L1_2020_table.iloc[4])

#Sexta a décima pregunta
#League1
def entero(value):
    if isinstance(value,str):
        return int(value.strip('"'))
    else:
        return value
datos_1['playerID']=datos_1['playerID'].apply(entero)
datos_1['leagueID']=datos_1['leagueID'].apply(entero)
datos_1['gameID']=datos_1['gameID'].apply(entero)
season=pd.DataFrame()
season['gameID']=datos_2['gameID']
season['season']=datos_2['season']
leagues_id_2=pd.merge(datos_1,datos_3_2,on='playerID')
leagues_id_2=pd.merge(leagues_id_2,datos_3_3,on='leagueID')
leagues_id_2=pd.merge(leagues_id_2,season,on='gameID')
#League 1
ligue_1_players_2016=leagues_id_2.loc[(leagues_id_2['leagueNAME']=='Ligue 1') & (leagues_id_2['season']==2016 )]
ligue_1_players_2016['goals']=ligue_1_players_2016['goals'].apply(entero)
ligue_1_players_2016['time']=ligue_1_players_2016['time'].apply(entero)
goals_ligue1=ligue_1_players_2016.groupby('playerNAME')['goals'].sum().reset_index()
minutes_ligue1=ligue_1_players_2016.groupby('playerNAME')['time'].sum().reset_index()
TopGoalScorers_Ligue1=goals_ligue1.sort_values(by='goals',ascending=False).reset_index(drop=True).nlargest(10,'goals')
TopGoalScorers_Ligue1=pd.merge(TopGoalScorers_Ligue1,minutes_ligue1,on='playerNAME')
TopGoalScorers_Ligue1['Goals Per Game']=90*(TopGoalScorers_Ligue1['goals']/TopGoalScorers_Ligue1['time'])
TopGoalScorers_Ligue1.sort_values(by='Goals Per Game',ascending=False).reset_index(drop=True)
#LaLiga
la_liga_players_2017=leagues_id_2.loc[(leagues_id_2['leagueNAME']=='La Liga') & (leagues_id_2['season']==2017 )]
la_liga_players_2017['goals']=la_liga_players_2017['goals'].apply(entero)
la_liga_players_2017['time']=la_liga_players_2017['time'].apply(entero)
goals_laliga=la_liga_players_2017.groupby('playerNAME')['goals'].sum().reset_index()
minutes_laliga=la_liga_players_2017.groupby('playerNAME')['time'].sum().reset_index()
TopGoalScorers_LaLiga=goals_laliga.sort_values(by='goals',ascending=False).reset_index(drop=True).nlargest(10,'goals')
TopGoalScorers_LaLiga=pd.merge(TopGoalScorers_LaLiga,minutes_laliga,on='playerNAME')
TopGoalScorers_LaLiga['Goals Per Game']=90*(TopGoalScorers_LaLiga['goals']/TopGoalScorers_LaLiga['time'])
TopGoalScorers_LaLiga.sort_values(by='Goals Per Game',ascending=False).reset_index(drop=True)
#print
#Bundesliga
bundesliga_players_2018=leagues_id_2.loc[(leagues_id_2['leagueNAME']=='Bundesliga') & (leagues_id_2['season']==2018 )]
bundesliga_players_2018['goals']=bundesliga_players_2018['goals'].apply(entero)
bundesliga_players_2018['time']=bundesliga_players_2018['time'].apply(entero)
goals_bundesliga=bundesliga_players_2018.groupby('playerNAME')['goals'].sum().reset_index()
minutes_bundesliga=bundesliga_players_2018.groupby('playerNAME')['time'].sum().reset_index()
TopGoalScorers_Bundesliga=goals_bundesliga.sort_values(by='goals',ascending=False).reset_index(drop=True).nlargest(10,'goals')
TopGoalScorers_Bundesliga=pd.merge(TopGoalScorers_Bundesliga,minutes_bundesliga,on='playerNAME')
TopGoalScorers_Bundesliga['Goals Per Game']=90*(TopGoalScorers_Bundesliga['goals']/TopGoalScorers_Bundesliga['time'])
TopGoalScorers_Bundesliga.sort_values(by='Goals Per Game',ascending=False).reset_index(drop=True)
#Serie A
serie_A_players_2019=leagues_id_2.loc[(leagues_id_2['leagueNAME']=='Serie A') & (leagues_id_2['season']==2019 )]
serie_A_players_2019['goals']=serie_A_players_2019['goals'].apply(entero)
serie_A_players_2019['time']=serie_A_players_2019['time'].apply(entero)
goals_serie_A=serie_A_players_2019.groupby('playerNAME')['goals'].sum().reset_index()
minutes_serie_A=serie_A_players_2019.groupby('playerNAME')['time'].sum().reset_index()
TopGoalScorers_Serie_A=goals_serie_A.sort_values(by='goals',ascending=False).reset_index(drop=True).nlargest(10,'goals')
TopGoalScorers_Serie_A=pd.merge(TopGoalScorers_Serie_A,minutes_serie_A,on='playerNAME')
TopGoalScorers_Serie_A['Goals Per Game']=90*(TopGoalScorers_Serie_A['goals']/TopGoalScorers_Serie_A['time'])
TopGoalScorers_Serie_A.sort_values(by='Goals Per Game',ascending=False).reset_index(drop=True)
#Premier League
premier_league_players_2020=leagues_id_2.loc[(leagues_id_2['leagueNAME']=='Premier League') & (leagues_id_2['season']==2020 )]
premier_league_players_2020['goals']=premier_league_players_2020['goals'].apply(entero)
premier_league_players_2020['time']=premier_league_players_2020['time'].apply(entero)
goals_premierleague=premier_league_players_2020.groupby('playerNAME')['goals'].sum().reset_index()
minutes_premierleague=premier_league_players_2020.groupby('playerNAME')['time'].sum().reset_index()
TopGoalScorers_PremierLeague=goals_premierleague.sort_values(by='goals',ascending=False).reset_index(drop=True).nlargest(10,'goals')
TopGoalScorers_PremierLeague=pd.merge(TopGoalScorers_PremierLeague,minutes_premierleague,on='playerNAME')
TopGoalScorers_PremierLeague['Goals Per Game']=90*(TopGoalScorers_PremierLeague['goals']/TopGoalScorers_PremierLeague['time'])
TopGoalScorers_PremierLeague.sort_values(by='Goals Per Game',ascending=False).reset_index(drop=True)



pass