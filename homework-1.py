<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>金門機場每週航班統計 (2026/10/12 - 10/18)</title>
  <style>
    :root {
      --primary: #1e3a8a;
      --primary-light: #3b82f6;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --text: #1e293b;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --danger: #ef4444;
      --success: #10b981;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background: var(--bg); color: var(--text); line-height: 1.5; padding: 20px; max-width: 1200px; margin: 0 auto; }

    header { margin-bottom: 24px; text-align: center; }
    header h1 { font-size: 1.8rem; color: var(--primary); margin-bottom: 8px; }
    header p { color: var(--text-muted); font-size: 0.95rem; }

    .stats-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 24px; }
    .card { background: var(--card-bg); padding: 20px; border-radius: 8px; border: 1px solid var(--border); box-shadow: 0 1px 3px rgba(0,0,0,0.05); text-align: center; }
    .card .title { font-size: 0.9rem; color: var(--text-muted); margin-bottom: 4px; }
    .card .value { font-size: 2rem; font-weight: bold; color: var(--primary); }

    .chart-section { background: var(--card-bg); padding: 20px; border-radius: 8px; border: 1px solid var(--border); margin-bottom: 24px; overflow-x: auto; }
    .chart-section h2 { font-size: 1.2rem; margin-bottom: 16px; color: var(--primary); }
    .bar-chart { display: flex; justify-content: space-between; align-items: flex-end; height: 180px; padding-top: 20px; border-bottom: 2px solid var(--border); min-width: 500px; }
    .chart-column { display: flex; flex-direction: column; align-items: center; flex: 1; cursor: pointer; height: 100%; justify-content: flex-end; padding: 0 4px; }
    .chart-column:hover .bar-group { opacity: 0.8; }
    .bar-group { display: flex; gap: 4px; align-items: flex-end; width: 100%; max-width: 40px; }
    .bar { flex: 1; background: var(--primary-light); border-radius: 4px 4px 0 0; transition: height 0.3s; position: relative; }
    .bar.dep { background: #06b6d4; }
    .bar-label { margin-top: 8px; font-size: 0.85rem; color: var(--text-muted); text-align: center; }
    .bar-val { position: absolute; top: -18px; left: 50%; transform: translateX(-50%); font-size: 0.7rem; color: var(--text-muted); }

    .filter-section { background: var(--card-bg); padding: 20px; border-radius: 8px; border: 1px solid var(--border); margin-bottom: 24px; }
    .filter-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin-bottom: 16px; }
    .filter-group { display: flex; flex-direction: column; gap: 4px; }
    .filter-group label { font-size: 0.85rem; font-weight: 600; color: var(--text-muted); }
    .filter-group select, .filter-group input { padding: 8px 12px; border: 1px solid var(--border); border-radius: 4px; font-size: 0.9rem; }

    .actions { display: flex; gap: 12px; flex-wrap: wrap; }
    .btn { padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer; font-size: 0.9rem; font-weight: 500; transition: background 0.2s; }
    .btn-primary { background: var(--primary-light); color: white; }
    .btn-primary:hover { background: #2563eb; }
    .btn-secondary { background: #e2e8f0; color: var(--text); }
    .btn-secondary:hover { background: #cbd5e1; }

    .table-section { background: var(--card-bg); border-radius: 8px; border: 1px solid var(--border); overflow: hidden; margin-bottom: 24px; }
    .table-container { overflow-x: auto; }
    table { width: 100%; border-collapse: collapse; text-align: left; font-size: 0.9rem; }
    th, td { padding: 12px 16px; border-bottom: 1px solid var(--border); }
    th { background: #f1f5f9; color: var(--text-muted); font-weight: 600; }
    tr:hover { background: #f8fafc; }
    .badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.8rem; font-weight: 500; }
    .badge-arr { background: #dbeafe; color: #1e40af; }
    .badge-dep { background: #cff4fc; color: #055160; }
    .status-cancelled { text-decoration: line-through; color: var(--danger); }
    .badge-cancel { background: #fee2e2; color: #991b1b; }
    .badge-normal { background: #d1fae5; color: #065f46; }

    .spec-section { background: var(--card-bg); padding: 20px; border-radius: 8px; border: 1px solid var(--border); font-size: 0.85rem; color: var(--text-muted); }
    .spec-section h3 { color: var(--text); margin-bottom: 8px; }
    .spec-section ul { padding-left: 20px; }

    .no-result { padding: 30px; text-align: center; color: var(--text-muted); }
  </style>
</head>
<body>

  <header>
    <h1>金門機場每週航班統計</h1>
    <p>統計期間：2026 年 10 月 12 日至 10 月 18 日 (依官方預定月班表整理)</p>
  </header>

  <!-- 統計卡片 -->
  <div class="stats-grid">
    <div class="card">
      <div class="title">進場班次 (抵達)</div>
      <div class="value" id="stat-arr">0</div>
    </div>
    <div class="card">
      <div class="title">離場班次 (出發)</div>
      <div class="value" id="stat-dep">0</div>
    </div>
    <div class="card">
      <div class="title">總班次</div>
      <div class="value" id="stat-total">0</div>
    </div>
  </div>

  <!-- 每日長條圖 -->
  <div class="chart-section">
    <h2>每日進出班次分布 (點選日期可快速篩選)</h2>
    <div class="bar-chart" id="chart-container"></div>
  </div>

  <!-- 組合篩選器 -->
  <div class="filter-section">
    <div class="filter-grid">
      <div class="filter-group">
        <label for="filter-date">日期</label>
        <select id="filter-date">
          <option value="">全部 (10/12 - 10/18)</option>
          <option value="2026-10-12">2026/10/12 (一)</option>
          <option value="2026-10-13">2026/10/13 (二)</option>
          <option value="2026-10-14">2026/10/14 (三)</option>
          <option value="2026-10-15">2026/10/15 (四)</option>
          <option value="2026-10-16">2026/10/16 (五)</option>
          <option value="2026-10-17">2026/10/17 (六)</option>
          <option value="2026-10-18">2026/10/18 (日)</option>
        </select>
      </div>

      <div class="filter-group">
        <label for="filter-airline">航空公司</label>
        <select id="filter-airline">
          <option value="">全部</option>
          <option value="立榮航空">立榮航空</option>
          <option value="華信航空">華信航空</option>
        </select>
      </div>

      <div class="filter-group">
        <label for="filter-airport">對端機場</label>
        <select id="filter-airport">
          <option value="">全部</option>
          <option value="臺北">臺北</option>
          <option value="台中">台中</option>
          <option value="嘉義">嘉義</option>
          <option value="臺南">臺南</option>
          <option value="高雄">高雄</option>
          <option value="澎湖">澎湖</option>
        </select>
      </div>

      <div class="filter-group">
        <label for="filter-dir">方向</label>
        <select id="filter-dir">
          <option value="">全部</option>
          <option value="進場">進場</option>
          <option value="離場">離場</option>
        </select>
      </div>

      <div class="filter-group">
        <label for="filter-search">航班搜尋</label>
        <input type="text" id="filter-search" placeholder="例如：B7-8921">
      </div>
    </div>

    <div class="actions">
      <button class="btn btn-primary" onclick="exportCSV()">匯出篩選結果 CSV</button>
      <button class="btn btn-secondary" onclick="resetFilters()">重設篩選</button>
    </div>
  </div>

  <!-- 航班明細表格 -->
  <div class="table-section">
    <div class="table-container">
      <table>
        <thead>
          <tr>
            <th>日期</th>
            <th>航班編號</th>
            <th>航空公司</th>
            <th>方向</th>
            <th>航線</th>
            <th>班表狀態</th>
          </tr>
        </thead>
        <tbody id="flight-table-body"></tbody>
      </table>
      <div id="no-data" class="no-result" style="display: none;">無符合條件的航班紀錄</div>
    </div>
  </div>

  <!-- 作業規格與備註 -->
  <div class="spec-section">
    <h3>專案說明與驗收項目</h3>
    <ul>
      <li><strong>資料來源：</strong>金門航空站 2026 年 10 月份班機時刻表 (統計區間：2026/10/12 - 2026/10/18)。</li>
      <li><strong>預設統計：</strong>全週正常航班合計 686 班（進場 342 班、離場 344 班）。</li>
      <li><strong>取消說明：</strong>10/15 的 B7-8921 與 B7-8922 明列取消，保留於明細列表中但<b>不納入</b>統計數值與圖表。</li>
      <li><strong>澎湖航線：</strong>10/17 納入 B7-8995（進場）、B7-8996（離場）。</li>
    </ul>
  </div>

  <script>
    // 生成基底資料庫
    const rawRoutes = [
      // 臺北
      { airline: '立榮航空', arrNo: 'B7-8801', depNo: 'B7-8802', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8805', depNo: 'B7-8806', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8811', depNo: 'B7-8812', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8815', depNo: 'B7-8816', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8821', depNo: 'B7-8822', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8825', depNo: 'B7-8826', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8829', depNo: 'B7-8830', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8835', depNo: 'B7-8836', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-1261', depNo: 'AE-1262', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-1265', depNo: 'AE-1266', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-1269', depNo: 'AE-1270', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-1273', depNo: 'AE-1274', apt: '臺北', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-1277', depNo: 'AE-1278', apt: '臺北', days: [1,2,3,4,5,6,7] },

      // 台中
      { airline: '立榮航空', arrNo: 'B7-8951', depNo: 'B7-8952', apt: '台中', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8955', depNo: 'B7-8956', apt: '台中', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8961', depNo: 'B7-8962', apt: '台中', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8965', depNo: 'B7-8966', apt: '台中', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-0761', depNo: 'AE-0762', apt: '台中', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-0765', depNo: 'AE-0766', apt: '台中', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-0769', depNo: 'AE-0770', apt: '台中', days: [1,2,3,4,5,6,7] },

      // 嘉義
      { airline: '立榮航空', arrNo: 'B7-8901', depNo: 'B7-8902', apt: '嘉義', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8905', depNo: 'B7-8906', apt: '嘉義', days: [1,2,3,4,5,6,7] },

      // 臺南
      { airline: '立榮航空', arrNo: 'B7-8981', depNo: 'B7-8982', apt: '臺南', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8985', depNo: 'B7-8986', apt: '臺南', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8989', depNo: 'B7-8990', apt: '臺南', days: [1,2,3,4,5,6,7] },

      // 高雄
      { airline: '立榮航空', arrNo: 'B7-8911', depNo: 'B7-8912', apt: '高雄', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8915', depNo: 'B7-8916', apt: '高雄', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8921', depNo: 'B7-8922', apt: '高雄', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8925', depNo: 'B7-8926', apt: '高雄', days: [1,2,3,4,5,6,7] },
      { airline: '立榮航空', arrNo: 'B7-8933', depNo: 'B7-8934', apt: '高雄', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-3071', depNo: 'AE-3072', apt: '高雄', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-3075', depNo: 'AE-3076', apt: '高雄', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-3079', depNo: 'AE-3080', apt: '高雄', days: [1,2,3,4,5,6,7] },
      { airline: '華信航空', arrNo: 'AE-3091', depNo: 'AE-3092', apt: '高雄', days: [1,2,3,4,5,6,7] }
    ];

    const weekDates = [
      { date: '2026-10-12', dayNum: 1, label: '10/12 (一)' },
      { date: '2026-10-13', dayNum: 2, label: '10/13 (二)' },
      { date: '2026-10-14', dayNum: 3, label: '10/14 (三)' },
      { date: '2026-10-15', dayNum: 4, label: '10/15 (四)' },
      { date: '2026-10-16', dayNum: 5, label: '10/16 (五)' },
      { date: '2026-10-17', dayNum: 6, label: '10/17 (六)' },
      { date: '2026-10-18', dayNum: 7, label: '10/18 (日)' }
    ];

    // 展開所有航班紀錄
    let allFlights = [];

    weekDates.forEach(d => {
      // 基準路線
      rawRoutes.forEach(r => {
        if (r.days.includes(d.dayNum)) {
          // 進場
          allFlights.push({
            date: d.date,
            flightNo: r.arrNo,
            airline: r.airline,
            dir: '進場',
            route: `${r.apt} -> 金門`,
            apt: r.apt,
            status: (d.date === '2026-10-15' && r.arrNo === 'B7-8921') ? '取消' : '正常'
          });
          // 離場
          allFlights.push({
            date: d.date,
            flightNo: r.depNo,
            airline: r.airline,
            dir: '離場',
            route: `金門 -> ${r.apt}`,
            apt: r.apt,
            status: (d.date === '2026-10-15' && r.depNo === 'B7-8922') ? '取消' : '正常'
          });
        }
      });

      // 獨立/非不對稱與特別調整
      // 1. B7-9206 每日進場
      allFlights.push({ date: d.date, flightNo: 'B7-9206', airline: '立榮航空', dir: '進場', route: '臺北 -> 金門', apt: '臺北', status: '正常' });
      
      // 2. B7-9208 週一四五日離場
      if ([1, 4, 5, 7].includes(d.dayNum)) {
        allFlights.push({ date: d.date, flightNo: 'B7-9208', airline: '立榮航空', dir: '離場', route: '金門 -> 臺北', apt: '臺北', status: '正常' });
      }

      // 3. 10/16 (五) 離場加一班
      if (d.date === '2026-10-16') {
        allFlights.push({ date: d.date, flightNo: 'B7-8832', airline: '立榮航空', dir: '離場', route: '金門 -> 臺北', apt: '臺北', status: '正常' });
      }

      // 4. 10/17 (六) 澎湖航線
      if (d.date === '2026-10-17') {
        allFlights.push({ date: d.date, flightNo: 'B7-8995', airline: '立榮航空', dir: '進場', route: '澎湖 -> 金門', apt: '澎湖', status: '正常' });
        allFlights.push({ date: d.date, flightNo: 'B7-8996', airline: '立榮航空', dir: '離場', route: '金門 -> 澎湖', apt: '澎湖', status: '正常' });
      }
    });

    // 監聽 DOM 與篩選控制
    document.addEventListener('DOMContentLoaded', () => {
      ['filter-date', 'filter-airline', 'filter-airport', 'filter-dir'].forEach(id => {
        document.getElementById(id).addEventListener('change', updateApp);
      });
      document.getElementById('filter-search').addEventListener('input', updateApp);

      updateApp();
    });

    function getFilteredData() {
      const dateVal = document.getElementById('filter-date').value;
      const airlineVal = document.getElementById('filter-airline').value;
      const aptVal = document.getElementById('filter-airport').value;
      const dirVal = document.getElementById('filter-dir').value;
      const searchVal = document.getElementById('filter-search').value.trim().toUpperCase();

      return allFlights.filter(f => {
        if (dateVal && f.date !== dateVal) return false;
        if (airlineVal && f.airline !== airlineVal) return false;
        if (aptVal && f.apt !== aptVal) return false;
        if (dirVal && f.dir !== dirVal) return false;
        if (searchVal && !f.flightNo.toUpperCase().includes(searchVal)) return false;
        return true;
      });
    }

    function updateApp() {
      const filtered = getFilteredData();

      // 計算非取消的有效統計數
      const validFlights = filtered.filter(f => f.status !== '取消');
      const arrCount = validFlights.filter(f => f.dir === '進場').length;
      const depCount = validFlights.filter(f => f.dir === '離場').length;

      document.getElementById('stat-arr').textContent = arrCount;
      document.getElementById('stat-dep').textContent = depCount;
      document.getElementById('stat-total').textContent = arrCount + depCount;

      renderChart();
      renderTable(filtered);
    }

    function renderChart() {
      const container = document.getElementById('chart-container');
      container.innerHTML = '';

      const airlineVal = document.getElementById('filter-airline').value;
      const aptVal = document.getElementById('filter-airport').value;
      const dirVal = document.getElementById('filter-dir').value;
      const searchVal = document.getElementById('filter-search').value.trim().toUpperCase();

      weekDates.forEach(d => {
        // 計算該日特定條件下的統計量 (排除取消)
        const dayValidFlights = allFlights.filter(f => {
          if (f.date !== d.date) return false;
          if (f.status === '取消') return false;
          if (airlineVal && f.airline !== airlineVal) return false;
          if (aptVal && f.apt !== aptVal) return false;
          if (dirVal && f.dir !== dirVal) return false;
          if (searchVal && !f.flightNo.toUpperCase().includes(searchVal)) return false;
          return true;
        });

        const arr = dayValidFlights.filter(f => f.dir === '進場').length;
        const dep = dayValidFlights.filter(f => f.dir === '離場').length;

        const maxVal = 55; // 用於計算長條圖比例高度
        const arrHeight = Math.round((arr / maxVal) * 100);
        const depHeight = Math.round((dep / maxVal) * 100);

        const col = document.createElement('div');
        col.className = 'chart-column';
        col.onclick = () => {
          document.getElementById('filter-date').value = d.date;
          updateApp();
        };

        col.innerHTML = `
          <div class="bar-group">
            ${dirVal !== '離場' ? `<div class="bar" style="height: ${arrHeight}%"><span class="bar-val">${arr}</span></div>` : ''}
            ${dirVal !== '進場' ? `<div class="bar dep" style="height: ${depHeight}%"><span class="bar-val">${dep}</span></div>` : ''}
          </div>
          <div class="bar-label">${d.label}</div>
        `;
        container.appendChild(col);
      });
    }

    function renderTable(data) {
      const tbody = document.getElementById('flight-table-body');
      const noData = document.getElementById('no-data');
      tbody.innerHTML = '';

      if (data.length === 0) {
        noData.style.display = 'block';
        return;
      }
      noData.style.display = 'none';

      data.forEach(f => {
        const tr = document.createElement('tr');
        const isCancelled = f.status === '取消';

        tr.innerHTML = `
          <td>${f.date}</td>
          <td class="${isCancelled ? 'status-cancelled' : ''}">${f.flightNo}</td>
          <td>${f.airline}</td>
          <td><span class="badge ${f.dir === '進場' ? 'badge-arr' : 'badge-dep'}">${f.dir}</span></td>
          <td>${f.route}</td>
          <td><span class="badge ${isCancelled ? 'badge-cancel' : 'badge-normal'}">${f.status}</span></td>
        `;
        tbody.appendChild(tr);
      });
    }

    function resetFilters() {
      document.getElementById('filter-date').value = '';
      document.getElementById('filter-airline').value = '';
      document.getElementById('filter-airport').value = '';
      document.getElementById('filter-dir').value = '';
      document.getElementById('filter-search').value = '';
      updateApp();
    }

    function exportCSV() {
      const filtered = getFilteredData();
      if (filtered.length === 0) {
        alert('目前無符合條件的航班可供匯出！');
        return;
      }

      let csvContent = '\uFEFF'; // BOM 防止中文亂碼
      csvContent += '日期,航班編號,航空公司,方向,航線,狀態\n';

      filtered.forEach(f => {
        csvContent += `"${f.date}","${f.flightNo}","${f.airline}","${f.dir}","${f.route}","${f.status}"\n`;
      });

      const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', `金門航班統計篩選結果_${new Date().toISOString().slice(0,10)}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  </script>
</body>
</html>
