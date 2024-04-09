import pandas as pd
import requests

url = 'https://gist.githubusercontent.com/farhaan-settyl/ecf9c1e7ab7374f18e4400b7a3d2a161/raw/f94652f217eeca83e36dab9d08727caf79ebdecf/dataset.json'
response = requests.get(url)
df = pd.read_json(response.text)
df.to_csv('dataset.csv', index=False)
df.to_csv('C:/Users/Brahmateja Yamanuri/Intershala/dataset.csv', index=False)


