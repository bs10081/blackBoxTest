import requests

# 初始化會話
session = requests.Session()

# API 網址
api_url = "https://d.systemdynamics.tw/blackbox.php"

# 測試函數：重置訂單資料
def test_reset():
    response = session.post(api_url, data={'act': 'reset'})
    if response.status_code == 200:
        print("重置訂單資料成功。")
    else:
        print("重置訂單資料失敗，狀態碼：", response.status_code)

# 測試函數：增加商品
def test_add_item(name, price):
    response = session.post(api_url, data={'act': 'addItem', 'name': name, 'price': price})
    if response.status_code == 200:
        print(f"增加商品 '{name}' 成功，價格：{price}。")
    else:
        print(f"增加商品 '{name}' 失敗，狀態碼：", response.status_code)

# 測試函數：獲取訂單總額
def test_get_total(expected_total):
    response = session.post(api_url, data={'act': 'getTotal'})
    if response.status_code == 200 and response.text == str(expected_total):
        print(f"訂單總額正確，總額：{response.text}。")
    else:
        print(f"訂單總額不正確，預期：{expected_total}，實際：{response.text}。")

# 測試函數：獲取折扣金額
def test_get_discount(expected_discount):
    response = session.post(api_url, data={'act': 'getDiscount'})
    if response.status_code == 200 and response.text == str(expected_discount):
        print(f"折扣金額正確，折扣：{response.text}。")
    else:
        print(f"折扣金額不正確，預期：{expected_discount}，實際：{response.text}。")

# 主測試流程
def main_test_flow():
    # 重置訂單資料
    test_reset()
    
    # 增加商品測試
    test_add_item('測試商品A', 500)
    test_add_item('測試商品B', 1500)
    
    # 驗證訂單總額
    test_get_total(2000)
    
    # 驗證折扣金額
    test_get_discount(200)
    
    # 增加更多商品來測試折扣規則
    test_add_item('測試商品C', 3000)
    test_get_total(5000)  # 更新後的總額
    test_get_discount(600)  # 應該是每滿1000減100，5000以上再多減100

    # 測試折扣上限
    test_add_item('測試商品D', 20000)
    test_get_total(25000)  # 更新後的總額
    test_get_discount(10000)  # 總折扣最多減10000

# 執行測試
if __name__ == "__main__":
    main_test_flow()

