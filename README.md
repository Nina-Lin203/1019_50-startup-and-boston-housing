# 50 Startups 多元線性迴歸互動視覺化學習工具
## (Multiple Linear Regression Interactive Explorer)

一個以現代化網頁技術打造的互動式機器學習教學工具，採用 Kaggle 經典的 **50 Startups** 資料集，讓使用者直觀理解多元線性迴歸（Multiple Linear Regression）中特徵權重、截距、最小平方法（OLS 正規方程式）與模型評估指標的數學機制。

![專案預覽](https://img.shields.io/badge/Language-HTML5%20%7C%20JavaScript-orange?style=flat-square)
![TailwindCSS](https://img.shields.io/badge/Style-TailwindCSS-blue?style=flat-square)
![Chart.js](https://img.shields.io/badge/Visualization-Chart.js-coral?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

### 🚀 核心功能特色

1. **內建完整 50 筆真實數據**：已預載 Kaggle 50 Startups 樣本，直接開啟即可離線運作。
2. **動態權重滑桿與即時公式連動**：
   $$\hat{Y} = w_1 \times \text{R\&D} + w_2 \times \text{Admin} + w_3 \times \text{Marketing} + b$$
   調整 $w_1, w_2, w_3, b$ 即時反映於預測利潤與誤差。
3. **一鍵計算 OLS 最佳解**：
   以純前端 JavaScript 實作高斯-約當消去法求解正規方程式：
   $$\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$
4. **多重視角 Chart.js 互動圖表**：
   - 實際值 vs 預測值散佈圖（含 $y = x$ 理想擬合線與三色階誤差標記）
   - 特徵投影與即時斜率旋轉
   - 殘差分佈檢驗（Homoscedasticity）
5. **即時四大誤差評估指標**：
   - 決定係數 $R^2$（最佳解達 0.9507）
   - RMSE（均方根誤差，約 $8,855）
   - MAE（平均絕對誤差，約 $6,471）
   - MSE（均方誤差）
6. **新創獲利推估試算機 (Simulator)**：輸入自訂支出推算利潤。
7. **樣本殘差總表與 CSV 匯出**：支援排序、搜尋與資料導出。

---

### 📂 目錄結構

```text
├── index.html           # 完整獨立單一網頁檔案（包含所有 HTML、CSS 與 JS）
├── 50_Startups.csv      # Kaggle 原始資料集
├── startups_data.json   # JSON 格式數據
├── build_app.py         # 應用程式建置腳本
└── README.md            # 專案說明文件
```

---

### 🌐 如何部署至 GitHub Pages

1. 將本專案推送到 GitHub。
2. 進入 GitHub 儲存庫的 **Settings** -> **Pages**。
3. 在 **Build and deployment** 下選擇：
   - Source: `Deploy from a branch`
   - Branch: `main` / `/(root)`
4. 點擊 **Save**，約 1 分鐘後即可透過網址在線遊玩！
