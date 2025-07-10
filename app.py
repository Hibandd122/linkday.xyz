from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
import re

app = Flask(__name__)
CORS(app)

DATA_FILE = "code.json"

def normalize_candidates(codes):
    candidates = set()
    for code in codes:
        candidates.add(code)
        if code.isdigit() and code.startswith("0"):
            candidates.add(code[1:])
    return candidates

# Load dữ liệu
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

    # 👉 Tách phần đặc biệt sau suffix (vd: "@", "#", ...)
    suffix_clean = ''.join(filter(str.isalnum, suffix))

    for code in CANDIDATES:
        code_clean = ''.join(filter(str.isalnum, code))
        if code_clean.lower().startswith(prefix) and code_clean.lower().endswith(suffix_clean):
            return jsonify({
                "success": True,
                "masked": masked,
                "decoded": code
            })

    return jsonify({"success": False, "message": "❌ Không tìm thấy mã khớp."})

