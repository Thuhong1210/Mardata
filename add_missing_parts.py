#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để tự động thêm các phần thiếu vào notebook phân tích marketing
"""

import json
import sys

def add_correlation_heatmap_cell():
    """Tạo cell cho correlation heatmap"""
    return {
        "cell_type": "code",
        "source": [
            "# ============================================================\n",
            "# 4.1. CORRELATION HEATMAP - Trực quan hóa ma trận tương quan\n",
            "# ============================================================\n",
            "\n",
            "# Tạo heatmap cho ma trận tương quan\n",
            "plt.figure(figsize=(16, 14))\n",
            "sns.heatmap(\n",
            "    corr, \n",
            "    annot=True,      # Hiển thị giá trị số\n",
            "    fmt='.2f',       # Format 2 chữ số thập phân\n",
            "    cmap='coolwarm', # Màu sắc: đỏ = tương quan dương, xanh = tương quan âm\n",
            "    center=0,        # Trung tâm tại 0\n",
            "    square=True,     # Ô vuông\n",
            "    linewidths=0.5,  # Đường chia\n",
            "    cbar_kws={\"shrink\": 0.8}\n",
            ")\n",
            "plt.title('Ma trận tương quan Pearson giữa các biến', fontsize=16, pad=20)\n",
            "plt.tight_layout()\n",
            "plt.show()\n",
            "\n",
            "print(\"\\n📊 Giải thích:\")\n",
            "print(\"- Màu đỏ đậm: Tương quan dương mạnh (gần +1)\")\n",
            "print(\"- Màu xanh đậm: Tương quan âm mạnh (gần -1)\")\n",
            "print(\"- Màu trắng: Không có tương quan (gần 0)\")\n"
        ],
        "metadata": {
            "id": "correlation_heatmap_new"
        },
        "execution_count": None,
        "outputs": []
    }

def add_cluster_naming_cell():
    """Tạo cell cho cluster naming"""
    return {
        "cell_type": "code",
        "source": [
            "# ============================================================\n",
            "# 5.1. ĐẶT TÊN CHO CÁC CLUSTER\n",
            "# ============================================================\n",
            "\n",
            "# Xem lại đặc điểm trung bình của từng cluster\n",
            "cluster_stats = df.groupby('cluster')[cluster_vars].mean().round(3)\n",
            "print(\"Đặc điểm trung bình của từng cluster:\")\n",
            "display(cluster_stats)\n",
            "\n",
            "# Phân tích để đặt tên cluster\n",
            "print(\"\\n\" + \"=\"*70)\n",
            "print(\"PHÂN TÍCH ĐẶC ĐIỂM CỤM:\")\n",
            "print(\"=\"*70)\n",
            "\n",
            "# Cluster 0: Purchase Intention, Trust, Convenience, Enjoyment cao\n",
            "print(\"\\n🎯 Cluster 0: 'Enthusiastic Shoppers' (Người mua sắm nhiệt tình)\")\n",
            "print(\"   - Đặc điểm: INT cao (4.594), TRUST cao (3.396), CONV cao (4.152), ENJ cao (4.080)\")\n",
            "print(\"   - VE trung bình (2.446), NVSE thấp (1.827)\")\n",
            "print(\"   - Ý nghĩa: Nhóm có ý định mua cao, tin tưởng và thích thú với mua sắm online\")\n",
            "\n",
            "# Cluster 1: Tất cả chỉ số thấp nhất\n",
            "print(\"\\n😟 Cluster 1: 'Skeptical Browsers' (Người duyệt web nghi ngờ)\")\n",
            "print(\"   - Đặc điểm: INT thấp nhất (3.114), TRUST thấp nhất (2.871), CONV thấp nhất (3.393)\")\n",
            "print(\"   - VE cao nhất (2.569), NVSE cao nhất (2.979)\")\n",
            "print(\"   - Ý nghĩa: Nhóm ít tin tưởng, ít ý định mua, lo lắng về rủi ro và tự đánh giá tiêu cực\")\n",
            "\n",
            "# Cluster 2: INT cao nhất, VE thấp nhất, các chỉ số dương tính cao nhất\n",
            "print(\"\\n⭐ Cluster 2: 'Convenience Seekers' (Người tìm kiếm sự tiện lợi)\")\n",
            "print(\"   - Đặc điểm: INT cao nhất (4.641), CONV cao nhất (4.766), ENJ cao nhất (4.970)\")\n",
            "print(\"   - TRUST cao nhất (4.308), VE thấp nhất (1.624), NVSE thấp nhất (1.468)\")\n",
            "print(\"   - Ý nghĩa: Nhóm hoàn hảo - tin tưởng cao, rủi ro thấp, yêu thích sự tiện lợi\")\n",
            "\n",
            "# Tạo dictionary mapping cluster number sang tên\n",
            "cluster_names = {\n",
            "    0: 'Enthusiastic Shoppers',\n",
            "    1: 'Skeptical Browsers', \n",
            "    2: 'Convenience Seekers'\n",
            "}\n",
            "\n",
            "# Thêm cột tên cluster vào dataframe\n",
            "df['cluster_name'] = df['cluster'].map(cluster_names)\n",
            "\n",
            "# Hiển thị phân bố\n",
            "print(\"\\n\" + \"=\"*70)\n",
            "print(\"PHÂN BỐ SỐ LƯỢNG KHÁCH HÀNG THEO CỤM:\")\n",
            "print(\"=\"*70)\n",
            "cluster_distribution = df.groupby(['cluster', 'cluster_name']).size().reset_index(name='Số lượng')\n",
            "cluster_distribution['Tỷ lệ (%)'] = (cluster_distribution['Số lượng'] / len(df) * 100).round(2)\n",
            "display(cluster_distribution)\n",
            "\n",
            "# Tạo visualization cho cluster names\n",
            "plt.figure(figsize=(10, 6))\n",
            "counts = df['cluster_name'].value_counts()\n",
            "colors = ['#2ecc71', '#e74c3c', '#3498db']  # Màu cho mỗi cluster\n",
            "plt.bar(counts.index, counts.values, color=colors, edgecolor='black', linewidth=1.5)\n",
            "plt.xlabel('Tên Cluster', fontsize=12, fontweight='bold')\n",
            "plt.ylabel('Số lượng khách hàng', fontsize=12, fontweight='bold')\n",
            "plt.title('Phân bố khách hàng theo các nhóm', fontsize=14, fontweight='bold')\n",
            "plt.xticks(rotation=15, ha='right')\n",
            "\n",
            "# Thêm số lượng trên mỗi cột\n",
            "for i, (name, value) in enumerate(counts.items()):\n",
            "    plt.text(i, value + 2, str(value), ha='center', fontweight='bold', fontsize=11)\n",
            "    \n",
            "plt.tight_layout()\n",
            "plt.show()\n",
            "\n",
            "print(\"\\n✅ Đã hoàn thành việc đặt tên các cluster!\")\n",
            "print(\"Cột 'cluster_name' đã được thêm vào dataframe.\")\n"
        ],
        "metadata": {
            "id": "cluster_naming_new"
        },
        "execution_count": None,
        "outputs": []
    }

def add_marketing_insights_cell():
    """Tạo cell cho marketing insights"""
    return {
        "cell_type": "code",
        "source": [
            "# ============================================================\n",
            "# 5.2. MARKETING INSIGHTS & RECOMMENDATIONS\n",
            "# ============================================================\n",
            "\n",
            "print(\"=\"*80)\n",
            "print(\"🎯 CHIẾN LƯỢC MARKETING CHO TỪNG NHÓM KHÁCH HÀNG\")\n",
            "print(\"=\"*80)\n",
            "\n",
            "print(\"\\n\" + \"-\"*80)\n",
            "print(\"📊 CLUSTER 0: 'ENTHUSIASTIC SHOPPERS' (Người mua sắm nhiệt tình)\")\n",
            "print(f\"   Số lượng: {len(df[df['cluster']==0])} khách hàng ({len(df[df['cluster']==0])/len(df)*100:.1f}%)\")\n",
            "print(\"-\"*80)\n",
            "print(\"💡 Chiến lược:\")\n",
            "print(\"   • Loyalty Programs: Tạo chương trình khách hàng thân thiết với ưu đãi đặc biệt\")\n",
            "print(\"   • Premium Services: Cung cấp dịch vụ giao hàng nhanh, free shipping\")\n",
            "print(\"   • Exclusive Offers: Gửi ưu đãi độc quyền, flash sale sớm nhất\")\n",
            "print(\"   • Social Proof: Thu thập review tích cực từ nhóm này\")\n",
            "print(\"   • Upselling/Cross-selling: Giới thiệu sản phẩm cao cấp hơn\")\n",
            "\n",
            "print(\"\\n\" + \"-\"*80)\n",
            "print(\"📊 CLUSTER 1: 'SKEPTICAL BROWSERS' (Người duyệt web nghi ngờ)\")\n",
            "print(f\"   Số lượng: {len(df[df['cluster']==1])} khách hàng ({len(df[df['cluster']==1])/len(df)*100:.1f}%)\")\n",
            "print(\"-\"*80)\n",
            "print(\"💡 Chiến lược:\")\n",
            "print(\"   • Trust Building: Hiển thị chứng chỉ bảo mật, đảm bảo hoàn tiền\")\n",
            "print(\"   • Risk Reduction: Chính sách đổi trả linh hoạt, dùng thử miễn phí\")\n",
            "print(\"   • Social Proof: Hiển thị review, rating, số người đã mua\")\n",
            "print(\"   • First Purchase Incentives: Giảm giá lần đầu, freeship đơn đầu\")\n",
            "print(\"   • Education: Hướng dẫn chi tiết về sản phẩm, FAQ đầy đủ\")\n",
            "print(\"   • Customer Support: Hỗ trợ 24/7, chatbot thông minh\")\n",
            "\n",
            "print(\"\\n\" + \"-\"*80)\n",
            "print(\"📊 CLUSTER 2: 'CONVENIENCE SEEKERS' (Người tìm kiếm sự tiện lợi)\")\n",
            "print(f\"   Số lượng: {len(df[df['cluster']==2])} khách hàng ({len(df[df['cluster']==2])/len(df)*100:.1f}%)\")\n",
            "print(\"-\"*80)\n",
            "print(\"💡 Chiến lược:\")\n",
            "print(\"   • Convenience Features: 1-click checkout, lưu thông tin thanh toán\")\n",
            "print(\"   • Fast Delivery: Giao hàng trong ngày, express delivery\")\n",
            "print(\"   • Mobile Optimization: App mobile mượt mà, thân thiện\")\n",
            "print(\"   • Subscription Model: Đăng ký nhận hàng định kỳ (auto-replenish)\")\n",
            "print(\"   • Personalization: Gợi ý sản phẩm dựa trên lịch sử mua\")\n",
            "print(\"   • Premium Experience: VIP support, dedicated account manager\")\n",
            "\n",
            "print(\"\\n\" + \"=\"*80)\n",
            "print(\"✅ KẾT LUẬN TỔNG QUAN\")\n",
            "print(\"=\"*80)\n",
            "print(\"\"\"  \n",
            "• Cluster 2 (Convenience Seekers): Nhóm VIP - Đầu tư mạnh nhất\n",
            "• Cluster 0 (Enthusiastic Shoppers): Nhóm tiềm năng - Duy trì & phát triển\n",
            "• Cluster 1 (Skeptical Browsers): Nhóm cần chuyển đổi - Tập trung xây dựng lòng tin\n",
            "\n",
            "🎯 Ưu tiên:\n",
            "1. Giữ chân và phát triển Cluster 2 (Revenue cao nhất)\n",
            "2. Nâng cấp Cluster 0 lên Cluster 2\n",
            "3. Chuyển đổi Cluster 1 thành khách hàng trung thành\n",
            "\"\"\")\n",
            "print(\"=\"*80)\n"
        ],
        "metadata": {
            "id": "marketing_insights_new"
        },
        "execution_count": None,
        "outputs": []
    }

def main():
    input_file = "/Users/admin/Downloads/Phân_tích_marketing.ipynb"
    output_file = "/Users/admin/Downloads/Phân_tích_marketing_UPDATED.ipynb"
    
    print("🔄 Đang đọc file notebook gốc...")
    with open(input_file, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    cells = notebook['cells']
    new_cells = []
    
    print("📝 Đang thêm các phần mới...")
    
    for i, cell in enumerate(cells):
        new_cells.append(cell)
        
        # Sau cell correlation (tìm cell có "corr = df[likert_vars].corr()")
        if cell.get('cell_type') == 'code' and 'source' in cell:
            source_text = ''.join(cell['source'])
            
            # Thêm heatmap sau correlation
            if 'corr = df[likert_vars].corr()' in source_text and 'PEARSON CORRELATION' in source_text:
                print("  ✅ Thêm Correlation Heatmap sau cell correlation")
                new_cells.append(add_correlation_heatmap_cell())
            
            # Thêm cluster naming sau kmeans
            if "df['cluster'] = kmeans.fit_predict(X_scaled)" in source_text and 'K-MEANS CLUSTERING' in source_text:
                print("  ✅ Thêm Cluster Naming sau cell clustering")
                new_cells.append(add_cluster_naming_cell())
                print("  ✅ Thêm Marketing Insights")
                new_cells.append(add_marketing_insights_cell())
    
    notebook['cells'] = new_cells
    
    print(f"\n💾 Đang lưu file mới: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=2)
    
    print("\n" + "="*80)
    print("✅ HOÀN THÀNH!")
    print("="*80)
    print(f"📁 File gốc: {input_file}")
    print(f"📁 File mới:  {output_file}")
    print("\n📊 Đã thêm:")
    print("   1. Correlation Heatmap (sau phần 4. PEARSON CORRELATION)")
    print("   2. Cluster Naming (sau phần 5. K-MEANS CLUSTERING)")
    print("   3. Marketing Insights")
    print("\n🎯 Bước tiếp theo:")
    print(f"   1. Mở file: {output_file}")
    print("   2. Chạy lại tất cả các cell (Run All)")
    print("   3. Kiểm tra kết quả")
    print("="*80)

if __name__ == "__main__":
    main()
