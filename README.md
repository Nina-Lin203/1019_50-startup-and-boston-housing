# 50 Startups 多元線性迴歸互動視覺化學習工具
## (Multiple Linear Regression Interactive Explorer)

一個以現代化網頁技術打造的互動式機器學習教學工具，支援 Kaggle 經典的 **50 Startups** 與 **Real Estate Price Prediction** 資料集，讓使用者直觀理解多元線性迴歸（Multiple Linear Regression）中特徵權重、截距、最小平方法（OLS 正規方程式）與模型評估指標的數學機制。

![專案預覽](https://img.shields.io/badge/Language-HTML5%20%7C%20JavaScript-orange?style=flat-square)
![TailwindCSS](https://img.shields.io/badge/Style-TailwindCSS-blue?style=flat-square)
![Chart.js](https://img.shields.io/badge/Visualization-Chart.js-coral?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

---

### 🚀 核心功能特色

1. **CSV 資料集切換**：可載入完整 50 Startups 與 414 筆 Real Estate 資料，並自動更新特徵控制、OLS 最佳解與評估指標。
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
8. **特徵選擇與 k 比較**：支援 Lasso、Forward SFS、RFE、ElasticNet 與 Exhaustive Search，以 5-fold CV RMSE/R² 排名並選擇特徵數；提供 RMSE/R² 對 k 的雙圖表分析。Exhaustive Search 限最多 8 個數值特徵。

---

### 📂 目錄結構

```text
├── index.html           # 主頁面（HTML、CSS 與互動邏輯）
├── 50_Startups.csv      # Kaggle 50 Startups 資料集（50 筆）
├── Real estate.csv      # Kaggle 房地產資料集（414 筆）
├── startups_data.json   # JSON 格式數據
├── build_app.py         # 應用程式建置腳本
└── README.md            # 專案說明文件
```

---

### 🖥️ 本機開啟

頁面會使用相對路徑讀取 CSV，請透過 VS Code Live Server 或其他本機 HTTP 伺服器開啟，不要直接以 `file://` 開啟 `index.html`。

---

### 🌐 如何部署至 GitHub Pages

1. 將本專案推送到 GitHub。
2. 進入 GitHub 儲存庫的 **Settings** -> **Pages**。
3. 在 **Build and deployment** 下選擇：
   - Source: `Deploy from a branch`
   - Branch: `main` / `/(root)`
4. 點擊 **Save**，約 1 分鐘後即可透過網址在線遊玩！
