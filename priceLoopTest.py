import requests

# 初始化會話
session = requests.Session()

# API 網址
api_url = "https://d.systemdynamics.tw/blackbox.php"

# 測試函數：增加商品並檢查總額和折扣


def test_order(price):
    session.post(api_url, data={'act': 'reset'})
    session.post(api_url, data={'act': 'addItem',
                 'name': 'testProduct', 'price': price})
    total_response = session.post(api_url, data={'act': 'getTotal'})
    discount_response = session.post(api_url, data={'act': 'getDiscount'})
    return total_response.text, discount_response.text

# 判斷結果是否正確


def is_result_correct(price, total, discount):
    expected_discount = min(10000, price // 1000 * 100)
    if price >= 5000:
        expected_discount += 100
    return total == str(price) and discount == str(expected_discount)

# 二分搜尋法找到錯誤出現的起始點


def binary_search_for_error(start, end):
    print(f"開始二分搜尋，範圍 {start} 到 {end}")
    while start <= end:
        mid = (start + end) // 2
        total, discount = test_order(mid)
        print(f"測試價格：{mid}, 總額：{total}, 折扣：{discount}")
        if is_result_correct(mid, total, discount):
            print("結果正確，向右搜尋")
            start = mid + 1  # 結果正確，向右搜尋
        else:
            print("結果錯誤，向左搜尋")
            end = mid - 1  # 結果錯誤，向左搜尋
    return start

# 主測試流程


def main_test_flow():
    # 使用二分搜尋法找到錯誤開始出現的位置
    error_start = binary_search_for_error(10000, 1000000)

    # 從找到的點開始進行細粒度搜索
    for offset in [1000, 100, 10, 1]:
        print(f"開始細粒度搜索，當前偏移量：{offset}")
        while True:
            price = error_start - offset
            total, discount = test_order(price)
            print(f"測試價格：{price}, 總額：{total}, 折扣：{discount}")
            if is_result_correct(price, total, discount):
                print("結果正確，向前恢復")
                error_start = price + offset  # 向前恢復到錯誤出現的位置
                break
            else:
                print("結果錯誤，繼續搜尋")
                error_start -= offset  # 繼續向後搜尋

    # 檢查連續三個點是否都出現錯誤
    print(f"檢查連續三個點，從價格 {error_start}")
    consecutive_errors = all(not is_result_correct(
        price, *test_order(price)) for price in range(error_start, error_start + 3))
    if consecutive_errors:
        print(
            f"連續三次錯誤出現在價格：{error_start}, {error_start + 1}, {error_start + 2}")
    else:
        print("未找到連續三次錯誤的價格點。")


# 執行測試
if __name__ == "__main__":
    main_test_flow()
