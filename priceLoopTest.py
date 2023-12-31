import requests

# 初始化會話
session = requests.Session()

# API 網址
api_url = "https://d.systemdynamics.tw/blackbox.php"

# 測試函數：增加商品並檢查總額和折扣


def test_order(price):
    # 重置訂單資料
    session.post(api_url, data={'act': 'reset'})

    # 增加商品
    session.post(api_url, data={'act': 'addItem',
                 'name': 'testProduct', 'price': price})

    # 獲取訂單總額
    total_response = session.post(api_url, data={'act': 'getTotal'})
    total = total_response.text if total_response.status_code == 200 else "Error"

    # 獲取折扣金額
    discount_response = session.post(api_url, data={'act': 'getDiscount'})
    discount = discount_response.text if discount_response.status_code == 200 else "Error"

    return total, discount

# 主測試流程：測試價格從 10000 到 1000000


def main_test_flow():
    error_count = 0
    for price in range(10000, 1000001):
        total, discount = test_order(price)

        # 計算預期的總額和折扣
        expected_discount = min(10000, price // 1000 * 100)
        if price >= 5000:
            expected_discount += 100

        # 檢查總額和折扣是否正確
        if total != str(price) or discount != str(expected_discount):
            error_count += 1
            print(
                f"出現問題的價格：{price}, 總額：{total}, 折扣：{discount}, 預期折扣：{expected_discount}")

            # 如果連續三次出現錯誤，停止測試
            if error_count >= 3:
                print("連續三次出現問題，停止測試。")
                break
        else:
            print(f"測試通過：{price}, 總額：{total}, 折扣：{discount}")
            error_count = 0  # 重置錯誤計數器


# 執行測試
if __name__ == "__main__":
    main_test_flow()
