# ============================================================
# CELL BỔ SUNG: TẠO CÁC BIẾN AGGREGATE
# CHẠY CELL NÀY TRƯỚC KHI CHẠY REGRESSION!
# ============================================================

print("="*80)
print("🔧 TẠO CÁC BIẾN AGGREGATE")
print("="*80)

# Tạo các biến aggregate bằng cách tính trung bình
print("\n📊 Đang tạo 8 biến aggregate...")

try:
    # Platform Characteristics
    df['INT'] = df[['int1', 'int2']].mean(axis=1)
    print("   ✅ INT = mean(int1, int2)")
    
    df['INF'] = df[['inf1', 'inf2', 'inf3']].mean(axis=1)
    print("   ✅ INF = mean(inf1, inf2, inf3)")
    
    df['VE'] = df[['ve1', 've2', 've3']].mean(axis=1)
    print("   ✅ VE = mean(ve1, ve2, ve3)")
    
    df['NVSE'] = df[['nvse1', 'nvse2']].mean(axis=1)
    print("   ✅ NVSE = mean(nvse1, nvse2)")
    
    # Psychological Responses
    df['TRUST'] = df[['trust1', 'trust2', 'trust3']].mean(axis=1)
    print("   ✅ TRUST = mean(trust1, trust2, trust3)")
    
    df['CONV'] = df[['conv1', 'conv2', 'conv3', 'conv4']].mean(axis=1)
    print("   ✅ CONV = mean(conv1, conv2, conv3, conv4)")
    
    df['ENJ'] = df[['enj1', 'enj2', 'enj3']].mean(axis=1)
    print("   ✅ ENJ = mean(enj1, enj2, enj3)")
    
    df['SC'] = df[['sc1', 'sc2']].mean(axis=1)
    print("   ✅ SC = mean(sc1, sc2)")
    
    # Attitudinal Loyalty (biến phụ thuộc)
    df['AL'] = df[['al1', 'al2', 'al3']].mean(axis=1)
    print("   ✅ AL = mean(al1, al2, al3)")
    
    print(f"\n✅ Đã tạo thành công 9 biến aggregate!")
    
except KeyError as e:
    print(f"\n❌ LỖI: Thiếu cột {e}")
    print("Vui lòng kiểm tra lại tên các cột trong dữ liệu")
    raise

# Hiển thị thống kê các biến mới
print(f"\n📊 THỐNG KÊ CÁC BIẾN MỚI:")
print("-"*80)

aggregate_vars = ['INT', 'INF', 'VE', 'NVSE', 'TRUST', 'CONV', 'ENJ', 'SC', 'AL']

stats_df = df[aggregate_vars].describe().T[['mean', 'std', 'min', 'max']]
print(stats_df.round(3))

print(f"\n" + "="*80)
print(f"✅ SẴN SÀNG CHO REGRESSION!")
print(f"="*80)
print(f"\n💡 Bây giờ bạn có thể chạy cell Regression!")
