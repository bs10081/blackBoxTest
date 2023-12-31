import requests

# 初始化會話
session = requests.Session()

# API 網址
api_url = "https://d.systemdynamics.tw/blackbox.php"

# 測試函數：重置訂單資料
def test_reset():
    try:
        response = session.post(api_url, data={'act': 'reset'})
        print("test_reset Response:", response.text)
        print("Status Code:", response.status_code)
    except Exception as e:
        print("test_reset Error:", e)

# 測試函數：增加商品
def test_add_item(name, price):
    try:
        response = session.post(api_url, data={'act': 'addItem', 'name': name, 'price': price})
        print(f"test_add_item Response for {name}:", response.text)
        print("Status Code:", response.status_code)
    except Exception as e:
        print(f"test_add_item Error for {name}:", e)

# 測試函數：獲取訂單總額
def test_get_total():
    try:
        response = session.post(api_url, data={'act': 'getTotal'})
        print("test_get_total Response:", response.text)
        print("Status Code:", response.status_code)
    except Exception as e:
        print("test_get_total Error:", e)

# 測試函數：獲取折扣金額
def test_get_discount():
    try:
        response = session.post(api_url, data={'act': 'getDiscount'})
        print("test_get_discount Response:", response.text)
        print("Status Code:", response.status_code)
    except Exception as e:
        print("test_get_discount Error:", e)

# 執行所有測試
def run_tests():
    print("執行 test_reset...")
    test_reset()
    
    print("執行 test_add_item...")
    test_add_item('測試商品A', 500)
    test_add_item('測試商品B', 1500)
    
    print("執行 test_get_total...")
    test_get_total()
    
    print("執行 test_get_discount...")
    test_get_discount()

# 主程式入口
if __name__ == "__main__":
    run_tests()

