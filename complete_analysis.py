#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PHÂN TÍCH HOÀN CHỈNH - MDA2025
Các yếu tố quyết định lòng trung thành của người tiêu dùng trên TMĐT

Bao gồm:
1. Data Cleaning
2. Factor Analysis
3. Regression Analysis

Author: Antigravity AI Assistant
Date: 9/12/2025
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

print("="*80)
print("PHÂN TÍCH MARKETING - MDA2025")
print("Bắt đầu phân tích...")
print("="*80)

# ============================================================
# 1. ĐỌC DỮ LIỆU
# ============================================================

print("\n📂 BƯỚC 1: ĐỌC DỮ LIỆU")
print("-"*80)

try:
    df = pd.read_csv("onlinebuy.csv")
    print(f"✅ Đọc dữ liệu thành công!")
    print(f"   Kích thước: {df.shape} (rows, columns)")
except FileNotFoundError:
    print("❌ LỖI: Không tìm thấy file 'onlinebuy.csv'")
    print("   Vui lòng đảm bảo file CSV nằm cùng thư mục với script này.")
    exit(1)

# Danh sách các cột Likert
likert_cols = [
    'int1','int2','inf1','inf2','inf3','ve1','ve2','ve3','nvse1','nvse2',
    'trust1','trust2','trust3','conv1','conv2','conv3','conv4',
    'enj1','enj2','enj3','sc1','sc2','al1','al2','al3'
]

# ============================================================
# 2. DATA CLEANING - LOẠI BỎ DỮ LIỆU KHÔNG HỢP LỆ
# ============================================================

print("\n🧹 BƯỚC 2: DATA CLEANING")
print("-"*80)

def check_invalid_responses(row, cols):
    """
    Kiểm tra xem một row có dữ liệu không hợp lệ không
    
    Tiêu chí không hợp lệ:
    1. Tất cả giá trị giống nhau
    2. Có ≥10 giá trị liên tiếp giống nhau
    
    Returns:
        tuple: (is_invalid: bool, reason: str)
    """
    values = row[cols].values
    
    # Tiêu chí 1: Tất cả giống nhau
    if len(set(values)) == 1:
        return True, "all_same"
    
    # Tiêu chí 2: 10 giá trị liên tiếp giống nhau
    max_consecutive = 1
    current_consecutive = 1
    
    for i in range(1, len(values)):
        if values[i] == values[i-1]:
            current_consecutive += 1
            max_consecutive = max(max_consecutive, current_consecutive)
        else:
            current_consecutive = 1
    
    if max_consecutive >= 10:
        return True, f"consecutive_{max_consecutive}"
    
    return False, "valid"

# Tìm rows không hợp lệ
print("🔍 Kiểm tra dữ liệu không hợp lệ...")
invalid_rows = []
invalid_reasons = []

for idx, row in df.iterrows():
    is_invalid, reason = check_invalid_responses(row, likert_cols)
    if is_invalid:
        invalid_rows.append(idx)
        invalid_reasons.append(reason)

# Báo cáo kết quả
print(f"\n📊 KẾT QUẢ KIỂM TRA:")
print(f"   Tổng số mẫu: {len(df)}")
print(f"   Số mẫu không hợp lệ: {len(invalid_rows)} ({len(invalid_rows)/len(df)*100:.1f}%)")

if len(invalid_rows) > 0:
    # Thống kê theo loại lỗi
    reason_counts = Counter(invalid_reasons)
    
    print(f"\n   Phân loại lỗi:")
    for reason, count in reason_counts.items():
        print(f"     - {reason}: {count} mẫu")
    
    # Hiển thị ví dụ
    print(f"\n   🔍 5 ví dụ đầu tiên:")
    for i, (idx, reason) in enumerate(zip(invalid_rows[:5], invalid_reasons[:5])):
        print(f"     Row {idx}: {reason}")

# Loại bỏ
df_clean = df.drop(invalid_rows).reset_index(drop=True)

