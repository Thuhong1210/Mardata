# ⚡ QUICK START - BẮT ĐẦU TRONG 5 PHÚT

---

## 🎯 3 BƯỚC BẮT ĐẦU

### Bước 1: Đọc file này (2 phút)
### Bước 2: Mở notebook (1 phút)  
### Bước 3: Chạy code (30 phút)

---

## 🔥 3 TASK ƯU TIÊN CAO NHẤT

### 1️⃣ DATA CLEANING (30 phút)

**Copy code này vào notebook ngay sau phần đọc dữ liệu:**

```python
# ============================================================
# DATA CLEANING - Loại bỏ dữ liệu không hợp lệ
# ============================================================

# Các cột Likert
likert_cols = [
    'int1','int2','inf1','inf2','inf3','ve1','ve2','ve3','nvse1','nvse2',
    'trust1','trust2','trust3','conv1','conv2','conv3','conv4',
    'enj1','enj2','enj3','sc1','sc2','al1','al2','al3'
]

# Function kiểm tra
def check_invalid(row):
    vals = row[likert_cols].values
    # Tất cả giống nhau
    if len(set(vals)) == 1:
        return True
    # 10 liên tiếp giống nhau
    max_consecutive = 1
    current = 1
    for i in range(1, len(vals)):
        if vals[i] == vals[i-1]:
            current += 1
            max_consecutive = max(max_consecutive, current)
        else:
            current = 1
    return max_consecutive >= 10

# Loại bỏ
invalid = [i for i, row in df.iterrows() if check_invalid(row)]
print(f"Loại bỏ: {len(invalid)} mẫu")
df = df.drop(invalid).reset_index(drop=True)
print(f"Còn lại: {len(df)} mẫu")
```

---

### 2️⃣ FACTOR ANALYSIS (1 giờ)

**Cài thư viện:**
```bash
!pip install factor-analyzer
```

**Code:**
```python
from factor_analyzer import FactorAnalyzer
from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity

# KMO Test
kmo_all, kmo_model = calculate_kmo(df[likert_vars])
print(f"KMO: {kmo_model:.3f}")

# Factor Analysis
fa = FactorAnalyzer(n_factors=5, rotation='varimax')
fa.fit(df[likert_vars])
loadings = pd.DataFrame(fa.loadings_, index=likert_vars)
print(loadings.round(3))
```

---

### 3️⃣ REGRESSION (30 phút)

```python
import statsmodels.api as sm

# Tạo biến AL
df['AL'] = df[['al1','al2','al3']].mean(axis=1)

# Regression 1: Platform → AL
X1 = sm.add_constant(df[['INT','INF','VE','NVSE']])
model1 = sm.OLS(df['AL'], X1).fit()
print("R² =", model1.rsquared)

# Regression 2: Psychology → AL
X2 = sm.add_constant(df[['TRUST','CONV','ENJ','SC']])
model2 = sm.OLS(df['AL'], X2).fit()
print("R² =", model2.rsquared)
```

---

## ✅ CHECKLIST HÔM NAY

- [ ] Chạy Data Cleaning
- [ ] Chạy Factor Analysis  
- [ ] Chạy Regression
- [ ] Ghi lại kết quả

---

## 📚 ĐỌC TIẾP

- **ACTION_CHECKLIST.md** - Code chi tiết hơn
- **PROJECT_STATUS_REPORT.md** - Roadmap 3 tuần

---

**🚀 BẮT ĐẦU NGAY!**
