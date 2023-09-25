import requests
import pandas as pd

url = "http://www.naturalstattrick.com/playerteams.php?fromseason=20222023&thruseason=20222023&stype=2&sit=5v5&score=all&stdoi=oi&rate=n&team=ALL&pos=S&loc=B&toi=0&gpfilt=none&fd=&td=&tgp=410&lines=single&draftteam=ALL"

df = pd.read_html(url, header=0, index_col=0, na_values=["-"])[0]


print(df)