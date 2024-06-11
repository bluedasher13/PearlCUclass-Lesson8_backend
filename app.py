from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 啟用所有路由的 CORS 支持


# 一個 API 路由，返回一些 JSON 數據
@app.route("/get_list", methods=["GET"])
def get_data():
    data = {"items": ["平板", "筆記型電腦", "手機", "桌上型電腦", "顯示卡", "CPU"]}
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
