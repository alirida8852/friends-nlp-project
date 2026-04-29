import joblib

# load model
model = joblib.load("../model/trained_model.pkl")

while True:
    text = input("Enter dialogue: ")
    prediction = model.predict([text])
    print("Predicted Character:", prediction[0])