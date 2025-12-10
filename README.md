# 📊 DỰ ÁN PHÂN TÍCH MARKETING - MDA2025

**Chủ đề:** Các yếu tố quyết định lòng trung thành của người tiêu dùng trên nền tảng TMĐT đối với sản phẩm truyền thống Việt Nam

---

## 📁 CẤU TRÚC DỰ ÁN

```
Mardata/
├── 📊 DATA
│   ├── onlinebuy.csv                    # Dữ liệu gốc (351 mẫu)
│   └── onlinebuy_cleaned.csv            # Dữ liệu sau khi làm sạch (tạo sau)
│
├── 📓 NOTEBOOKS
│   ├── Phân_tích_marketing_UPDATED.ipynb    # Notebook chính (90% hoàn thành)
│   └── Missing_Parts_Marketing_Analysis.ipynb
│
├── 📝 ĐỀ BÀI & HƯỚNG DẪN
│   ├── HUONG_DAN_BO_SUNG.md             # Hướng dẫn từ conversation trước
│   ├── PROJECT_STATUS_REPORT.md         # ⭐ BÁO CÁO TỔNG QUAN ⭐
│   └── ACTION_CHECKLIST.md              # ⭐ CHECKLIST HÀNH ĐỘNG ⭐
│
├── 📄 BÁO CÁO (chưa có - cần tạo)
│   ├── MDA2025Report.Group1.LeaderName.StudentID.docx
│   ├── conceptual_model.png
│   └── references.txt
│
└── 📊 KẾT QUẢ & TÀI LIỆU
    ├── FINAL_SUMMARY.md
    ├── CLUSTER_SUMMARY_TABLE.md
    └── cluster_overview.png (nếu có)
```

---

## 🚀 BẮT ĐẦU NGAY

### ⚡ NHANH NHẤT - 3 BƯỚC:

#### 1️⃣ ĐỌC BÁO CÁO TỔNG QUAN (5 phút)
```bash
📖 Đọc file: PROJECT_STATUS_REPORT.md
```
**Nội dung:**
- Đánh giá tiến độ hiện tại (70/100)
- Phân tích chi tiết 5 câu hỏi nghiên cứu
- Roadmap 3 tuần hoàn thành

#### 2️⃣ XEM CHECKLIST HÀNH ĐỘNG (3 phút)
```bash
✅ Đọc file: ACTION_CHECKLIST.md
```
**Nội dung:**
- Code sẵn sàng chạy (copy/paste)
- Ưu tiên làm ngay hôm nay
- Tracking tiến độ hàng ngày

#### 3️⃣ BẮT ĐẦU LÀM VIỆC (NGAY!)
```bash
🔥 Mở file: Phân_tích_marketing_UPDATED.ipynb
```
**Làm theo thứ tự:**
1. Chạy Data Cleaning (code trong ACTION_CHECKLIST.md)
2. Thêm Factor Analysis
3. Hoàn thiện Regression

---

## 📊 TIẾN ĐỘ HIỆN TẠI

### ✅ ĐÃ HOÀN THÀNH (70%)
- [x] **Descriptive Analysis** - 100% ✓
- [x] **Cluster Analysis** - 100% ✓ (3 clusters có tên)
- [x] **Correlation** - 90% ✓ (có heatmap)
- [x] **Code Infrastructure** - 100% ✓

### ⚠️ CẦN BỔ SUNG (30%)
- [ ] **Data Cleaning** - 0% (theo yêu cầu GV)
- [ ] **Factor Analysis** - Cần kiểm tra
- [ ] **Regression** - 60% (cần 2 phân tích rõ ràng)
- [ ] **Word Report** - 0% (4,000 từ)
- [ ] **References** - 0/15 bài

---

## 🎯 MỤC TIÊU TUẦN NÀY (9-15/12)

