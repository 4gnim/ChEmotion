from flask import Flask, request, jsonify
from ocr import extract_text_from_image
from preprocessing import clean_text
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

app = Flask(__name__)

# Load model dan tokenizer
model = load_model("model/model_lstm_stress.h5")
with open("model/tokenizer_stress.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAX_LEN = 100  # sama seperti waktu training


@app.route("/predict", methods=["POST"])
def predict_stress():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"].read()
    extracted_text = extract_text_from_image(image_file)
    cleaned = clean_text(extracted_text)

    if not cleaned:
        return jsonify({"error": "No readable text in image"}), 400

    seq = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(seq, maxlen=MAX_LEN, padding="post")

    prediction = model.predict(padded)[0][0]
    label = "stres" if prediction > 0.5 else "tidak stres"

    return jsonify(
        {
            "text_ocr": extracted_text.strip(),
            "text_cleaned": cleaned,
            "label": label,
            "confidence": float(prediction),
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
