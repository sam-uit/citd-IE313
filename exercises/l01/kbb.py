# IE313 - Buổi 01 - Hoạt Động 02
# MSSV:
# Họ Tên:
# Github:
# Bài Tập
# Viết chương trình mô phỏng trò chơi Kéo - Búa - Bao giữa người và máy.
# Quy ước:
# - Kéo > Bao
# - Búa > Kéo
# - Bao > Búa

import random

# dict chứa các lựa chọn khả thi
kbb_dict = {
    "keo": "Kéo",
    "bua": "Búa",
    "bao": "Bao"
}

# result_dict: các kết quả khả thi của trò chơi
result_dict = {
    0: "Hòa!",
    1: "Bạn thắng!",
    2: "Máy thắng!"
}

# get_kbb_choice: trả về một lựa chọn ngẫu nhiên từ kbb_dict
def get_kbb_choice():
    """Trả về một lựa chọn ngẫu nhiên từ kbb_dict"""
    return random.choice(tuple(kbb_dict.keys()))

# winner: xác định người chiến thắng dựa trên các lựa chọn
def winner(your_choice: str, computer_choice: str):
    """Xác định người chiến thắng dựa trên lựa chọn của người chơi và máy"""
    if your_choice == computer_choice:
        return 0
    elif (your_choice == "keo" and computer_choice == "bao") or \
         (your_choice == "bua" and computer_choice == "keo") or \
         (your_choice == "bao" and computer_choice == "bua"):
        return 1
    else:
        return 2