print(f"\n✅ KẾT QUẢ SAU KHI LÀM SẠCH:")
print(f"   Đã loại bỏ: {len(invalid_rows)} mẫu")
print(f"   Còn lại: {len(df_clean)} mẫu ({len(df_clean)/len(df)*100:.1f}%)")

# Lưu dữ liệu sạch
df_clean.to_csv("onlinebuy_cleaned.csv", index=False)
print(f"\n💾 Đã lưu: onlinebuy_cleaned.csv")

# Cập nhật df
df = df_clean.copy()

# ============================================================
# 3. FACTOR ANALYSIS
# ============================================================

print("\n\n📊 BƯỚC 3: FACTOR ANALYSIS")
print("-"*80)

try:
    from factor_analyzer import FactorAnalyzer
    from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity
    
    print("✅ Thư viện factor-analyzer đã có sẵn")
except ImportError:
    print("⚠️  Đang cài đặt thư viện factor-analyzer...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'factor-analyzer', '-q'])
    from factor_analyzer import FactorAnalyzer
    from factor_analyzer.factor_analyzer import calculate_kmo, calculate_bartlett_sphericity
    print("✅ Đã cài đặt thành công!")

# 3.1. KMO & Bartlett's Test
print("\n🔍 3.1. KMO & Bartlett's Test")

kmo_all, kmo_model = calculate_kmo(df[likert_cols])

print(f"\n   KMO Score: {kmo_model:.3f}")
if kmo_model >= 0.9:
    print(f"   → ✅ Tuyệt vời (≥0.9)")
elif kmo_model >= 0.8:
    print(f"   → ✅ Rất tốt (≥0.8)")
elif kmo_model >= 0.7:
    print(f"   → ✅ Trung bình (≥0.7)")
elif kmo_model >= 0.6:
    print(f"   → ⚠️  Vừa phải (≥0.6)")
else:
    print(f"   → ❌ Không phù hợp (<0.6)")

# Bartlett's Test
chi_square_value, p_value = calculate_bartlett_sphericity(df[likert_cols])

print(f"\n   Bartlett's Test:")
print(f"     Chi-square: {chi_square_value:.2f}")
print(f"     p-value: {p_value:.4f}")
if p_value < 0.05:
    print(f"   → ✅ Có ý nghĩa thống kê (p < 0.05)")
    print(f"   → ✅ Dữ liệu phù hợp cho Factor Analysis")
else:
    print(f"   → ❌ Không có ý nghĩa thống kê (p ≥ 0.05)")

# 3.2. Xác định số nhân tố tối ưu
print("\n🔍 3.2. Xác định số nhân tố tối ưu")

fa_test = FactorAnalyzer(n_factors=len(likert_cols), rotation=None)
fa_test.fit(df[likert_cols])

ev, v = fa_test.get_eigenvalues()

print(f"\n   Eigenvalues (Kaiser Criterion: > 1.0):")
n_factors_optimal = sum(ev > 1.0)
for i, eigenvalue in enumerate(ev[:10], 1):
    marker = "✅" if eigenvalue > 1.0 else "  "
    print(f"   {marker} Factor {i}: {eigenvalue:.3f}")

print(f"\n   💡 Số nhân tố tối ưu: {n_factors_optimal}")

# 3.3. Chạy Factor Analysis với Varimax rotation
print(f"\n🔍 3.3. Factor Analysis với Varimax Rotation")

fa = FactorAnalyzer(n_factors=n_factors_optimal, rotation='varimax')
fa.fit(df[likert_cols])

loadings = fa.loadings_

# Tạo DataFrame
loadings_df = pd.DataFrame(
    loadings,
    index=likert_cols,
    columns=[f'Factor{i+1}' for i in range(n_factors_optimal)]
)

print(f"\n   📋 Factor Loadings (chỉ hiển thị |loading| ≥ 0.4):")
for col in loadings_df.columns:
    print(f"\n   {col}:")
    high_loadings = loadings_df[col][abs(loadings_df[col]) >= 0.4].sort_values(ascending=False)
    if len(high_loadings) > 0:
        for var, loading in high_loadings.items():
            print(f"     {var:8s}: {loading:6.3f}")
    else:
        print(f"     (Không có biến nào có loading ≥ 0.4)")

# Variance Explained
variance = fa.get_factor_variance()
print(f"\n   📊 Phương sai giải thích:")
print(f"     Tổng: {variance[2][-1]*100:.1f}%")

# Lưu kết quả
loadings_df.to_csv("factor_loadings.csv")
print(f"\n💾 Đã lưu: factor_loadings.csv")

# ============================================================
# 4. REGRESSION ANALYSIS
# ============================================================

print("\n\n📈 BƯỚC 4: REGRESSION ANALYSIS")
print("-"*80)

try:
    import statsmodels.api as sm
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    print("✅ Thư viện statsmodels đã có sẵn")
except ImportError:
    print("⚠️  Đang cài đặt thư viện statsmodels...")
    import subprocess
    subprocess.check_call(['pip', 'install', 'statsmodels', '-q'])
    import statsmodels.api as sm
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    print("✅ Đã cài đặt thành công!")

# Tạo các biến aggregate
print("\n🔧 Tạo các biến aggregate...")

df['INT'] = df[['int1','int2']].mean(axis=1)
df['INF'] = df[['inf1','inf2','inf3']].mean(axis=1)
df['VE'] = df[['ve1','ve2','ve3']].mean(axis=1)
df['NVSE'] = df[['nvse1','nvse2']].mean(axis=1)
df['TRUST'] = df[['trust1','trust2','trust3']].mean(axis=1)
df['CONV'] = df[['conv1','conv2','conv3','conv4']].mean(axis=1)
df['ENJ'] = df[['enj1','enj2','enj3']].mean(axis=1)
df['SC'] = df[['sc1','sc2']].mean(axis=1)
df['AL'] = df[['al1','al2','al3']].mean(axis=1)

print("✅ Đã tạo 9 biến aggregate")

# 4.1. Regression 1: Platform Features → Attitudinal Loyalty
print("\n📊 4.1. REGRESSION 1: Platform Features → Attitudinal Loyalty")
print("-"*60)

X1_vars = ['INT', 'INF', 'VE', 'NVSE']
X1 = df[X1_vars]
y = df['AL']

X1_with_const = sm.add_constant(X1)
model1 = sm.OLS(y, X1_with_const).fit()

print(f"\n   R² = {model1.rsquared:.4f}")
print(f"   Adjusted R² = {model1.rsquared_adj:.4f}")
print(f"   F-statistic = {model1.fvalue:.4f} (p = {model1.f_pvalue:.4f})")

print(f"\n   Coefficients:")
results1 = pd.DataFrame({
    'Variable': model1.params.index,
    'Coefficient': model1.params.values,
    'p-value': model1.pvalues.values,
    'Sig': ['***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else '' 
            for p in model1.pvalues.values]
})
print(results1.to_string(index=False))
print(f"\n   Ghi chú: *** p<0.001, ** p<0.01, * p<0.05")

# VIF check
print(f"\n   🔍 VIF (Multicollinearity Check):")
vif_data1 = pd.DataFrame()
vif_data1["Variable"] = X1_vars
vif_data1["VIF"] = [variance_inflation_factor(X1.values, i) for i in range(len(X1_vars))]
print(vif_data1.to_string(index=False))

# 4.2. Regression 2: Psychological Factors → Attitudinal Loyalty
print("\n\n📊 4.2. REGRESSION 2: Psychological Factors → Attitudinal Loyalty")
print("-"*60)

X2_vars = ['TRUST', 'CONV', 'ENJ', 'SC']
X2 = df[X2_vars]

X2_with_const = sm.add_constant(X2)
model2 = sm.OLS(y, X2_with_const).fit()

print(f"\n   R² = {model2.rsquared:.4f}")
print(f"   Adjusted R² = {model2.rsquared_adj:.4f}")
print(f"   F-statistic = {model2.fvalue:.4f} (p = {model2.f_pvalue:.4f})")

print(f"\n   Coefficients:")
results2 = pd.DataFrame({
    'Variable': model2.params.index,
    'Coefficient': model2.params.values,
    'p-value': model2.pvalues.values,
    'Sig': ['***' if p < 0.001 else '**' if p < 0.01 else '*' if p < 0.05 else '' 
            for p in model2.pvalues.values]
})
print(results2.to_string(index=False))
print(f"\n   Ghi chú: *** p<0.001, ** p<0.01, * p<0.05")

# VIF check
print(f"\n   🔍 VIF (Multicollinearity Check):")
vif_data2 = pd.DataFrame()
vif_data2["Variable"] = X2_vars
vif_data2["VIF"] = [variance_inflation_factor(X2.values, i) for i in range(len(X2_vars))]
print(vif_data2.to_string(index=False))

# So sánh 2 models
print("\n\n📊 SO SÁNH 2 MODELS:")
print("-"*60)

comparison = pd.DataFrame({
    'Model': ['Model 1: Platform', 'Model 2: Psychology'],
    'R²': [model1.rsquared, model2.rsquared],
    'Adj. R²': [model1.rsquared_adj, model2.rsquared_adj],
    'F-statistic': [model1.fvalue, model2.fvalue],
    'Prob (F)': [model1.f_pvalue, model2.f_pvalue]
})
print(comparison.to_string(index=False))

# Lưu kết quả
results1.to_csv("regression1_results.csv", index=False)
results2.to_csv("regression2_results.csv", index=False)
print(f"\n💾 Đã lưu:")
print(f"   - regression1_results.csv")
print(f"   - regression2_results.csv")

# ============================================================
# 5. TÓM TẮT KẾT QUẢ
# ============================================================

print("\n\n" + "="*80)
print("🎯 TÓM TẮT KẾT QUẢ PHÂN TÍCH")
print("="*80)

print(f"\n1️⃣ DATA CLEANING:")
print(f"   ✅ Đã loại bỏ {len(invalid_rows)} mẫu không hợp lệ")
print(f"   ✅ Còn lại {len(df_clean)} mẫu sử dụng cho phân tích")

print(f"\n2️⃣ FACTOR ANALYSIS:")
print(f"   ✅ KMO Score: {kmo_model:.3f}")
print(f"   ✅ Số nhân tố tối ưu: {n_factors_optimal}")
print(f"   ✅ Phương sai giải thích: {variance[2][-1]*100:.1f}%")

print(f"\n3️⃣ REGRESSION 1 (Platform → Loyalty):")
print(f"   ✅ R² = {model1.rsquared:.4f}")
print(f"   ✅ Significant variables:")
for var in X1_vars:
    if model1.pvalues[var] < 0.05:
        coef = model1.params[var]
        print(f"      • {var}: {coef:+.4f} (p < 0.05)")

print(f"\n4️⃣ REGRESSION 2 (Psychology → Loyalty):")
print(f"   ✅ R² = {model2.rsquared:.4f}")
print(f"   ✅ Significant variables:")
for var in X2_vars:
    if model2.pvalues[var] < 0.05:
        coef = model2.params[var]
        print(f"      • {var}: {coef:+.4f} (p < 0.05)")

print("\n\n📁 FILES ĐÃ TẠO:")
print("   ✅ onlinebuy_cleaned.csv - Dữ liệu sau khi làm sạch")
print("   ✅ factor_loadings.csv - Kết quả Factor Analysis")
print("   ✅ regression1_results.csv - Kết quả Regression 1")
print("   ✅ regression2_results.csv - Kết quả Regression 2")

print("\n\n" + "="*80)
print("🎉 HOÀN THÀNH TẤT CẢ PHÂN TÍCH!")
print("="*80)
print("\n📖 BƯỚC TIẾP THEO:")
print("   1. Xem các file CSV đã tạo để lấy kết quả")
print("   2. Copy kết quả vào báo cáo Word")
print("   3. Tìm 15+ references")
print("   4. Viết báo cáo 4,000 từ")
print("\n💪 GOOD LUCK!\n")
