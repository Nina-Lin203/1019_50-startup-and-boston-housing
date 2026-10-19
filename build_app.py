import json

with open('startups_data.json', 'r', encoding='utf-8') as f:
    startups_data = json.load(f)

startups_json_str = json.dumps(startups_data, indent=2, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="zh-Hant" class="h-full bg-slate-50">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>50 Startups 多元線性迴歸互動視覺化學習工具 | Multiple Linear Regression Explorer</title>
  <meta name="description" content="互動式多元線性迴歸學習工具，使用 Kaggle 經典 50 Startups 新創公司利潤資料集。提供即時參數微調、OLS 最小平方法解析解、誤差指標分析與高互動圖表。">

  <!-- Google Fonts: Outfit & Inter & Fira Code -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Inter:wght@300;400;500;600;700&family=Outfit:wght@500;600;700;800;900&display=swap" rel="stylesheet">

  <!-- FontAwesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: ['Inter', 'sans-serif'],
            heading: ['Outfit', 'sans-serif'],
            mono: ['Fira Code', 'monospace']
          }},
          colors: {{
            brand: {{
              50: '#eef2ff',
              100: '#e0e7ff',
              200: '#c7d2fe',
              500: '#6366f1',
              600: '#4f46e5',
              700: '#4338ca',
              800: '#3730a3',
              900: '#1e1b4b'
            }}
          }}
        }}
      }}
    }}
  </script>

  <!-- Chart.js CDN -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

  <!-- Canvas Confetti CDN -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>

  <style>
    :root {{
      --primary: #4f46e5;
      --primary-dark: #3730a3;
    }}
    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}
    h1, h2, h3, h4, .font-heading {{
      font-family: 'Outfit', sans-serif;
    }}
    code, pre, .font-mono {{
      font-family: 'Fira Code', monospace;
    }}

    /* Custom range input styling */
    input[type=range] {{
      -webkit-appearance: none;
      width: 100%;
      background: transparent;
    }}
    input[type=range]:focus {{
      outline: none;
    }}
    input[type=range]::-webkit-slider-runnable-track {{
      width: 100%;
      height: 8px;
      cursor: pointer;
      border-radius: 9999px;
      background: #e2e8f0;
      transition: background 0.2s;
    }}
    input[type=range]::-webkit-slider-thumb {{
      height: 20px;
      width: 20px;
      border-radius: 50%;
      background: #ffffff;
      cursor: pointer;
      -webkit-appearance: none;
      margin-top: -6px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.2), 0 0 0 2px var(--thumb-border, #4f46e5);
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }}
    input[type=range]::-webkit-slider-thumb:hover {{
      transform: scale(1.15);
      box-shadow: 0 4px 10px rgba(0,0,0,0.25), 0 0 0 3px var(--thumb-border, #4f46e5);
    }}
    input[type=range]::-webkit-slider-thumb:active {{
      transform: scale(0.95);
    }}

    /* Card glow and subtle shadows */
    .card-shadow {{
      box-shadow: 0 4px 20px -2px rgba(15, 23, 42, 0.05), 0 2px 6px -1px rgba(15, 23, 42, 0.03);
    }}
    .card-shadow-hover:hover {{
      box-shadow: 0 10px 25px -3px rgba(15, 23, 42, 0.08), 0 4px 10px -2px rgba(15, 23, 42, 0.04);
    }}

    /* Glass effect */
    .glass-card {{
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
    }}

    /* Subtle pulse animation for optimal highlight */
    @keyframes pulse-border {{
      0%, 100% {{ border-color: rgba(99, 102, 241, 0.4); box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.4); }}
      50% {{ border-color: rgba(99, 102, 241, 0.8); box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.15); }}
    }}
    .pulse-optimal {{
      animation: pulse-border 2s infinite ease-in-out;
    }}

    /* Custom scrollbars */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #f1f5f9;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #cbd5e1;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #94a3b8;
    }}
  </style>
