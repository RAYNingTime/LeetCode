import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    data = players.size
    columns = len(players.columns)
    return([int(data/columns), columns])