### Ngày 1-2: Data & Factor
- [ ] Data Cleaning code
- [ ] Loại bỏ invalid responses
- [ ] Factor Analysis (KMO, Bartlett's, EFA)

### Ngày 3-4: Regression
- [ ] Regression 1: Platform → Loyalty
- [ ] Regression 2: Psychology → Loyalty
- [ ] VIF check, R² analysis

### Ngày 5-7: References
- [ ] Tìm 5 bài về E-commerce Trust
- [ ] Tìm 5 bài về Consumer Loyalty
- [ ] Tìm 5 bài về Vietnamese Market

---

## 📚 TÀI LIỆU QUAN TRỌNG

### 🔴 ƯU TIÊN ĐỌC TRƯỚC

| File | Mục đích | Thời gian đọc |
|------|----------|---------------|
| **PROJECT_STATUS_REPORT.md** | Hiểu tổng quan dự án | 10 phút |
| **ACTION_CHECKLIST.md** | Code sẵn sàng chạy | 5 phút |
| **HUONG_DAN_BO_SUNG.md** | Context từ lần trước | 5 phút |

### 🟡 TÀI LIỆU THAM KHẢO

| File | Mục đích |
|------|----------|
| **FINAL_SUMMARY.md** | Kết quả từ conversation trước |
| **CLUSTER_SUMMARY_TABLE.md** | Chi tiết 3 clusters |

---

## 🔧 YÊU CẦU KỸ THUẬT

### Môi trường
- **Google Colab** hoặc **Jupyter Notebook**
- **Python 3.8+**

### Thư viện đã dùng
```python
pandas==2.0.0
numpy==1.24.0
matplotlib==3.7.0
seaborn==0.12.0
scikit-learn==1.2.0
statsmodels (cho regression)
```

### Thư viện CẦN CÀI THÊM
```bash
!pip install factor-analyzer
```

---

## 📋 BỘ DỮ LIỆU

### Thông tin cơ bản
- **Tổng mẫu:** 351 người
- **Biến số:** 38 cột
  - 25 biến Likert (1-5)
  - 13 biến demographic (dummy)

### Cấu trúc dữ liệu

#### Biến Likert (25 biến)
```
Platform:     int1, int2, inf1-3, ve1-3, nvse1-2
Psychology:   trust1-3, conv1-4, enj1-3, sc1-2
Loyalty:      al1, al2, al3
```

#### Biến Demographic (13 biến)
```
Gender:       gender_0, gender_1
Occupation:   occupation_0, occupation_1, occupation_2
Frequency:    freq_0, freq_1, freq_2, freq_3
Age:          age_0, age_1, age_2
```

---

## 📈 KẾT QUẢ CHÍNH (từ phân tích hiện có)

### 3 Nhóm Khách Hàng

| Cluster | Tên | Số lượng | Đặc điểm chính |
|---------|-----|----------|----------------|
| 0 | **Enthusiastic Shoppers** | 133 (38%) | Nhiệt tình, tin tưởng vừa |
| 1 | **Skeptical Browsers** | 140 (40%) | Nghi ngờ, thiếu tin tưởng |
| 2 | **Convenience Seekers** | 78 (22%) | VIP, hoàn hảo nhất |

### Chiến lược Marketing

**Cluster 0:** Loyalty programs, xây dựng trust  
**Cluster 1:** Incentives, giảm rủi ro  
**Cluster 2:** Premium services, VIP experience

---

## ⚠️ ISSUES ĐANG CÓ

### ❌ Critical (Làm ngay)
1. **Data Cleaning chưa có** - Vi phạm yêu cầu GV
2. **Factor Analysis không rõ** - Cần kiểm tra/bổ sung
3. **Regression chưa đủ** - Cần 2 phân tích riêng biệt

### ⚠️ Important (Làm tuần này)
4. **References = 0** - Cần 15+ bài
5. **Conceptual Model chưa có** - Cần diagram
6. **Word Report chưa bắt đầu** - 4,000 từ

### 🟢 Nice to have
7. Dashboard trực quan hóa
8. Presentation slides

---

## 🆘 TROUBLESHOOTING

### Lỗi thường gặp

**Q: Cell không chạy được?**  
A: Chạy lại từ đầu notebook (Runtime → Restart and Run All)

**Q: Thiếu thư viện?**  
A: `!pip install [tên-thư-viện]`

**Q: Dữ liệu không load được?**  
A: Kiểm tra path file CSV

**Q: Factor Analysis lỗi?**  
A: Cài `!pip install factor-analyzer`

---

## 📞 HỖ TRỢ

### Nếu gặp vấn đề:
1. ✅ Kiểm tra lại code trong ACTION_CHECKLIST.md
2. ✅ Đọc error message kỹ
3. ✅ Google error message
4. ✅ Hỏi ChatGPT/Claude (nhớ ghi Honor Code!)

### Nếu cần hỗ trợ nhóm:
- Báo cáo hỗ trợ cho GV
- Ảnh hưởng điểm cộng!

---

## ✅ CHECKLIST TRƯỚC KHI NỘP

### Code
- [ ] Notebook chạy được từ đầu đến cuối
- [ ] Tất cả cells có output
- [ ] Dữ liệu đã làm sạch

### Báo cáo
- [ ] Số từ: 3,600-4,400 ✓
- [ ] References: ≥15 ✓
- [ ] Conceptual Model có ✓
- [ ] Questionnaire đính kèm ✓

### Files
- [ ] Đặt tên đúng format
- [ ] MDA2025Report.Group1.LeaderName.StudentID.docx
- [ ] MDA2025Data.Group1.LeaderName.StudentID.csv

---

## 🎯 TIMELINE TỔNG QUAN

```
Tuần 1 (9-15/12):  Data Cleaning + Factor + Regression
Tuần 2 (16-22/12): Viết báo cáo Word (4,000 từ)
Tuần 3 (23-27/12): Review + Polish + Nộp bài
```

**Deadline dự kiến:** 27/12/2025

---

## 📝 GHI CHÚ QUAN TRỌNG

### 💡 Lời khuyên từ GV:
- "Ngay từ đầu cần thống nhất cách định nghĩa khái niệm"
- "Không hỏi lặp lại những câu đã được hướng dẫn nhiều lần"
- "Hỗ trợ nhóm khác cần báo cáo → ảnh hưởng điểm"

### 🎨 Câu chuyện (Story):
- Không giới hạn - có thể mở rộng
- Mỗi nhóm góc nhìn khác nhau → không lo trùng
- Quan trọng: Thuyết phục dựa trên dữ liệu

---

## 📧 THÔNG TIN DỰ ÁN

**Môn học:** Marketing Data Analytics (MDA2025)  
**Học kỳ:** HK1 2025-2026  
**Loại bài:** Group Project  
**Số lượng thành viên:** 4-6 người (khuyến nghị)

---

## 🚀 BẮT ĐẦU NGAY!

```bash
# 1. Đọc báo cáo tổng quan
📖 PROJECT_STATUS_REPORT.md

# 2. Xem checklist hành động
✅ ACTION_CHECKLIST.md

# 3. Mở notebook và làm việc
🔥 Phân_tích_marketing_UPDATED.ipynb

# 4. Follow roadmap 3 tuần
📅 Tuần 1: Data + Analysis
📅 Tuần 2: Báo cáo Word
📅 Tuần 3: Review + Nộp
```

