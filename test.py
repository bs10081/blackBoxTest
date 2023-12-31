import requests

# API URL
api_url = "https://d.systemdynamics.tw/blackbox.php"

# 測試函數: 增加商品
def test_add_item():
    try:
        response = requests.post(api_url, data={'act': 'addItem', 'name': '測試商品', 'price': 1000})
        
        # 打印出原始的回應位元組和回應標頭
        print("Raw Response Content:", response.content)
        print("Headers:", response.headers)
        
        # 檢查 Content-Length 標頭
        if 'Content-Length' in response.headers:
            print("Content-Length:", response.headers['Content-Length'])
        else:
            print("Content-Length not found in headers.")
        
    except Exception as e:
        print("test_add_item Error:", e)

# 執行測試
def run_tests():
    print("Running test_add_item...")
    test_add_item()

# 主程式入口
if __name__ == "__main__":
    run_tests()

