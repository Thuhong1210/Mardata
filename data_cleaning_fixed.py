# ============================================================
# DATA CLEANING - PHIÊN BẢN CẢI TIẾN
# ============================================================

print("="*80)
print("🧹 BƯỚC 1: DATA CLEANING")
print("="*80)

# Import libraries (nếu chưa có)
try:
    import pandas as pd
    import numpy as np
except ImportError as e:
    print(f"❌ Lỗi import: {e}")
    print("Vui lòng chạy: !pip install pandas numpy")

# Kiểm tra df đã tồn tại chưa
try:
    _ = df.shape
    print(f"\n✅ DataFrame đã sẵn sàng: {df.shape}")
except NameError:
    print("\n❌ LỖI: Biến 'df' chưa được tạo!")
    print("Vui lòng chạy cell đọc dữ liệu trước:")
    print("   df = pd.read_csv('onlinebuy.csv')")
    raise

# Định nghĩa các cột Likert
likert_cols = [
    'int1', 'int2', 'inf1', 'inf2', 'inf3', 
    've1', 've2', 've3', 'nvse1', 'nvse2',
    'trust1', 'trust2', 'trust3', 
    'conv1', 'conv2', 'conv3', 'conv4',
    'enj1', 'enj2', 'enj3', 
    'sc1', 'sc2', 
    'al1', 'al2', 'al3'
]

# Kiểm tra các cột có tồn tại không
print(f"\n🔍 Kiểm tra cột dữ liệu...")
missing_cols = [col for col in likert_cols if col not in df.columns]
if missing_cols:
    print(f"❌ LỖI: Thiếu các cột sau trong dữ liệu:")
    for col in missing_cols:
        print(f"   - {col}")
    print(f"\n📋 Các cột hiện có trong df:")
    print(df.columns.tolist())
    raise ValueError(f"Thiếu {len(missing_cols)} cột trong dữ liệu")
else:
    print(f"✅ Tất cả {len(likert_cols)} cột Likert đều có trong dữ liệu")

# Function kiểm tra dữ liệu không hợp lệ
def check_invalid(row):
    """
    Kiểm tra dữ liệu không hợp lệ
    
    Tiêu chí loại bỏ:
    1. Tất cả 25 giá trị giống nhau
    2. Có ≥10 giá trị liên tiếp giống nhau
    
    Returns:
        bool: True nếu không hợp lệ, False nếu hợp lệ
    """
    try:
        vals = row[likert_cols].values
        
        # Kiểm tra tiêu chí 1: Tất cả giống nhau
        if len(set(vals)) == 1:
            return True
        
        # Kiểm tra tiêu chí 2: 10 liên tiếp giống nhau
        max_consec = 1
        current = 1
        
        for i in range(1, len(vals)):
            if vals[i] == vals[i-1]:
                current += 1
                max_consec = max(max_consec, current)
            else:
                current = 1
        
        return max_consec >= 10
    
    except Exception as e:
        print(f"⚠️  Lỗi khi kiểm tra row {row.name}: {e}")
        return False

# Tìm các mẫu không hợp lệ
print(f"\n🔍 Đang kiểm tra {len(df)} mẫu...")
try:
    invalid = [i for i, row in df.iterrows() if check_invalid(row)]
except Exception as e:
    print(f"❌ LỖI khi kiểm tra dữ liệu: {e}")
    raise

# Báo cáo kết quả
print(f"\n📊 KẾT QUẢ KIỂM TRA:")
print(f"   Tổng mẫu ban đầu: {len(df)}")
print(f"   Mẫu không hợp lệ: {len(invalid)} ({len(invalid)/len(df)*100:.1f}%)")

if len(invalid) > 0:
    print(f"\n   📋 Danh sách 10 mẫu đầu tiên bị loại:")
    for idx in invalid[:10]:
        vals = df.loc[idx, likert_cols].values
        unique_vals = len(set(vals))
        print(f"      Row {idx}: {unique_vals} giá trị unique")
else:
    print(f"\n   ✅ Không có mẫu nào bị loại bỏ!")

# Loại bỏ dữ liệu không hợp lệ
if len(invalid) > 0:
    print(f"\n🗑️  Đang loại bỏ {len(invalid)} mẫu...")
    df_original = df.copy()  # Backup
    df = df.drop(invalid).reset_index(drop=True)
    print(f"   ✅ Đã loại bỏ thành công!")
else:
    print(f"\n   ℹ️  Không có gì để loại bỏ")

# Kết quả cuối cùng
print(f"\n" + "="*80)
print(f"✅ KẾT QUẢ SAU KHI LÀM SẠCH:")
print(f"="*80)
print(f"   Mẫu ban đầu:  {len(df) + len(invalid)}")
print(f"   Mẫu bị loại:  {len(invalid)}")
print(f"   Mẫu còn lại:  {len(df)} ({len(df)/(len(df)+len(invalid))*100:.1f}%)")

# Lưu dữ liệu sạch
try:
    df.to_csv('onlinebuy_cleaned.csv', index=False)
    print(f"\n💾 Đã lưu dữ liệu sạch: onlinebuy_cleaned.csv")
except Exception as e:
    print(f"\n⚠️  Không thể lưu file: {e}")

print(f"\n" + "="*80)
print(f"🎉 DATA CLEANING HOÀN THÀNH!")
print(f"="*80)

# Hiển thị thống kê cơ bản
print(f"\n📊 THỐNG KÊ DỮ LIỆU SAU KHI LÀM SẠCH:")
print(f"   Shape: {df.shape}")
print(f"   Missing values: {df[likert_cols].isnull().sum().sum()}")
print(f"   Data types: {df[likert_cols].dtypes.value_counts().to_dict()}")
