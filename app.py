from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Bật CORS cho toàn bộ domain

# Dữ liệu ánh xạ
DATA_MAPPING = {
    "Mô Hình Sàn Tiếp Thị Liên Kết": "Storytelling",
    "Mô hình Affiliate Marketing permate là gì": "Storytelling",
    "bác sĩ nguyên giáp phốt": "989090599",
    "bán laptop cũ": "110617518",
    "bình xe điện trẻ em": "0919267266",
    "celadon city": "975769123",
    "chi phí thay bàn phím laptop": "110617518",
    "chivas 12 ruoutaychinhhang": "AnnabelMeikle",
    "chống thấm ngược cho tường": "972839232",
    "chống thấm ngược tường nhà": "0972839232",
    "chống thấm tường nhà cũ": "972839232",
    "chống thấm vách tường": "972839232",
    "cung cấp khí công nghiệp dakhien": "906666858",
    "cỏ nhân tạo khánh phát": "0877799988",
    "cửa hàng hoa sunny": "8675228625",
    "du lịch hoàng việt": "/2015/CDLQGVN",
    "ghế công thái học bchair": "0988626962",
    "ghế giám đốc bchair": "0988626962",
    "hút bể phốt tại ba đình": "46616888",
    "hút bể phốt tại hà nội": "46616888",
    "hút bể phốt tại long biên": "46616888",
    "hút hầm cầu bình dương": "701743714",
    "hút hầm cầu châu đức huthamcaubaria24h.com": "963588919",
    "hút hầm cầu phú mỹ huthamcaubaria24h.com": "963588919",
    "hút hầm cầu đà nẵng": "23123456",
    "job gg dịch": "TechCrunch",
    "kiếm tiền affiliate": "ReferralPermate",
    "kiếm tiền với affiliate": "ReferralPermate",
    "kế hoạch kiếm tiền affiliate": "ReferralPermate",
    "máy bắt muỗi": "972222958",
    "máy rửa chén bát công nghiệp": "972222958",
    "niềng răng bao nhiêu elite dental": "2873063838",
    "nắp ga composite 850x850": "0946402868",
    "nắp hố ga": "0946402868",
    "nền tảng affiliate": "AffiliatePlatform",
    "nền tảng affiliate marketing": "AffiliatePlatform",
    "proxy us": "THANKYOU",
    "quà mừng thọ": "19541968",
    "quà tặng sếp nam": "19541968",
    "sàn tiếp thị liên kết là gì": "Storytelling",
    "sơn dầu chống thấm ngoài trời": "972839232",
    "sạc pin laptop dell mới mua": "110617518",
    "sửa chữa laptop quận 3": "0981537570",
    "sửa chữa laptop quận bình thạnh": "110617518",
    "sửa chữa laptop tại nhà hà nội": "110617518",
    "sửa pin laptop dell bao nhiêu tiền": "110617518",
    "tem nhãn thực phẩm insonnguyen.vn": "HswA#1Rt%@",
    "thay màn hình laptop": "110617518",
    "thay ắc quy ô tô mazda 3": "0919267266",
    "thiết kế website": "0315552572",
    "thép lưới hàn": "301155522",
    "thông cống nghẹt bình dương": "701743714",
    "thông cống nghẹt đà nẵng": "23123456",
    "thông tắc cống tại hà nội": "46616888",
    "topacquy": "0919267266",
    "trần xuyên sáng": "315476699",
    "trần xuyên sáng barrisol": "315476699",
    "trần xuyên sáng tphcm": "315476699",
    "trồng răng implant giá bao nhiêu": "2873063838",
    "tuyển dụng vị trí gg dịch": "TechCrunch",
    "xưởng đúc đồng": "19541968",
    "đèn bắt muỗi": "972222958",
    "đèn uv": "972222958",
    "đông trùng hạ thảo": "367306846",
    "đông trùng hạ thảo khô": "367306846",
    "đồ cũ hà nội ngọc hưng": "hosyngoc91",
    "ắc quy delkor": "0919267266",
    "ắc quy gs": "0919267266",
    "ắc quy gs 60ah": "0919267266",
    "ắc quy varta": "0919267266",
    "ắc quy xe mercedes c250": "0919267266",
    "ắc quy xe morning": "0919267266",
    "ắc quy xe điện": "0919267266",
    "ắc quy xe đạp điện": "0919267266",
    "ắc quy đồng nai": "0919267266"
}


@app.route("/", methods=["POST"])
def get_all_data():
    return jsonify(DATA_MAPPING), 200, {'Content-Type': 'application/json; charset=utf-8'}

if __name__ == "__main__":
    app.run(debug=True)
