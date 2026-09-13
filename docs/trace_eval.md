# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Trương Hoàng Thành An
> **Mã Sinh Viên / Mã Học viên:** 2A202602574
> **Chủ đề Lựa chọn:** Trợ lý Học vụ & Tra cứu Lịch thi VinUni

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá             | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm                                                                              |
| :--------------------------------- | :---------------: | :---------------------------------------------------------------------------------------------------------------------- |
| **1. Multi-step Reasoning**  |       4 / 5       | Agent xác định nhu cầu, gọi công cụ tra cứu và tổng hợp hồ sơ hoặc lịch thi.                             |
| **2. Tool Interaction**      |       5 / 5       | Agent kết nối MCP Server để tra cứu dữ liệu học vụ và đặt lịch tư vấn.                                   |
| **3. Dynamic Decision**      |       4 / 5       | Agent chọn trả lời trực tiếp hoặc gọi Tool tùy câu hỏi, đồng thời xử lý mã sinh viên không tồn tại. |
| **4. Long Horizon Goal**     |       3 / 5       | Quy trình có thể mở rộng từ tra cứu hồ sơ sang lịch thi và đặt lịch tư vấn trong cùng phiên.          |
| **TỔNG ĐIỂM AGENTIC FIT** | **16 / 20** | *Bài toán phù hợp triển khai Agentic System.*                                                                    |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Chào bạn, bạn có thể giới thiệu quy chế học vụ cơ bản của Đại học VinUni không?",
    "action_type": "FINAL_ANSWER",
    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ).",
    "output": "Chào bạn! Đại học VinUni áp dụng quy chế học vụ chuẩn quốc tế, hướng tới sự xuất sắc trong học thuật và phát triển toàn diện. Dưới đây là một số điểm cốt lõi trong quy chế học vụ cơ bản tại VinUni:\n\n---\n\n### 1. Hệ thống Tín chỉ và Thang điểm\n* **Đơn vị học trình:** Các chương trình đào tạo được thiết kế theo hệ thống tín chỉ (Credits). Mỗi học kỳ sinh viên thường đăng ký từ 12 đến 18 tín chỉ tùy ngành và năng lực học tập.\n* **Thang điểm:** VinUni sử dụng thang điểm chữ từ **A+ đến F**, quy đổi tương đương sang thang điểm 4.0:\n  * **A / A+ (3.7 - 4.0):** Xuất sắc (Excellent)\n  * **B / B+ (3.0 - 3.5):** Giỏi / Khá (Good)\n  * **C / C+ (2.0 - 2.5):** Đạt / Trung bình (Satisfactory)\n  * **D / D+ (1.0 - 1.5):** Đạt mức tối thiểu (Poor/Marginal)\n  * **F (0.0):** Không đạt (Fail - phải học lại hoặc thi lại theo quy định)\n* **Điểm trung bình (GPA & cGPA):** \n  * *GPA (Grade Point Average):* Điểm trung bình của một học kỳ.\n  * *cGPA (Cumulative GPA):* Điểm trung bình tích lũy toàn khóa.\n\n---\n\n### 2. Tình trạng Học vụ (Academic Standing)\n* **Good Standing:** Sinh viên duy trì cGPA đạt chuẩn (thường từ 2.0/4.0 trở lên và đáp ứng số tín chỉ hoàn thành tối thiểu).\n* **Cảnh báo học vụ (Academic Probation):** Áp dụng khi cGPA rơi xuống dưới ngưỡng chuẩn quy định. Sinh viên sẽ nhận được sự hỗ trợ đặc biệt và giám sát chặt chẽ từ Cố vấn học tập (Academic Advisor) để cải thiện điểm số.\n* **Đình chỉ / Buộc thôi học (Academic Suspension/Dismissal):** Áp dụng nếu sinh viên bị cảnh báo học vụ liên tiếp mà không cải thiện được kết quả học tập.\n\n---\n\n### 3. Liêm chính Học thuật (Academic Integrity)\n* VinUni đặt tiêu chuẩn rất cao về tính trung thực trong học tập và nghiên cứu:\n  * Tuyệt đối nghiêm cấm: Đạo văn (Plagiarism), gian lận thi cử (Cheating), làm bài hộ hoặc nhờ người thi/làm bài hộ.\n  * Mọi vi phạm sẽ bị Hội đồng Kỷ luật & Học thuật VinUni xử lý từ mức cảnh cáo, hủy kết quả môn học đến buộc thôi học.\n\n---\n\n### 4. Cố vấn Học tập (Academic Advisor) & Hỗ trợ Sinh viên\n* Mỗi sinh viên được phân công một Cố vấn học thuật đồng hành trong suốt quá trình học để định hướng lộ trình, đăng ký môn học và giải quyết các vướng mắc học vụ.\n* Dịch vụ hỗ trợ kèm cặp (Peer Tutoring) và Văn phòng Học vụ (OAS - Office of Academic Services) luôn sẵn sàng hỗ trợ.\n\n---\n\n📌 **Lưu ý hỗ trợ:**\nNếu bạn cần **tra cứu hồ sơ học vụ cá nhân, bảng điểm, lịch thi** hoặc **đặt lịch hẹn với Cố vấn học tập**, vui lòng cung cấp **Mã sinh viên (Student ID)** (ví dụ: `SV2026001`) để mình hỗ trợ nhé!",
    "latency_ms": 8713.98
  },
  {
    "step": 1,
    "query": "Hãy tra cứu thông tin học vụ của sinh viên SV2026001.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "class": "AI-K4",
        "gpa": 3.85,
        "email": "an.nv@vinuni.edu.vn",
        "status": "Đang học",
        "advisor": "PGS.TS Nguyễn Văn A",
        "exam_schedule": [
          {
            "course": "Machine Learning",
            "date": "20/09/2026",
            "time": "08:00",
            "room": "A201"
          },
          {
            "course": "Data Structures",
            "date": "24/09/2026",
            "time": "13:30",
            "room": "B302"
          }
        ]
      }
    },
    "latency_ms": 4698.77
  },
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [X] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).

- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases offline.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