</head>
<body class="min-h-full flex flex-col text-slate-800 antialiased selection:bg-indigo-500 selection:text-white">

  <!-- ================= TOP NAVIGATION ================= -->
  <header class="sticky top-0 z-40 bg-white/95 backdrop-blur border-b border-slate-200">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      
      <!-- Brand & Title -->
      <div class="flex items-center space-x-3">
        <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-700 via-indigo-600 to-indigo-400 flex items-center justify-center text-white shadow-md shadow-indigo-200">
          <i class="fa-solid fa-chart-line text-lg"></i>
        </div>
        <div>
          <div class="flex items-center space-x-2">
            <h1 class="text-lg font-heading font-bold text-slate-900 tracking-tight">50 Startups 多元線性迴歸</h1>
            <span class="bg-indigo-100 text-indigo-700 font-bold text-[10px] tracking-wider uppercase px-2 py-0.5 rounded-full">Interactive ML</span>
          </div>
          <p class="text-xs text-slate-500 hidden sm:block">最小平方法 (OLS) 與特徵影響力互動可視化平台</p>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="flex items-center space-x-2 sm:space-x-3">
        <button id="btn-theory-modal" class="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold text-slate-600 hover:text-indigo-600 hover:border-indigo-200 hover:bg-indigo-50/50 transition">
          <i class="fa-solid fa-book-open text-slate-400"></i>
          <span class="hidden md:inline">原理速查</span>
        </button>

        <button id="btn-reset" class="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-slate-200 text-xs font-semibold text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition" title="重設為預設參數">
          <i class="fa-solid fa-rotate-left text-slate-400"></i>
          <span class="hidden sm:inline">重設</span>
        </button>

        <button id="btn-animate-fit" class="inline-flex items-center space-x-1.5 px-3 py-1.5 rounded-lg border border-indigo-200 bg-indigo-50 text-xs font-semibold text-indigo-700 hover:bg-indigo-100 transition" title="播放數值平滑收斂至最佳解動畫">
          <i class="fa-solid fa-play text-indigo-500"></i>
          <span class="hidden sm:inline">收斂演示</span>
        </button>

        <button id="btn-apply-optimal" class="inline-flex items-center space-x-1.5 px-4 py-1.5 rounded-lg bg-gradient-to-r from-indigo-600 to-indigo-700 text-white text-xs font-bold shadow-md shadow-indigo-200 hover:from-indigo-700 hover:to-indigo-800 transition transform active:scale-95">
          <i class="fa-solid fa-bolt text-amber-300"></i>
          <span>一鍵最佳解 (OLS)</span>
        </button>
      </div>

    </div>
  </header>

  <!-- ================= MAIN CONTAINER ================= -->
  <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 space-y-6">

    <!-- HERO / LIVE MATHEMATICAL FORMULA CARD -->
    <div class="relative overflow-hidden rounded-2xl bg-gradient-to-br from-slate-900 via-indigo-950 to-slate-900 text-white p-6 sm:p-8 shadow-xl">
      <!-- Background geometric glow -->
      <div class="absolute -right-16 -top-16 w-80 h-80 rounded-full bg-indigo-600/20 blur-3xl pointer-events-none"></div>
      <div class="absolute -left-16 -bottom-16 w-80 h-80 rounded-full bg-emerald-600/10 blur-3xl pointer-events-none"></div>

      <div class="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-6">
        <div class="space-y-2 max-w-2xl">
          <div class="inline-flex items-center space-x-2 px-2.5 py-1 rounded-full bg-white/10 backdrop-blur border border-white/10 text-xs font-medium text-indigo-200">
            <i class="fa-solid fa-database text-indigo-400"></i>
            <span>50 Startups Dataset (50 筆真實企業支出與獲利數據)</span>
          </div>
          <h2 class="text-2xl sm:text-3xl font-heading font-black tracking-tight text-white">
            多元線性迴歸互動視覺化
          </h2>
          <p class="text-sm text-slate-300 leading-relaxed">
            透過調節特徵權重 <span class="font-mono text-indigo-300">w₁, w₂, w₃</span> 與截距 <span class="font-mono text-purple-300">b</span>，實時觀察模型在 50 家新創公司上的擬合曲線、預測散佈與四大評估指標（MSE / RMSE / MAE / R²）。點擊「一鍵最佳解」即可自動執行高斯-約當矩陣正規方程式解析求得全局最佳解！
          </p>
        </div>

        <!-- Dynamic Live Equation Panel -->
        <div class="bg-white/10 backdrop-blur-md border border-white/15 rounded-xl p-4 sm:p-5 flex-shrink-0 lg:w-[460px] shadow-inner">
          <div class="flex items-center justify-between text-xs text-indigo-200 uppercase tracking-wider font-semibold mb-2">
            <span class="flex items-center gap-1.5"><i class="fa-solid fa-square-root-variable"></i> 當前動態迴歸模型方程式</span>
            <span id="formula-status-tag" class="text-[10px] bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 px-2 py-0.5 rounded-full">已就緒</span>
          </div>

          <div class="font-mono text-xs sm:text-sm leading-relaxed tracking-tight bg-slate-950/60 p-3 rounded-lg border border-white/5 overflow-x-auto text-slate-100">
            <span class="text-pink-400 font-semibold">利潤 Ŷ</span> = 
            <span class="text-indigo-400 font-bold" id="eq-w-rd">0.8057</span> <span class="text-slate-400">× 研發</span> 
            <span id="eq-w-admin-sign" class="text-amber-400">-</span> <span class="text-amber-400 font-bold" id="eq-w-admin">0.0268</span> <span class="text-slate-400">× 管理</span> 
            <span id="eq-w-mkt-sign" class="text-emerald-400">+</span> <span class="text-emerald-400 font-bold" id="eq-w-mkt">0.0272</span> <span class="text-slate-400">× 行銷</span> 
            <span id="eq-b-sign" class="text-purple-400">+</span> <span class="text-purple-400 font-bold" id="eq-b">50,122.19</span>
          </div>

          <div class="mt-3 flex items-center justify-between text-[11px] text-slate-300">
            <span>最佳解參考：</span>
            <span class="font-mono text-indigo-300">R² = 0.9507 | RMSE = $8,855</span>
          </div>
        </div>
      </div>
    </div>

    <!-- MAIN TWO-COLUMN DASHBOARD GRID -->
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

      <!-- ================= LEFT PANEL (4 COLS): CONTROLS & SIMULATOR ================= -->
      <div class="lg:col-span-4 space-y-6">

        <!-- PRESET MODEL SELECTOR -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200 card-shadow">
          <div class="flex items-center justify-between mb-3">
            <h3 class="text-sm font-heading font-bold text-slate-900 flex items-center gap-2">
              <i class="fa-solid fa-sliders text-indigo-600"></i>
              特徵組合情境預設
            </h3>
            <span class="text-[11px] text-slate-400 font-medium">特徵工程實驗</span>
          </div>

          <div class="grid grid-cols-2 gap-2 text-xs">
            <button id="preset-all" class="preset-btn active py-2 px-2.5 rounded-lg border text-left font-medium transition flex flex-col justify-between border-indigo-600 bg-indigo-50 text-indigo-900 shadow-sm">
              <span class="font-bold flex items-center justify-between">
                全特徵模型
                <span class="w-2 h-2 rounded-full bg-indigo-600"></span>
              </span>
              <span class="text-[10px] text-indigo-600 mt-1">3 特徵 (R&D + Admin + Mkt)</span>
            </button>

            <button id="preset-2feat" class="preset-btn py-2 px-2.5 rounded-lg border text-left font-medium transition flex flex-col justify-between border-slate-200 bg-white text-slate-700 hover:border-slate-300">
              <span class="font-bold flex items-center justify-between">
                精簡高效組合
                <span class="w-2 h-2 rounded-full bg-slate-300"></span>
              </span>
              <span class="text-[10px] text-slate-500 mt-1">2 特徵 (R&D + Marketing)</span>
            </button>

            <button id="preset-rd-only" class="preset-btn py-2 px-2.5 rounded-lg border text-left font-medium transition flex flex-col justify-between border-slate-200 bg-white text-slate-700 hover:border-slate-300">
              <span class="font-bold flex items-center justify-between">
                單特徵基準
                <span class="w-2 h-2 rounded-full bg-slate-300"></span>
              </span>
              <span class="text-[10px] text-slate-500 mt-1">單變量 (僅研發支出)</span>
            </button>

            <button id="preset-zero" class="preset-btn py-2 px-2.5 rounded-lg border text-left font-medium transition flex flex-col justify-between border-slate-200 bg-white text-slate-700 hover:border-slate-300">
              <span class="font-bold flex items-center justify-between">
                全部歸零
                <span class="w-2 h-2 rounded-full bg-slate-300"></span>
              </span>
              <span class="text-[10px] text-slate-500 mt-1">從零開始手動調校</span>
            </button>
          </div>
        </div>

        <!-- PARAMETERS ADJUSTMENT PANEL -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200 card-shadow space-y-5">
          <div class="flex items-center justify-between border-b border-slate-100 pb-3">
            <div>
              <h3 class="text-sm font-heading font-bold text-slate-900 flex items-center gap-2">
                <i class="fa-solid fa-wand-magic-sparkles text-indigo-600"></i>
                迴歸權重參數調校
              </h3>
              <p class="text-[11px] text-slate-500">拖曳滑桿或直接輸入數值即時連動</p>
            </div>
            <button id="btn-quick-optimal" class="text-xs bg-indigo-50 hover:bg-indigo-100 text-indigo-700 font-semibold px-2.5 py-1 rounded-md transition flex items-center gap-1">
              <i class="fa-solid fa-check-double text-[10px]"></i> 最佳解
            </button>
          </div>

          <!-- 1. w1: R&D Spend -->
          <div class="space-y-1.5 p-3 rounded-xl bg-slate-50/80 border border-slate-200/80" style="--thumb-border: #4f46e5;">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-indigo-600"></span>
                <label for="slider-w-rd" class="text-xs font-bold text-slate-800">研發支出權重 (w₁)</label>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="text-[10px] text-slate-400 font-mono">OLS最佳: 0.8057</span>
                <button class="snap-btn text-[10px] text-indigo-600 hover:underline font-medium" data-target="w_rd" title="將此參數單獨對齊至最佳解">對齊</button>
              </div>
            </div>

            <div class="flex items-center gap-2">
              <input type="range" id="slider-w-rd" min="-0.5" max="2.0" step="0.001" value="0.8057" class="flex-grow">
              <input type="number" id="input-w-rd" step="0.001" value="0.8057" class="w-20 px-2 py-1 text-xs font-mono font-semibold bg-white border border-slate-300 rounded-md text-right focus:outline-none focus:ring-1 focus:ring-indigo-500">
            </div>

            <div class="flex justify-between items-center text-[10px] text-slate-400 font-mono">
              <span>-0.50</span>
              <span class="text-indigo-600 font-semibold">R&D Spend (最強正向驅動力)</span>
              <span>+2.00</span>
            </div>
          </div>

          <!-- 2. w2: Administration -->
          <div class="space-y-1.5 p-3 rounded-xl bg-slate-50/80 border border-slate-200/80" style="--thumb-border: #f59e0b;">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-amber-500"></span>
                <label for="slider-w-admin" class="text-xs font-bold text-slate-800">管理支出權重 (w₂)</label>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="text-[10px] text-slate-400 font-mono">OLS最佳: -0.0268</span>
                <button class="snap-btn text-[10px] text-amber-600 hover:underline font-medium" data-target="w_admin" title="將此參數單獨對齊至最佳解">對齊</button>
              </div>
            </div>

            <div class="flex items-center gap-2">
              <input type="range" id="slider-w-admin" min="-0.5" max="0.5" step="0.001" value="-0.0268" class="flex-grow">
              <input type="number" id="input-w-admin" step="0.001" value="-0.0268" class="w-20 px-2 py-1 text-xs font-mono font-semibold bg-white border border-slate-300 rounded-md text-right focus:outline-none focus:ring-1 focus:ring-amber-500">
            </div>

            <div class="flex justify-between items-center text-[10px] text-slate-400 font-mono">
              <span>-0.50</span>
              <span class="text-amber-600 font-semibold">Administration (接近 0，統計不顯著)</span>
              <span>+0.50</span>
            </div>
          </div>

          <!-- 3. w3: Marketing Spend -->
          <div class="space-y-1.5 p-3 rounded-xl bg-slate-50/80 border border-slate-200/80" style="--thumb-border: #10b981;">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                <label for="slider-w-mkt" class="text-xs font-bold text-slate-800">行銷支出權重 (w₃)</label>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="text-[10px] text-slate-400 font-mono">OLS最佳: 0.0272</span>
                <button class="snap-btn text-[10px] text-emerald-600 hover:underline font-medium" data-target="w_mkt" title="將此參數單獨對齊至最佳解">對齊</button>
              </div>
            </div>

            <div class="flex items-center gap-2">
              <input type="range" id="slider-w-mkt" min="-0.2" max="0.5" step="0.001" value="0.0272" class="flex-grow">
              <input type="number" id="input-w-mkt" step="0.001" value="0.0272" class="w-20 px-2 py-1 text-xs font-mono font-semibold bg-white border border-slate-300 rounded-md text-right focus:outline-none focus:ring-1 focus:ring-emerald-500">
            </div>

            <div class="flex justify-between items-center text-[10px] text-slate-400 font-mono">
              <span>-0.20</span>
              <span class="text-emerald-600 font-semibold">Marketing Spend (微幅正向驅動)</span>
              <span>+0.50</span>
            </div>
          </div>

          <!-- 4. b: Intercept -->
          <div class="space-y-1.5 p-3 rounded-xl bg-slate-50/80 border border-slate-200/80" style="--thumb-border: #8b5cf6;">
            <div class="flex items-center justify-between">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-purple-500"></span>
                <label for="slider-b" class="text-xs font-bold text-slate-800">基準截距常數 (b / 截距項)</label>
              </div>
              <div class="flex items-center gap-1.5">
                <span class="text-[10px] text-slate-400 font-mono">OLS最佳: 50,122</span>
                <button class="snap-btn text-[10px] text-purple-600 hover:underline font-medium" data-target="b" title="將此參數單獨對齊至最佳解">對齊</button>
              </div>
            </div>

            <div class="flex items-center gap-2">
              <input type="range" id="slider-b" min="-50000" max="150000" step="100" value="50122.19" class="flex-grow">
              <input type="number" id="input-b" step="100" value="50122.19" class="w-24 px-2 py-1 text-xs font-mono font-semibold bg-white border border-slate-300 rounded-md text-right focus:outline-none focus:ring-1 focus:ring-purple-500">
            </div>

            <div class="flex justify-between items-center text-[10px] text-slate-400 font-mono">
              <span>-$50k</span>
              <span class="text-purple-600 font-semibold">基底利潤 ($)</span>
              <span>+$150k</span>
            </div>
          </div>

          <!-- Bottom Action Buttons in Card -->
          <div class="pt-2 flex gap-2">
            <button id="btn-nudge-down" class="flex-1 py-1.5 px-2 bg-slate-100 hover:bg-slate-200 rounded-lg text-xs font-semibold text-slate-700 transition">
              <i class="fa-solid fa-angle-left"></i> 微調 -1%
            </button>
            <button id="btn-nudge-up" class="flex-1 py-1.5 px-2 bg-slate-100 hover:bg-slate-200 rounded-lg text-xs font-semibold text-slate-700 transition">
              微調 +1% <i class="fa-solid fa-angle-right"></i>
            </button>
            <button id="btn-randomize" class="py-1.5 px-3 bg-slate-100 hover:bg-slate-200 rounded-lg text-xs font-semibold text-slate-700 transition" title="隨機生成權重以測試誤差">
              <i class="fa-solid fa-dice"></i>
            </button>
          </div>
        </div>

        <!-- PROFIT SIMULATOR (新創利潤推估試算機) -->
        <div class="bg-gradient-to-br from-indigo-50/70 to-slate-50 rounded-2xl p-5 border border-indigo-100 card-shadow">
          <div class="flex items-center justify-between mb-3">
            <h3 class="text-sm font-heading font-bold text-slate-900 flex items-center gap-2">
              <i class="fa-solid fa-calculator text-indigo-600"></i>
              新創利潤即時試算機
            </h3>
            <span class="text-[10px] bg-indigo-100 text-indigo-700 font-bold px-2 py-0.5 rounded-full">Simulator</span>
          </div>
          <p class="text-xs text-slate-500 mb-4">輸入自訂支出金額，即刻使用當前模型公式推估獲利：</p>

          <div class="space-y-2.5 text-xs">
            <div>
              <div class="flex justify-between text-slate-600 mb-1">
                <span>研發支出 (R&D Spend):</span>
                <span class="font-mono font-semibold" id="sim-rd-val">$100,000</span>
              </div>
              <input type="range" id="sim-rd" min="0" max="200000" step="5000" value="100000" class="w-full">
            </div>

            <div>
              <div class="flex justify-between text-slate-600 mb-1">
                <span>管理支出 (Administration):</span>
                <span class="font-mono font-semibold" id="sim-admin-val">$120,000</span>
              </div>
              <input type="range" id="sim-admin" min="0" max="200000" step="5000" value="120000" class="w-full">
            </div>

            <div>
              <div class="flex justify-between text-slate-600 mb-1">
                <span>行銷支出 (Marketing Spend):</span>
                <span class="font-mono font-semibold" id="sim-mkt-val">$250,000</span>
              </div>
              <input type="range" id="sim-mkt" min="0" max="500000" step="10000" value="250000" class="w-full">
            </div>
          </div>

          <!-- Calculated Result Box -->
          <div class="mt-4 p-3.5 rounded-xl bg-white border border-indigo-200 shadow-sm flex items-center justify-between">
            <div>
              <div class="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">預估企業利潤 (Predicted Profit)</div>
              <div class="text-xl sm:text-2xl font-heading font-extrabold text-indigo-700 tracking-tight" id="sim-result-profit">$134,269</div>
            </div>
            <div class="text-right">
              <span id="sim-vs-avg-badge" class="inline-flex items-center gap-1 text-[11px] font-bold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-700 border border-emerald-200">
                <i class="fa-solid fa-arrow-trend-up"></i> 高於平均
              </span>
              <div class="text-[10px] text-slate-400 mt-0.5">母體均值: $112,013</div>
            </div>
          </div>
        </div>

      </div>

      <!-- ================= RIGHT PANEL (8 COLS): METRICS, CHARTS & TABLE ================= -->
      <div class="lg:col-span-8 space-y-6">

        <!-- 4 KPI ERROR METRIC CARDS -->
        <div class="grid grid-cols-2 sm:grid-cols-4 gap-3.5">
          
          <!-- 1. R² CARD -->
          <div class="bg-white rounded-2xl p-4 border border-slate-200 card-shadow relative overflow-hidden group">
            <div class="absolute top-0 left-0 right-0 h-1 bg-indigo-600" id="metric-bar-r2"></div>
            <div class="flex items-center justify-between text-slate-400 text-xs mb-1">
              <span class="font-bold text-slate-700 uppercase tracking-wider text-[11px]">R² 決定係數</span>
              <i class="fa-solid fa-bullseye text-indigo-500"></i>
            </div>
            <div class="text-2xl sm:text-3xl font-heading font-black text-slate-900 tracking-tight" id="metric-r2">0.9507</div>
            <div class="mt-2 flex items-center justify-between">
              <span id="metric-r2-badge" class="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700">卓越擬合</span>
              <span class="text-[10px] text-slate-400 font-mono" id="metric-r2-diff">Δ: 0.0000</span>
            </div>
            <!-- Mini progress bar -->
            <div class="w-full bg-slate-100 h-1.5 rounded-full mt-2.5 overflow-hidden">
              <div id="metric-r2-progress" class="bg-indigo-600 h-full rounded-full transition-all duration-300" style="width: 95.1%;"></div>
            </div>
          </div>

          <!-- 2. RMSE CARD -->
          <div class="bg-white rounded-2xl p-4 border border-slate-200 card-shadow relative overflow-hidden">
            <div class="absolute top-0 left-0 right-0 h-1 bg-emerald-500" id="metric-bar-rmse"></div>
            <div class="flex items-center justify-between text-slate-400 text-xs mb-1">
              <span class="font-bold text-slate-700 uppercase tracking-wider text-[11px]">RMSE (均方根)</span>
              <i class="fa-solid fa-scale-balanced text-emerald-500"></i>
            </div>
            <div class="text-2xl sm:text-3xl font-heading font-black text-slate-900 tracking-tight font-mono text-[22px] sm:text-[24px]" id="metric-rmse">$8,855</div>
            <div class="mt-2 flex items-center justify-between">
              <span class="text-[10px] text-slate-500">標準誤差單位同 $</span>
              <span class="text-[10px] text-slate-400 font-mono" id="metric-rmse-diff">最佳: $8,855</span>
            </div>
            <div class="w-full bg-slate-100 h-1.5 rounded-full mt-2.5 overflow-hidden">
              <div id="metric-rmse-progress" class="bg-emerald-500 h-full rounded-full transition-all duration-300" style="width: 88%;"></div>
            </div>
          </div>

          <!-- 3. MAE CARD -->
          <div class="bg-white rounded-2xl p-4 border border-slate-200 card-shadow relative overflow-hidden">
            <div class="absolute top-0 left-0 right-0 h-1 bg-amber-500" id="metric-bar-mae"></div>
            <div class="flex items-center justify-between text-slate-400 text-xs mb-1">
              <span class="font-bold text-slate-700 uppercase tracking-wider text-[11px]">MAE (絕對誤差)</span>
              <i class="fa-solid fa-ruler-combined text-amber-500"></i>
            </div>
            <div class="text-2xl sm:text-3xl font-heading font-black text-slate-900 tracking-tight font-mono text-[22px] sm:text-[24px]" id="metric-mae">$6,471</div>
            <div class="mt-2 flex items-center justify-between">
              <span class="text-[10px] text-slate-500">平均單筆誤差金額</span>
              <span class="text-[10px] text-slate-400 font-mono" id="metric-mae-diff">最佳: $6,471</span>
            </div>
            <div class="w-full bg-slate-100 h-1.5 rounded-full mt-2.5 overflow-hidden">
              <div id="metric-mae-progress" class="bg-amber-500 h-full rounded-full transition-all duration-300" style="width: 90%;"></div>
            </div>
          </div>

          <!-- 4. MSE CARD -->
          <div class="bg-white rounded-2xl p-4 border border-slate-200 card-shadow relative overflow-hidden">
            <div class="absolute top-0 left-0 right-0 h-1 bg-rose-500" id="metric-bar-mse"></div>
            <div class="flex items-center justify-between text-slate-400 text-xs mb-1">
              <span class="font-bold text-slate-700 uppercase tracking-wider text-[11px]">MSE (均方誤差)</span>
              <i class="fa-solid fa-arrows-to-dot text-rose-500"></i>
            </div>
            <div class="text-2xl sm:text-3xl font-heading font-black text-slate-900 tracking-tight font-mono text-[19px] sm:text-[21px]" id="metric-mse">7.84e+07</div>
            <div class="mt-2 flex items-center justify-between">
              <span class="text-[10px] text-slate-500">OLS 目標損失函數</span>
              <span class="text-[10px] text-slate-400 font-mono" id="metric-mse-diff">越小越好</span>
            </div>
            <div class="w-full bg-slate-100 h-1.5 rounded-full mt-2.5 overflow-hidden">
              <div id="metric-mse-progress" class="bg-rose-500 h-full rounded-full transition-all duration-300" style="width: 85%;"></div>
            </div>
          </div>

        </div>

        <!-- VISUALIZATION CANVAS CARD -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200 card-shadow space-y-4">
          
          <!-- Chart Header & Controls -->
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-slate-100 pb-4">
            
            <!-- Chart Tabs -->
            <div class="flex items-center bg-slate-100 p-1 rounded-xl text-xs font-semibold">
              <button id="tab-actual-vs-pred" class="chart-tab px-3 py-1.5 rounded-lg bg-white text-indigo-700 shadow-sm transition">
                <i class="fa-solid fa-chart-line mr-1"></i> 實際 vs 預測
              </button>
              <button id="tab-feature-scatter" class="chart-tab px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition">
                <i class="fa-solid fa-bezier-curve mr-1"></i> 特徵投影與斜率
              </button>
              <button id="tab-residuals" class="chart-tab px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition">
                <i class="fa-solid fa-chart-simple mr-1"></i> 殘差分佈 (Residuals)
              </button>
            </div>

            <!-- Filters & Feature Dropdown -->
            <div class="flex items-center gap-2">
              <!-- Feature selector (for Tab 2) -->
              <div id="feature-select-wrapper" class="hidden">
                <select id="select-feature-projection" class="bg-slate-50 border border-slate-200 text-xs font-semibold text-slate-700 rounded-lg px-2.5 py-1.5 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                  <option value="rd">X軸: 研發支出 (R&D Spend)</option>
                  <option value="mkt">X軸: 行銷支出 (Marketing Spend)</option>
                  <option value="admin">X軸: 管理支出 (Administration)</option>
                </select>
              </div>

              <!-- State Filter -->
              <div class="flex items-center gap-1.5 text-xs">
                <i class="fa-solid fa-filter text-slate-400"></i>
                <select id="select-state-filter" class="bg-slate-50 border border-slate-200 text-xs font-semibold text-slate-700 rounded-lg px-2.5 py-1.5 focus:outline-none focus:ring-1 focus:ring-indigo-500">
                  <option value="All">全區 (50 家公司)</option>
                  <option value="New York">New York</option>
                  <option value="California">California</option>
                  <option value="Florida">Florida</option>
                </select>
              </div>
            </div>

          </div>

          <!-- Chart Description / Guide -->
          <div class="flex flex-wrap items-center justify-between text-xs text-slate-500 gap-2 bg-slate-50/70 px-3 py-2 rounded-lg border border-slate-100">
            <div id="chart-hint-text" class="flex items-center gap-2">
              <span class="inline-block w-2 h-2 rounded-full bg-indigo-500"></span>
              <span><strong>完美擬合基準線</strong>：虛線為 y = x。點越靠近對角虛線，代表預測越精準。</span>
            </div>
            <div class="flex items-center gap-3 text-[11px]">
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-emerald-500"></span> 誤差 &lt; 5%</span>
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-amber-500"></span> 5% ~ 15%</span>
              <span class="flex items-center gap-1"><span class="w-2 h-2 rounded-full bg-rose-500"></span> &gt; 15% (離群)</span>
            </div>
          </div>

          <!-- Canvas Container -->
          <div class="relative w-full h-[360px] sm:h-[400px]">
            <canvas id="regressionChart"></canvas>
          </div>

        </div>

        <!-- 50 STARTUPS DATASET & RESIDUALS TABLE -->
        <div class="bg-white rounded-2xl p-5 border border-slate-200 card-shadow space-y-4">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-3">
            <div>
              <h3 class="text-sm font-heading font-bold text-slate-900 flex items-center gap-2">
                <i class="fa-solid fa-table-list text-indigo-600"></i>
                50 Startups 樣本殘差明細表
              </h3>
              <p class="text-xs text-slate-500">即時檢視各新創公司利潤之預測值與偏差幅度</p>
            </div>

            <!-- Search, Sort & Export -->
            <div class="flex items-center gap-2">
              <div class="relative">
                <input type="text" id="table-search" placeholder="搜尋地區或序號..." class="text-xs bg-slate-50 border border-slate-200 rounded-lg pl-7 pr-2.5 py-1.5 focus:outline-none focus:ring-1 focus:ring-indigo-500 w-36 sm:w-44">
                <i class="fa-solid fa-magnifying-glass text-slate-400 absolute left-2.5 top-2.5 text-[10px]"></i>
              </div>

              <select id="table-sort" class="text-xs bg-slate-50 border border-slate-200 rounded-lg px-2 py-1.5 font-medium text-slate-700 focus:outline-none">
                <option value="id">序號 (#1-50)</option>
                <option value="actual-desc">利潤由高到低</option>
                <option value="error-desc">絕對誤差由大到小</option>
                <option value="rd-desc">研發支出最高</option>
              </select>

              <button id="btn-export-csv" class="text-xs bg-slate-100 hover:bg-slate-200 text-slate-700 font-semibold px-2.5 py-1.5 rounded-lg transition" title="下載包含當前預測與殘差的 CSV 檔">
                <i class="fa-solid fa-download"></i>
              </button>
            </div>
          </div>

          <!-- Table Container with scrolling -->
          <div class="overflow-x-auto max-h-72 rounded-xl border border-slate-100">
            <table class="min-w-full divide-y divide-slate-200 text-xs">
              <thead class="bg-slate-50 sticky top-0 z-10 font-bold text-slate-600 text-left">
                <tr>
                  <th class="py-2.5 px-3">#</th>
                  <th class="py-2.5 px-3">地區 (State)</th>
                  <th class="py-2.5 px-3">研發支出 (R&D)</th>
                  <th class="py-2.5 px-3">管理支出 (Admin)</th>
                  <th class="py-2.5 px-3">行銷支出 (Mkt)</th>
                  <th class="py-2.5 px-3 text-right">實際利潤 (Y)</th>
                  <th class="py-2.5 px-3 text-right">預測利潤 (Ŷ)</th>
                  <th class="py-2.5 px-3 text-right">殘差 (e)</th>
                  <th class="py-2.5 px-3 text-center">誤差率</th>
                </tr>
              </thead>
              <tbody id="table-body" class="divide-y divide-slate-100 bg-white font-mono">
                <!-- Dynamically populated via JS -->
              </tbody>
            </table>
          </div>

          <div class="flex items-center justify-between text-[11px] text-slate-400">
            <span>顯示 <span id="table-row-count" class="font-bold text-slate-700">50</span> 筆樣本</span>
            <span>點擊欄位排序或使用上方過濾器檢視子群體</span>
          </div>
        </div>

      </div>

    </div>

    <!-- ================= THEORY & MATHEMATICAL EDUCATION ACCORDION ================= -->
    <section class="bg-white rounded-2xl p-6 sm:p-8 border border-slate-200 card-shadow space-y-6">
      <div class="flex items-center justify-between border-b border-slate-100 pb-4">
        <div>
          <h2 class="text-lg sm:text-xl font-heading font-black text-slate-900 flex items-center gap-2">
            <i class="fa-solid fa-graduation-cap text-indigo-600"></i>
            多元線性迴歸 (Multiple Linear Regression) 核心原理與 50 Startups 統計洞察
          </h2>
          <p class="text-xs text-slate-500 mt-0.5">理解從資料矩陣到閉式解 (Closed-form Solution) 的數學機制</p>
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs text-slate-600 leading-relaxed">
        
        <!-- Pillar 1 -->
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-100 space-y-2">
          <div class="font-bold text-slate-900 text-sm flex items-center gap-1.5">
            <span class="w-6 h-6 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center text-xs font-mono font-bold">1</span>
            最小平方法與正規方程式 (OLS)
          </div>
          <p>
            線性迴歸旨在最小化所有樣本殘差平方和：
            <br><code class="bg-white px-1.5 py-0.5 rounded border text-indigo-600 font-mono">Loss = Σ(yᵢ - ŷᵢ)² = ||y - Xw||²</code>
          </p>
          <p>
            對權重向量求梯度並令其為零，即可解出不需要迭代的全局最佳解析解：
            <br><code class="bg-white px-1.5 py-0.5 rounded border text-indigo-600 font-mono">w* = (XᵀX)⁻¹ Xᵀy</code>
            <br>本工具中的「一鍵最佳解」即在前端以純 JavaScript 透過高斯-約當消去法實時計算此矩陣反矩陣！
          </p>
        </div>

        <!-- Pillar 2 -->
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-100 space-y-2">
          <div class="font-bold text-slate-900 text-sm flex items-center gap-1.5">
            <span class="w-6 h-6 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center text-xs font-mono font-bold">2</span>
            為什麼研發支出 (R&D) 決定一切？
          </div>
          <p>
            在 50 Startups 資料集中，研發支出與利潤的 Pearson 相關係數高達 <strong>r = 0.973</strong>。
          </p>
          <p>
            即便僅使用單一特徵「研發支出」，決定係數 <span class="font-mono text-indigo-600">R²</span> 就已經高達 <strong>0.9465</strong>。
            而加入管理支出 (Administration) 與行銷支出後，<span class="font-mono text-indigo-600">R²</span> 僅微幅提升至 <strong>0.9507</strong>。
            這揭示了企業創新技術研發是獲利的絕對主導驅動力。
          </p>
        </div>

        <!-- Pillar 3 -->
        <div class="p-4 rounded-xl bg-slate-50 border border-slate-100 space-y-2">
          <div class="font-bold text-slate-900 text-sm flex items-center gap-1.5">
            <span class="w-6 h-6 rounded-lg bg-indigo-100 text-indigo-700 flex items-center justify-center text-xs font-mono font-bold">3</span>
            管理支出的多重共線性與 P 值
          </div>
          <p>
            在完整的 3 特徵模型中，管理支出的係數約為 <strong>-0.0268</strong>，但其假說檢定的 P-value 高達 <strong>0.6</strong> 以上（遠大於顯著性標準 0.05）。
          </p>
          <p>
            在統計模型中，這意味著「管理支出對利潤的線性貢獻在統計上不顯著」，在後向剔除法 (Backward Elimination) 或 Lasso 懲罰迴歸中，管理支出往往是第一個被篩選剔除的特徵。
          </p>
        </div>

      </div>
    </section>

  </main>

  <!-- ================= FOOTER ================= -->
  <footer class="bg-white border-t border-slate-200 py-6 mt-12 text-center text-xs text-slate-500">
    <div class="max-w-7xl mx-auto px-4 space-y-1">
      <p class="font-medium text-slate-700">50 Startups 多元線性迴歸互動視覺化學習工具</p>
      <p>基於 Kaggle 經典 50 Startups 資料集 · 採用 JavaScript OLS 矩陣閉式解 · Chart.js 數據視覺化</p>
      <p class="text-[11px] text-slate-400">© 2026 AIoT Machine Learning Interactive Laboratory. Single-file standalone HTML application.</p>
    </div>
  </footer>

  <!-- ================= THEORY MODAL ================= -->
  <div id="theory-modal" class="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/60 backdrop-blur-sm hidden p-4">
    <div class="bg-white rounded-2xl max-w-2xl w-full p-6 shadow-2xl border border-slate-200 max-h-[90vh] overflow-y-auto space-y-4">
      <div class="flex items-center justify-between border-b border-slate-100 pb-3">
        <h3 class="text-base font-heading font-bold text-slate-900 flex items-center gap-2">
          <i class="fa-solid fa-circle-info text-indigo-600"></i>
          多元線性迴歸評估指標計算公式
        </h3>
        <button id="btn-close-modal" class="w-8 h-8 rounded-lg bg-slate-100 text-slate-500 hover:bg-slate-200 flex items-center justify-center text-sm transition">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>

      <div class="space-y-4 text-xs text-slate-600 leading-relaxed">
        <div class="p-3 rounded-lg bg-slate-50 border border-slate-200">
          <div class="font-bold text-slate-900 mb-1">1. 決定係數 (R-Squared, R²)</div>
          <div class="font-mono text-indigo-600 mb-1">R² = 1 - (SS_res / SS_tot) = 1 - [Σ(yᵢ - ŷᵢ)² / Σ(yᵢ - ȳ)²]</div>
          <p>衡量模型自變數能解釋目標變數總變異量 (Variance) 的百分比。值越接近 1.0 代表擬合效果越完美；若小於 0 則代表模型表現比直接猜平均值還差。</p>
        </div>

        <div class="p-3 rounded-lg bg-slate-50 border border-slate-200">
          <div class="font-bold text-slate-900 mb-1">2. 均方根誤差 (Root Mean Squared Error, RMSE)</div>
          <div class="font-mono text-indigo-600 mb-1">RMSE = √[ (1/N) Σ(yᵢ - ŷᵢ)² ]</div>
          <p>對誤差平方和開根號，將單位拉回與目標變數利潤同等的美元 ($)。RMSE 對極端異常值（大殘差）較為敏感。</p>
        </div>

        <div class="p-3 rounded-lg bg-slate-50 border border-slate-200">
          <div class="font-bold text-slate-900 mb-1">3. 平均絕對誤差 (Mean Absolute Error, MAE)</div>
          <div class="font-mono text-indigo-600 mb-1">MAE = (1/N) Σ|yᵢ - ŷᵢ|</div>
          <p>所有樣本預測誤差絕對值的平均數，直觀代表「平均每家新創公司我們猜錯了多少美元」。對異常值抗性較高。</p>
        </div>

        <div class="p-3 rounded-lg bg-slate-50 border border-slate-200">
          <div class="font-bold text-slate-900 mb-1">4. 均方誤差 (Mean Squared Error, MSE)</div>
          <div class="font-mono text-indigo-600 mb-1">MSE = (1/N) Σ(yᵢ - ŷᵢ)²</div>
          <p>線性迴歸的基礎損失函數 (Loss Function)。在數學上具備連續平滑一階可導特性，是 OLS 與梯度下降優化的核心標的。</p>
        </div>
      </div>

      <div class="pt-3 border-t border-slate-100 text-right">
        <button id="btn-modal-ok" class="px-4 py-2 bg-indigo-600 hover:bg-indigo-700 text-white rounded-lg text-xs font-bold transition">
          我知道了
        </button>
      </div>
    </div>
  </div>

  <!-- ================= JAVASCRIPT LOGIC ================= -->
  <script>
    // 1. EMBEDDED REAL 50 STARTUPS DATASET
    const STARTUPS_DATA = {startups_json_str};

    // Precalculate Dataset summary statistics
    const N_SAMPLES = STARTUPS_DATA.length;
    const Y_ACTUAL = STARTUPS_DATA.map(d => d.Profit);
    const Y_MEAN = Y_ACTUAL.reduce((a, b) => a + b, 0) / N_SAMPLES;
    const SS_TOT = Y_ACTUAL.reduce((sum, y) => sum + Math.pow(y - Y_MEAN, 2), 0);

    // 2. MATHEMATICAL OLS SOLVER (GAUSS-JORDAN ELIMINATION)
    function solveOLS(activeFeatureKeys) {{
      // activeFeatureKeys: array of keys e.g. ['rd', 'admin', 'mkt']
      const keyMap = {{
        'rd': 'R&D Spend',
        'admin': 'Administration',
        'mkt': 'Marketing Spend'
      }};

      const selectedKeys = activeFeatureKeys.filter(k => keyMap[k]);
      const p = selectedKeys.length + 1; // features + intercept
      
      // If no feature selected, predict mean
      if (selectedKeys.length === 0) {{
        return {{
          b: Y_MEAN,
          w_rd: 0,
          w_admin: 0,
          w_mkt: 0
        }};
      }}

      // Build design matrix X with bias column of 1s
      // X: N x p
      const X = STARTUPS_DATA.map(row => [1, ...selectedKeys.map(k => row[keyMap[k]])]);

      // Compute XtX (p x p) and Xty (p x 1)
      const XtX = Array.from({{ length: p }}, () => new Array(p).fill(0));
      const Xty = new Array(p).fill(0);

      for (let i = 0; i < N_SAMPLES; i++) {{
        const yi = Y_ACTUAL[i];
        for (let r = 0; r < p; r++) {{
          Xty[r] += X[i][r] * yi;
          for (let c = 0; c < p; c++) {{
            XtX[r][c] += X[i][r] * X[i][c];
          }}
        }}
      }}

      // Gauss-Jordan elimination on [XtX | I]
      const M = XtX.map((row, r) => [...row, ...Array.from({{ length: p }}, (_, c) => (r === c ? 1 : 0))]);
      for (let i = 0; i < p; i++) {{
        let maxRow = i;
        for (let r = i + 1; r < p; r++) {{
          if (Math.abs(M[r][i]) > Math.abs(M[maxRow][i])) maxRow = r;
        }}
        [M[i], M[maxRow]] = [M[maxRow], M[i]];
        const pivot = M[i][i];
        if (Math.abs(pivot) < 1e-12) return null; // singular
        for (let c = 0; c < 2 * p; c++) M[i][c] /= pivot;
        for (let r = 0; r < p; r++) {{
          if (r !== i) {{
            const factor = M[r][i];
            for (let c = 0; c < 2 * p; c++) M[r][c] -= factor * M[i][c];
          }}
        }}
      }}

      const inv = M.map(row => row.slice(p));
      const beta = new Array(p).fill(0);
      for (let r = 0; r < p; r++) {{
        for (let c = 0; c < p; c++) {{
          beta[r] += inv[r][c] * Xty[c];
        }}
      }}

      const result = {{
        b: beta[0],
        w_rd: 0,
        w_admin: 0,
        w_mkt: 0
      }};

      selectedKeys.forEach((k, idx) => {{
        result['w_' + k] = beta[idx + 1];
      }});

      return result;
    }}

    // Compute Global 3-feature Optimal
    const GLOBAL_OPTIMAL = solveOLS(['rd', 'admin', 'mkt']);

    // 3. APPLICATION STATE
    const state = {{
      w_rd: GLOBAL_OPTIMAL.w_rd,
      w_admin: GLOBAL_OPTIMAL.w_admin,
      w_mkt: GLOBAL_OPTIMAL.w_mkt,
      b: GLOBAL_OPTIMAL.b,
      activePreset: 'all',
      chartTab: 'actual-vs-pred',
      stateFilter: 'All',
      projectionFeature: 'rd',
      tableSort: 'id',
      tableSearch: ''
    }};

    // 4. CHART.JS INITIALIZATION
    let chartInstance = null;
    const ctx = document.getElementById('regressionChart').getContext('2d');

    function initChart() {{
      chartInstance = new Chart(ctx, {{
        type: 'scatter',
        data: {{
          datasets: [
            {{
              label: '完美預測對角線 (y = x)',
              type: 'line',
              data: [{{ x: 0, y: 0 }}, {{ x: 200000, y: 200000 }}],
              borderColor: '#94a3b8',
              borderWidth: 2,
              borderDash: [6, 6],
              pointRadius: 0,
              fill: false,
              order: 2
            }},
            {{
              label: '新創企業樣本點',
              type: 'scatter',
              data: [],
              backgroundColor: [],
              borderColor: '#ffffff',
              borderWidth: 1.5,
              pointRadius: 6,
              pointHoverRadius: 9,
              order: 1
            }}
          ]
        }},
        options: {{
          responsive: true,
          maintainAspectRatio: false,
          animation: {{
            duration: 250
          }},
          plugins: {{
            legend: {{
              position: 'top',
              labels: {{
                font: {{ family: 'Outfit', size: 12, weight: 600 }},
                usePointStyle: true,
                boxWidth: 8
              }}
            }},
            tooltip: {{
              backgroundColor: 'rgba(15, 23, 42, 0.92)',
              titleFont: {{ family: 'Outfit', size: 13, weight: 700 }},
              bodyFont: {{ family: 'Fira Code', size: 12 }},
              padding: 12,
              cornerRadius: 10,
              displayColors: false,
              callbacks: {{
                label: function(context) {{
                  const raw = context.raw;
                  if (!raw || raw.meta === undefined) return '';
                  const item = STARTUPS_DATA[raw.meta];
                  const residual = raw.y - raw.x;
                  const pct = Math.abs(residual / (raw.x || 1) * 100).toFixed(1);
                  return [
                    `企業 #${{raw.meta + 1}} (${{item.State}})`,
                    `實際利潤: $${{Math.round(raw.x).toLocaleString()}}`,
                    `預測利潤: $${{Math.round(raw.y).toLocaleString()}}`,
                    `預測殘差: ${{residual >= 0 ? '+' : ''}}${{Math.round(residual).toLocaleString()}} (誤差 ${{pct}}%)`,
                    `研發: $${{Math.round(item['R&D Spend']).toLocaleString()}} | 行銷: $${{Math.round(item['Marketing Spend']).toLocaleString()}}`
                  ];
                }}
              }}
            }}
          }},
          scales: {{
            x: {{
              title: {{
                display: true,
                text: '實際利潤 (Actual Profit $)',
                font: {{ family: 'Inter', size: 12, weight: 600 }}
              }},
              grid: {{ color: '#f1f5f9' }},
              ticks: {{
                callback: v => '$' + (v >= 1000 ? (v / 1000) + 'k' : v)
              }}
            }},
            y: {{
              title: {{
                display: true,
                text: '模型預測利潤 (Predicted Profit $)',
                font: {{ family: 'Inter', size: 12, weight: 600 }}
              }},
              grid: {{ color: '#f1f5f9' }},
              ticks: {{
                callback: v => '$' + (v >= 1000 ? (v / 1000) + 'k' : v)
              }}
            }}
          }}
        }}
      }});
    }}

    // 5. METRICS & PREDICTION CALCULATIONS
    function computePredictions() {{
      const predictions = [];
      let ss_res = 0;
      let sum_abs_err = 0;

      for (let i = 0; i < N_SAMPLES; i++) {{
        const row = STARTUPS_DATA[i];
        const y_pred = state.w_rd * row['R&D Spend'] +
                       state.w_admin * row['Administration'] +
                       state.w_mkt * row['Marketing Spend'] +
                       state.b;
        const y_act = row.Profit;
        const res = y_act - y_pred;
        const abs_err = Math.abs(res);
        
        ss_res += res * res;
        sum_abs_err += abs_err;

        predictions.push({{
          index: i,
          item: row,
          actual: y_act,
          predicted: y_pred,
          residual: res,
          absError: abs_err,
          pctError: (abs_err / (y_act || 1)) * 100
        }});
      }}

      const mse = ss_res / N_SAMPLES;
      const rmse = Math.sqrt(mse);
      const mae = sum_abs_err / N_SAMPLES;
      const r2 = 1 - (ss_res / SS_TOT);

      return {{ predictions, mse, rmse, mae, r2 }};
    }}

    // 6. UI UPDATE DISPATCHER
    function updateUI() {{
      const {{ predictions, mse, rmse, mae, r2 }} = computePredictions();

      // A. Update Dynamic Formula in Hero
      document.getElementById('eq-w-rd').textContent = state.w_rd.toFixed(4);
      
      const adminVal = Math.abs(state.w_admin);
      document.getElementById('eq-w-admin-sign').textContent = state.w_admin >= 0 ? '+' : '-';
      document.getElementById('eq-w-admin').textContent = adminVal.toFixed(4);

      const mktVal = Math.abs(state.w_mkt);
      document.getElementById('eq-w-mkt-sign').textContent = state.w_mkt >= 0 ? '+' : '-';
      document.getElementById('eq-w-mkt').textContent = mktVal.toFixed(4);

      const bVal = Math.abs(state.b);
      document.getElementById('eq-b-sign').textContent = state.b >= 0 ? '+' : '-';
      document.getElementById('eq-b').textContent = bVal.toLocaleString('en-US', {{ minimumFractionDigits: 2, maximumFractionDigits: 2 }});

      // B. Update KPI Metrics Cards
      const r2Display = isNaN(r2) ? '0.0000' : (r2 < -1.0 ? r2.toFixed(2) : r2.toFixed(4));
      document.getElementById('metric-r2').textContent = r2Display;
      
      const r2Badge = document.getElementById('metric-r2-badge');
      const r2Progress = document.getElementById('metric-r2-progress');
      const r2Pct = Math.max(0, Math.min(100, r2 * 100));
      r2Progress.style.width = `${{r2Pct}}%`;

      if (r2 >= 0.94) {{
        r2Badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-700';
        r2Badge.textContent = '卓越 (Excellent)';
      }} else if (r2 >= 0.8) {{
        r2Badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-blue-100 text-blue-700';
        r2Badge.textContent = '良好 (Good)';
      }} else if (r2 >= 0.5) {{
        r2Badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-100 text-amber-700';
        r2Badge.textContent = '偏弱 (Fair)';
      }} else {{
        r2Badge.className = 'text-[10px] font-bold px-2 py-0.5 rounded-full bg-rose-100 text-rose-700';
        r2Badge.textContent = '擬合不足 (Poor)';
      }}

      // Delta comparison against optimal
      const r2Diff = r2 - 0.9507;
      document.getElementById('metric-r2-diff').textContent = `Δ: ${{r2Diff >= 0 ? '+' : ''}}${{r2Diff.toFixed(4)}}`;

      document.getElementById('metric-rmse').textContent = '$' + Math.round(rmse).toLocaleString();
      document.getElementById('metric-mae').textContent = '$' + Math.round(mae).toLocaleString();
      document.getElementById('metric-mse').textContent = mse > 1e6 ? mse.toExponential(2) : Math.round(mse).toLocaleString();

      // RMSE progress bar (scaled relative to baseline standard deviation)
      const rmsePct = Math.max(5, Math.min(100, 100 - (rmse / 40000) * 100));
      document.getElementById('metric-rmse-progress').style.width = `${{rmsePct}}%`;

      // C. Update Sliders & Inputs sync
      syncControlValues();

      // D. Update Profit Simulator
      updateSimulator();

      // E. Update Visual Chart
      updateChartData(predictions);

      // F. Update Table
      updateTable(predictions);
    }}

    function syncControlValues() {{
      const w_rd_slider = document.getElementById('slider-w-rd');
      const w_rd_input = document.getElementById('input-w-rd');
      w_rd_slider.value = state.w_rd;
      w_rd_input.value = Number(state.w_rd.toFixed(4));

      const w_admin_slider = document.getElementById('slider-w-admin');
      const w_admin_input = document.getElementById('input-w-admin');
      w_admin_slider.value = state.w_admin;
      w_admin_input.value = Number(state.w_admin.toFixed(4));

      const w_mkt_slider = document.getElementById('slider-w-mkt');
      const w_mkt_input = document.getElementById('input-w-mkt');
      w_mkt_slider.value = state.w_mkt;
      w_mkt_input.value = Number(state.w_mkt.toFixed(4));

      const b_slider = document.getElementById('slider-b');
      const b_input = document.getElementById('input-b');
      b_slider.value = state.b;
      b_input.value = Number(state.b.toFixed(2));
    }}

    function updateSimulator() {{
      const simRd = parseFloat(document.getElementById('sim-rd').value);
      const simAdmin = parseFloat(document.getElementById('sim-admin').value);
      const simMkt = parseFloat(document.getElementById('sim-mkt').value);

      document.getElementById('sim-rd-val').textContent = '$' + simRd.toLocaleString();
      document.getElementById('sim-admin-val').textContent = '$' + simAdmin.toLocaleString();
      document.getElementById('sim-mkt-val').textContent = '$' + simMkt.toLocaleString();

      const profit = state.w_rd * simRd + state.w_admin * simAdmin + state.w_mkt * simMkt + state.b;
      document.getElementById('sim-result-profit').textContent = '$' + Math.round(profit).toLocaleString();

      const badge = document.getElementById('sim-vs-avg-badge');
      if (profit >= Y_MEAN) {{
        badge.className = 'inline-flex items-center gap-1 text-[11px] font-bold px-2 py-0.5 rounded-md bg-emerald-50 text-emerald-700 border border-emerald-200';
        badge.innerHTML = '<i class="fa-solid fa-arrow-trend-up"></i> 高於平均';
      }} else {{
        badge.className = 'inline-flex items-center gap-1 text-[11px] font-bold px-2 py-0.5 rounded-md bg-rose-50 text-rose-700 border border-rose-200';
        badge.innerHTML = '<i class="fa-solid fa-arrow-trend-down"></i> 低於平均';
      }}
    }}

    // 7. CHART RENDERING ACROSS 3 TABS
    function updateChartData(predictions) {{
      if (!chartInstance) return;

      const filtered = predictions.filter(p => {{
        if (state.stateFilter === 'All') return true;
        return p.item.State === state.stateFilter;
      }});

      if (state.chartTab === 'actual-vs-pred') {{
        // TAB 1: ACTUAL VS PREDICTED
        chartInstance.options.scales.x.title.text = '實際利潤 (Actual Profit $)';
        chartInstance.options.scales.y.title.text = '模型預測利潤 (Predicted Profit $)';
        chartInstance.options.scales.x.min = 0;
        chartInstance.options.scales.x.max = 210000;
        chartInstance.options.scales.y.min = undefined;
        chartInstance.options.scales.y.max = undefined;

        chartInstance.data.datasets[0].label = '完美預測對角線 (y = x)';
        chartInstance.data.datasets[0].data = [{{ x: 0, y: 0 }}, {{ x: 210000, y: 210000 }}];
        chartInstance.data.datasets[0].hidden = false;

        const points = [];
        const colors = [];

        filtered.forEach(p => {{
          points.push({{
            x: p.actual,
            y: p.predicted,
            meta: p.index
          }});
          if (p.pctError < 5) colors.push('rgba(16, 185, 129, 0.85)'); // emerald
          else if (p.pctError < 15) colors.push('rgba(245, 158, 11, 0.85)'); // amber
          else colors.push('rgba(244, 63, 94, 0.85)'); // rose
        }});

        chartInstance.data.datasets[1].label = '新創公司樣本 (色階代表誤差幅度)';
        chartInstance.data.datasets[1].data = points;
        chartInstance.data.datasets[1].backgroundColor = colors;
        chartInstance.data.datasets[1].pointRadius = 6;

        document.getElementById('chart-hint-text').innerHTML = `
          <span class="inline-block w-2 h-2 rounded-full bg-indigo-500"></span>
          <span><strong>完美預測對角線</strong>：虛線為 y = x。點越貼合虛線，代表模型對該新創預測越準確。</span>
        `;

      }} else if (state.chartTab === 'feature-scatter') {{
        // TAB 2: FEATURE PROJECTION
        const featKey = state.projectionFeature;
        let featName = 'R&D Spend';
        let featLabel = '研發支出 (R&D Spend $)';
        let slope = state.w_rd;

        if (featKey === 'admin') {{
          featName = 'Administration';
          featLabel = '管理支出 (Administration $)';
          slope = state.w_admin;
        }} else if (featKey === 'mkt') {{
          featName = 'Marketing Spend';
          featLabel = '行銷支出 (Marketing Spend $)';
          slope = state.w_mkt;
        }}

        chartInstance.options.scales.x.title.text = featLabel;
        chartInstance.options.scales.y.title.text = '新創利潤 (Profit $)';
        chartInstance.options.scales.x.min = 0;
        chartInstance.options.scales.x.max = featKey === 'mkt' ? 500000 : 200000;

        // Calculate mean of other 2 features
        const otherFeaturesMeanContribution = STARTUPS_DATA.reduce((sum, row) => {{
          let other = state.b;
          if (featKey !== 'rd') other += state.w_rd * row['R&D Spend'];
          if (featKey !== 'admin') other += state.w_admin * row['Administration'];
          if (featKey !== 'mkt') other += state.w_mkt * row['Marketing Spend'];
          return sum + other;
        }}, 0) / N_SAMPLES;

        const max_x = chartInstance.options.scales.x.max;
        const trendStart = otherFeaturesMeanContribution;
        const trendEnd = slope * max_x + otherFeaturesMeanContribution;

        chartInstance.data.datasets[0].label = `當前迴歸斜率線 (w = ${{slope.toFixed(4)}})`;
        chartInstance.data.datasets[0].data = [{{ x: 0, y: trendStart }}, {{ x: max_x, y: trendEnd }}];
        chartInstance.data.datasets[0].hidden = false;

        const points = [];
        const colors = [];

        filtered.forEach(p => {{
          points.push({{
            x: p.item[featName],
            y: p.actual,
            meta: p.index
          }});
          colors.push(featKey === 'rd' ? 'rgba(79, 70, 229, 0.85)' : (featKey === 'admin' ? 'rgba(245, 158, 11, 0.85)' : 'rgba(16, 185, 129, 0.85)'));
        }});

        chartInstance.data.datasets[1].label = `實際樣本分佈 (${{featName}})`;
        chartInstance.data.datasets[1].data = points;
        chartInstance.data.datasets[1].backgroundColor = colors;
        chartInstance.data.datasets[1].pointRadius = 6;

        document.getElementById('chart-hint-text').innerHTML = `
          <span class="inline-block w-2 h-2 rounded-full bg-indigo-500"></span>
          <span><strong>特徵邊際效應斜率</strong>：拖曳滑桿時，虛線斜率將實時旋轉，呈現該特徵對利潤的邊際貢獻。</span>
        `;

      }} else if (state.chartTab === 'residuals') {{
        // TAB 3: RESIDUALS VS PREDICTED
        chartInstance.options.scales.x.title.text = '模型預測利潤 (Predicted Profit $)';
        chartInstance.options.scales.y.title.text = '殘差 Residual (Actual - Predicted $)';
        chartInstance.options.scales.x.min = 0;
        chartInstance.options.scales.x.max = 210000;
        chartInstance.options.scales.y.min = -40000;
        chartInstance.options.scales.y.max = 40000;

        chartInstance.data.datasets[0].label = '零殘差基準線 (Residual = 0)';
        chartInstance.data.datasets[0].data = [{{ x: 0, y: 0 }}, {{ x: 210000, y: 0 }}];
        chartInstance.data.datasets[0].hidden = false;

        const points = [];
        const colors = [];

        filtered.forEach(p => {{
          points.push({{
            x: p.predicted,
            y: p.residual,
            meta: p.index
          }});
          colors.push(p.residual >= 0 ? 'rgba(59, 130, 246, 0.8)' : 'rgba(239, 68, 68, 0.8)');
        }});

        chartInstance.data.datasets[1].label = '各企業殘差 (藍色:低估, 紅色:高估)';
        chartInstance.data.datasets[1].data = points;
        chartInstance.data.datasets[1].backgroundColor = colors;
        chartInstance.data.datasets[1].pointRadius = 5.5;

        document.getElementById('chart-hint-text').innerHTML = `
          <span class="inline-block w-2 h-2 rounded-full bg-blue-500"></span>
          <span><strong>殘差隨機分佈檢驗</strong>：點隨機均勻散佈在 0 基準線兩側表示符合同方差性 (Homoscedasticity)。</span>
        `;
      }}

      chartInstance.update();
    }}

    // 8. TABLE POPULATION
    function updateTable(predictions) {{
      const tbody = document.getElementById('table-body');
      let rows = [...predictions];

      // Filter by search
      if (state.tableSearch.trim() !== '') {{
        const q = state.tableSearch.toLowerCase();
        rows = rows.filter(r => 
          r.item.State.toLowerCase().includes(q) ||
          (r.index + 1).toString().includes(q)
        );
      }}

      // Filter by state filter
      if (state.stateFilter !== 'All') {{
        rows = rows.filter(r => r.item.State === state.stateFilter);
      }}

      // Sort
      if (state.tableSort === 'id') {{
        rows.sort((a, b) => a.index - b.index);
      }} else if (state.tableSort === 'actual-desc') {{
        rows.sort((a, b) => b.actual - a.actual);
      }} else if (state.tableSort === 'error-desc') {{
        rows.sort((a, b) => b.absError - a.absError);
      }} else if (state.tableSort === 'rd-desc') {{
        rows.sort((a, b) => b.item['R&D Spend'] - a.item['R&D Spend']);
      }}

      document.getElementById('table-row-count').textContent = rows.length;

      tbody.innerHTML = rows.map(r => {{
        let badgeColor = 'bg-emerald-100 text-emerald-800';
        if (r.pctError >= 15) badgeColor = 'bg-rose-100 text-rose-800 font-bold';
        else if (r.pctError >= 5) badgeColor = 'bg-amber-100 text-amber-800';

        const isOutlier = r.pctError >= 18;

        return `
          <tr class="hover:bg-slate-50 transition ${{isOutlier ? 'bg-rose-50/40' : ''}}">
            <td class="py-2 px-3 font-semibold text-slate-500">
              #${{r.index + 1}}
              ${{isOutlier ? '<span class="ml-1 text-[9px] bg-rose-200 text-rose-800 px-1 py-0.5 rounded font-sans font-bold">異常</span>' : ''}}
            </td>
            <td class="py-2 px-3 font-sans font-medium text-slate-800">${{r.item.State}}</td>
            <td class="py-2 px-3 text-slate-600">$${{Math.round(r.item['R&D Spend']).toLocaleString()}}</td>
            <td class="py-2 px-3 text-slate-600">$${{Math.round(r.item['Administration']).toLocaleString()}}</td>
            <td class="py-2 px-3 text-slate-600">$${{Math.round(r.item['Marketing Spend']).toLocaleString()}}</td>
            <td class="py-2 px-3 text-right font-bold text-slate-900">$${{Math.round(r.actual).toLocaleString()}}</td>
            <td class="py-2 px-3 text-right font-semibold text-indigo-700">$${{Math.round(r.predicted).toLocaleString()}}</td>
            <td class="py-2 px-3 text-right ${{r.residual >= 0 ? 'text-blue-600' : 'text-rose-600'}} font-medium">
              ${{r.residual >= 0 ? '+' : ''}}${{Math.round(r.residual).toLocaleString()}}
            </td>
            <td class="py-2 px-3 text-center">
              <span class="inline-block px-1.5 py-0.5 rounded text-[10px] ${{badgeColor}}">
                ${{r.pctError.toFixed(1)}}%
              </span>
            </td>
          </tr>
        `;
      }}).join('');
    }}

    // 9. ANIMATED SMOOTH INTERPOLATION TO OPTIMAL
    let animationFrameId = null;
    function animateToWeights(targetW_rd, targetW_admin, targetW_mkt, targetB, duration = 800) {{
      if (animationFrameId) cancelAnimationFrame(animationFrameId);

      const startW_rd = state.w_rd;
      const startW_admin = state.w_admin;
      const startW_mkt = state.w_mkt;
      const startB = state.b;

      const startTime = performance.now();

      function step(now) {{
        const elapsed = now - startTime;
        const progress = Math.min(1, elapsed / duration);
        // easeOutCubic curve
        const ease = 1 - Math.pow(1 - progress, 3);

        state.w_rd = startW_rd + (targetW_rd - startW_rd) * ease;
        state.w_admin = startW_admin + (targetW_admin - startW_admin) * ease;
        state.w_mkt = startW_mkt + (targetW_mkt - startW_mkt) * ease;
        state.b = startB + (targetB - startB) * ease;

        updateUI();

        if (progress < 1) {{
          animationFrameId = requestAnimationFrame(step);
        }} else {{
          // Check if confetti should trigger
          if (typeof confetti === 'function' && targetW_rd === GLOBAL_OPTIMAL.w_rd) {{
            confetti({{
              particleCount: 80,
              spread: 60,
              origin: {{ y: 0.7 }}
            }});
          }}
        }}
      }}

      animationFrameId = requestAnimationFrame(step);
    }}

    // 10. ATTACH EVENT LISTENERS
    document.addEventListener('DOMContentLoaded', () => {{
      initChart();
      updateUI();

      // Sliders & Number inputs sync
      const controls = [
        {{ key: 'w_rd', slider: 'slider-w-rd', input: 'input-w-rd' }},
        {{ key: 'w_admin', slider: 'slider-w-admin', input: 'input-w-admin' }},
        {{ key: 'w_mkt', slider: 'slider-w-mkt', input: 'input-w-mkt' }},
        {{ key: 'b', slider: 'slider-b', input: 'input-b' }}
      ];

      controls.forEach(c => {{
        const slider = document.getElementById(c.slider);
        const input = document.getElementById(c.input);

        slider.addEventListener('input', (e) => {{
          state[c.key] = parseFloat(e.target.value);
          updateUI();
        }});

        input.addEventListener('change', (e) => {{
          let val = parseFloat(e.target.value);
          if (isNaN(val)) val = 0;
          state[c.key] = val;
          updateUI();
        }});
      }});

      // Simulator inputs
      ['sim-rd', 'sim-admin', 'sim-mkt'].forEach(id => {{
        document.getElementById(id).addEventListener('input', updateSimulator);
      }});

      // Optimal button (Top & Quick)
      function triggerOptimal(animate = true) {{
        let optimal;
        if (state.activePreset === '2feat') {{
          optimal = solveOLS(['rd', 'mkt']);
        }} else if (state.activePreset === 'rd-only') {{
          optimal = solveOLS(['rd']);
        }} else {{
          optimal = GLOBAL_OPTIMAL;
        }}

        if (animate) {{
          animateToWeights(optimal.w_rd, optimal.w_admin, optimal.w_mkt, optimal.b, 750);
        }} else {{
          state.w_rd = optimal.w_rd;
          state.w_admin = optimal.w_admin;
          state.w_mkt = optimal.w_mkt;
          state.b = optimal.b;
          updateUI();
        }}
      }}

      document.getElementById('btn-apply-optimal').addEventListener('click', () => triggerOptimal(true));
      document.getElementById('btn-quick-optimal').addEventListener('click', () => triggerOptimal(true));

      // Reset button
      document.getElementById('btn-reset').addEventListener('click', () => {{
        animateToWeights(GLOBAL_OPTIMAL.w_rd, GLOBAL_OPTIMAL.w_admin, GLOBAL_OPTIMAL.w_mkt, GLOBAL_OPTIMAL.b, 500);
      }});

      // Animation Fit (starts from 0 or perturbed and converges)
      document.getElementById('btn-animate-fit').addEventListener('click', () => {{
        state.w_rd = 0.2;
        state.w_admin = 0.4;
        state.w_mkt = -0.1;
        state.b = 10000;
        updateUI();
        setTimeout(() => {{
          triggerOptimal(true);
        }}, 300);
      }});

      // Preset buttons
      const presetBtns = {{
        'preset-all': 'all',
        'preset-2feat': '2feat',
        'preset-rd-only': 'rd-only',
        'preset-zero': 'zero'
      }};

      Object.entries(presetBtns).forEach(([btnId, presetKey]) => {{
        document.getElementById(btnId).addEventListener('click', () => {{
          document.querySelectorAll('.preset-btn').forEach(b => {{
            b.className = 'preset-btn py-2 px-2.5 rounded-lg border text-left font-medium transition flex flex-col justify-between border-slate-200 bg-white text-slate-700 hover:border-slate-300';
            b.querySelector('.rounded-full').className = 'w-2 h-2 rounded-full bg-slate-300';
          }});

          const activeBtn = document.getElementById(btnId);
          activeBtn.className = 'preset-btn active py-2 px-2.5 rounded-lg border text-left font-medium transition flex flex-col justify-between border-indigo-600 bg-indigo-50 text-indigo-900 shadow-sm';
          activeBtn.querySelector('.rounded-full').className = 'w-2 h-2 rounded-full bg-indigo-600';

          state.activePreset = presetKey;

          if (presetKey === 'all') {{
            const opt = solveOLS(['rd', 'admin', 'mkt']);
            animateToWeights(opt.w_rd, opt.w_admin, opt.w_mkt, opt.b, 600);
          }} else if (presetKey === '2feat') {{
            const opt = solveOLS(['rd', 'mkt']);
            animateToWeights(opt.w_rd, 0, opt.w_mkt, opt.b, 600);
          }} else if (presetKey === 'rd-only') {{
            const opt = solveOLS(['rd']);
            animateToWeights(opt.w_rd, 0, 0, opt.b, 600);
          }} else if (presetKey === 'zero') {{
            animateToWeights(0, 0, 0, 0, 500);
          }}
        }});
      }});

      // Snap individual parameter to optimal
      document.querySelectorAll('.snap-btn').forEach(btn => {{
        btn.addEventListener('click', (e) => {{
          const target = e.target.getAttribute('data-target');
          if (target && GLOBAL_OPTIMAL[target] !== undefined) {{
            state[target] = GLOBAL_OPTIMAL[target];
            updateUI();
          }}
        }});
      }});

      // Nudge buttons
      document.getElementById('btn-nudge-up').addEventListener('click', () => {{
        state.w_rd *= 1.02;
        state.w_admin *= 1.02;
        state.w_mkt *= 1.02;
        state.b *= 1.02;
        updateUI();
      }});
      document.getElementById('btn-nudge-down').addEventListener('click', () => {{
        state.w_rd *= 0.98;
        state.w_admin *= 0.98;
        state.w_mkt *= 0.98;
        state.b *= 0.98;
        updateUI();
      }});
      document.getElementById('btn-randomize').addEventListener('click', () => {{
        state.w_rd = parseFloat((Math.random() * 1.5).toFixed(3));
        state.w_admin = parseFloat(((Math.random() - 0.5) * 0.4).toFixed(3));
        state.w_mkt = parseFloat((Math.random() * 0.2).toFixed(3));
        state.b = Math.round(Math.random() * 80000);
        updateUI();
      }});

      // Chart Tabs
      const tabs = [
        {{ id: 'tab-actual-vs-pred', key: 'actual-vs-pred' }},
        {{ id: 'tab-feature-scatter', key: 'feature-scatter' }},
        {{ id: 'tab-residuals', key: 'residuals' }}
      ];

      tabs.forEach(t => {{
        document.getElementById(t.id).addEventListener('click', () => {{
          tabs.forEach(item => {{
            const el = document.getElementById(item.id);
            el.className = 'chart-tab px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 transition';
          }});
          document.getElementById(t.id).className = 'chart-tab px-3 py-1.5 rounded-lg bg-white text-indigo-700 shadow-sm transition';
          
          state.chartTab = t.key;
          const featWrapper = document.getElementById('feature-select-wrapper');
          if (t.key === 'feature-scatter') {{
            featWrapper.classList.remove('hidden');
          }} else {{
            featWrapper.classList.add('hidden');
          }}

          const {{ predictions }} = computePredictions();
          updateChartData(predictions);
        }});
      }});

      // Feature projection select
      document.getElementById('select-feature-projection').addEventListener('change', (e) => {{
        state.projectionFeature = e.target.value;
        const {{ predictions }} = computePredictions();
        updateChartData(predictions);
      }});

      // State Filter select
      document.getElementById('select-state-filter').addEventListener('change', (e) => {{
        state.stateFilter = e.target.value;
        const {{ predictions }} = computePredictions();
        updateChartData(predictions);
        updateTable(predictions);
      }});

      // Table Search & Sort
      document.getElementById('table-search').addEventListener('input', (e) => {{
        state.tableSearch = e.target.value;
        const {{ predictions }} = computePredictions();
        updateTable(predictions);
      }});

      document.getElementById('table-sort').addEventListener('change', (e) => {{
        state.tableSort = e.target.value;
        const {{ predictions }} = computePredictions();
        updateTable(predictions);
      }});

      // Export CSV
      document.getElementById('btn-export-csv').addEventListener('click', () => {{
        const {{ predictions }} = computePredictions();
        let csv = 'Startup_ID,State,R&D_Spend,Administration,Marketing_Spend,Actual_Profit,Predicted_Profit,Residual,Absolute_Error_Pct\\n';
        predictions.forEach(p => {{
          csv += `${{p.index + 1}},"${{p.item.State}}",${{p.item['R&D Spend']}},${{p.item.Administration}},${{p.item['Marketing Spend']}},${{p.actual}},${{p.predicted.toFixed(2)}},${{p.residual.toFixed(2)}},${{p.pctError.toFixed(2)}}%\\n`;
        }});

        const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `50_startups_regression_predictions_${{Date.now()}}.csv`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
      }});

      // Theory Modal
      const modal = document.getElementById('theory-modal');
      document.getElementById('btn-theory-modal').addEventListener('click', () => modal.classList.remove('hidden'));
      document.getElementById('btn-close-modal').addEventListener('click', () => modal.classList.add('hidden'));
      document.getElementById('btn-modal-ok').addEventListener('click', () => modal.classList.add('hidden'));
      modal.addEventListener('click', (e) => {{
        if (e.target === modal) modal.classList.add('hidden');
      }});
    }});
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully! Size:", len(html_content), "bytes")
