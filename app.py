from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

DATA_FILE = "code.json"

def normalize_candidates(codes):
    candidates = set()
    for code in codes:
        candidates.add(code)
        if code.isdigit() and code.startswith("0"):
            candidates.add(code[1:])  # thêm phiên bản bỏ số 0
    return candidates

# Load dữ liệu từ code.json
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        CODE_VALUES = set(json.load(f))
else:
    CODE_VALUES = set()

CANDIDATES = normalize_candidates(CODE_VALUES)

@app.route("/", methods=["POST"])
def decode():
    masked = request.json.get("masked", "").strip()
    if not masked or "*" not in masked:
        return jsonify({"success": False, "message": "❌ Dữ liệu không hợp lệ hoặc không chứa dấu *."})

    prefix = masked.split("*")[0].lower()
    suffix = masked.split("*")[-1].lower()

    for code in CANDIDATES:
        if code.lower().startswith(prefix) and code.lower().endswith(suffix):
            return jsonify({
                "success": True,
                "masked": masked,
                "decoded": code
            })

    return jsonify({"success": False, "message": "❌ Không tìm thấy mã khớp."})
