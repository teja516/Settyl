
import json
from fastapi import FastAPI
from pydantic import BaseModel
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import InputLayer, Dense, Dropout
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer

label_encoder = LabelEncoder()
vectorizer = CountVectorizer()


with open('nn_model_architecture.json', 'r') as json_file:
    model_config = json.load(json_file)


nn_model = Sequential()


for layer_config in model_config['config']['layers']:
    if layer_config['class_name'] == 'InputLayer':
        layer = InputLayer(**layer_config['config'])
    else:
        layer_class = globals()[layer_config['class_name']]
        layer = layer_class(**layer_config['config'])
    nn_model.add(layer)

nn_model.load_weights('nn_model_weights.weights.h5')


app = FastAPI()

class TextData(BaseModel):
    text: str

@app.post("/predict")
async def predict(data: TextData):
    try:


        return {"predicted_label": predicted_label}
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": "Internal Server Error"})


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
