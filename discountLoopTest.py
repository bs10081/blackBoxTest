import requests

# 初始化會話
session = requests.Session()

# API 網址
api_url = "https://d.systemdynamics.tw/blackbox.php"

# 計算折扣函數


def calculate_expected_discount(price):
    discount = min(10000, price // 1000 * 100)
    if price >= 5000:
        discount += 100
    return discount

# 測試折扣計算


def test_discount(price):
    session.post(api_url, data={'act': 'reset'})
    session.post(api_url, data={'act': 'addItem',
                 'name': 'testProduct', 'price': price})
    discount_response = session.post(api_url, data={'act': 'getDiscount'})
    return discount_response.text

# 進行二元搜尋找出計算折扣出現問題的點


def binary_search_discount_error(low, high):
    while low <= high:
        mid = (low + high) // 2
        actual_discount = test_discount(mid)
        expected_discount = calculate_expected_discount(mid)
        print(f"測試價格：{mid}, 實際折扣：{actual_discount}, 預期折扣：{expected_discount}")

        if int(actual_discount) == expected_discount:
            low = mid + 1
        else:
            high = mid - 1

    # 高值 high + 1 是最初出現錯誤的點
    return high + 1

# 主測試流程


def main_test_flow():
    error_point = binary_search_discount_error(10000, 1000000)
    print(f"折扣計算首次出現問題的價格是：{error_point}")


# 執行測試
if __name__ == "__main__":
    main_test_flow()
