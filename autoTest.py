from prettytable import PrettyTable
import requests
import random
import string

# 初始化會話和表格
session = requests.Session()
api_url = "https://d.systemdynamics.tw/blackbox.php"
table = PrettyTable()
table.field_names = ["測試案例", "操作", "預期結果", "實際結果", "測試結果"]

# 測試函數：重置訂單資料


def test_reset():
    response = session.post(api_url, data={'act': 'reset'})
    if response.status_code == 200:
        table.add_row(["重置訂單資料", "act=reset", "狀態碼 200",
                      f"狀態碼 {response.status_code}", "通過"])
    else:
        table.add_row(["重置訂單資料", "act=reset", "狀態碼 200",
                      f"狀態碼 {response.status_code}", "失敗"])

# 測試函數：增加商品


def test_add_item(name, price):
    response = session.post(
        api_url, data={'act': 'addItem', 'name': name, 'price': price})
    if response.status_code == 200:
        table.add_row([f"增加商品 '{name}'", f"act=addItem, name={name}, price={price}",
                      "狀態碼 200", f"狀態碼 {response.status_code}", "通過"])
    else:
        table.add_row([f"增加商品 '{name}'", f"act=addItem, name={name}, price={price}",
                      "狀態碼 200", f"狀態碼 {response.status_code}", "失敗"])

# 測試函數：獲取訂單總額


def test_get_total(expected_total):
    response = session.post(api_url, data={'act': 'getTotal'})
    if response.status_code == 200 and response.text == str(expected_total):
        table.add_row(["獲取訂單總額", "act=getTotal",
                      f"總額 {expected_total}", f"總額 {response.text}", "通過"])
    else:
        table.add_row(["獲取訂單總額", "act=getTotal",
                      f"總額 {expected_total}", f"總額 {response.text}", "失敗"])

# 測試函數：獲取折扣金額


def test_get_discount(expected_discount):
    response = session.post(api_url, data={'act': 'getDiscount'})
    if response.status_code == 200 and response.text == str(expected_discount):
        table.add_row(["獲取折扣金額", "act=getDiscount",
                      f"折扣 {expected_discount}", f"折扣 {response.text}", "通過"])
    else:
        table.add_row(["獲取折扣金額", "act=getDiscount",
                      f"折扣 {expected_discount}", f"折扣 {response.text}", "失敗"])

# 生成隨機商品名稱和價格


def generate_random_name(length=5):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))


def generate_random_price(max_price=26000):
    return random.randint(1, max_price)
# 互動模式


def interactive_mode():
    while True:
        action = input("請選擇操作：1-重置訂單，2-增加商品，3-獲取總額，4-獲取折扣，0-退出：")
        if action == '1':
            test_reset()
        elif action == '2':
            name = input("輸入商品名稱：")
            price = int(input("輸入商品價格："))
            test_add_item(name, price)
        elif action == '3':
            total = int(input("輸入預期的訂單總額："))
            test_get_total(total)
        elif action == '4':
            discount = int(input("輸入預期的折扣金額："))
            test_get_discount(discount)
        elif action == '0':
            break
        else:
            print("無效的操作。")

# 全自動模式


def automated_mode():
    test_reset()
    total_price = 0
    items_added = []

    # 自動生成測試資料
    for _ in range(random.randint(1, 10)):  # 隨機決定增加的商品數量
        name = generate_random_name()
        price = generate_random_price()
        items_added.append((name, price))
        test_add_item(name, price)
        total_price += price

    # 顯示每件商品的價格
    for item in items_added:
        print(f"商品名稱: {item[0]}, 價格: {item[1]}")

    # 計算預期折扣
    expected_discount = min(10000, total_price // 1000 * 100)
    if total_price >= 5000:
        expected_discount += 100
    if expected_discount > 10000:
        expected_discount = 10000

    # 自動檢查總額和折扣
    test_get_total(total_price)
    test_get_discount(expected_discount)

# 主測試流程


def main_test_flow():
    mode = input("請選擇測試模式：[1] 互動模式 [2] 全自動模式\n")
    if mode == '1':
        interactive_mode()
    elif mode == '2':
        automated_mode()
    else:
        print("無效的輸入。")

    # 打印測試結果表格
    print(table)


# 執行測試
if __name__ == "__main__":
    main_test_flow()
