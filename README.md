# 測試腳本使用指南

這是一系列自動化測試腳本，用於檢查 Web 後台計算訂單總額和折扣的 API。這些腳本將驗證API的響應是否符合特定的業務規則。

## 功能描述

- `autoTest.py`: 主測試腳本，提供交互式和全自動的測試選項。
- `discountLoopTest.py`: 專門用於測試折扣計算的腳本。
- `priceLoopTest.py`: 測試不同價格點的腳本，用於尋找計算總額出錯的具體價位。
- `test.py`: 簡單的API功能測試腳本。

## 如何使用

1. 確保您的環境中已安裝Python 3。
2. 安裝必要的Python庫，如requests：
   ```sh
   pip install requests prettytable string random
   ```
3. 運行任一測試腳本：
   ```sh
   python3 <script_name>.py
   ```
   替換 `<script_name>` 為您想要運行的腳本名稱。

## 測試腳本詳細

### autoTest.py

這個腳本提供兩種模式：互動模式和全自動模式。在互動模式下，您可以手動輸入測試數據；在全自動模式下，測試數據將自動生成。

## 注意事項

- 在運行腳本前，請確保API服務器運行並可訪問。
- 根據您的API和業務規則，您可能需要調整腳本中的某些參數。
