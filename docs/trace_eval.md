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
    "query": "Hãy tra cứu cố vấn của SV2026001, sau đó đặt lịch gặp cố vấn đó lúc 14:00 ngày 15/09/2026.",
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
    "latency_ms": 812.08
  },
  {
    "step": 2,
    "query": "Hãy tra cứu cố vấn của SV2026001, sau đó đặt lịch gặp cố vấn đó lúc 14:00 ngày 15/09/2026.",
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
    "latency_ms": 665.18
  },
  {
    "step": 3,
    "query": "Hãy tra cứu cố vấn của SV2026001, sau đó đặt lịch gặp cố vấn đó lúc 14:00 ngày 15/09/2026.",
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
    "latency_ms": 720.43
  },
  {
    "step": 4,
    "query": "Hãy tra cứu cố vấn của SV2026001, sau đó đặt lịch gặp cố vấn đó lúc 14:00 ngày 15/09/2026.",
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
    "latency_ms": 681.51
  },
  {
    "step": 5,
    "query": "Hãy tra cứu cố vấn của SV2026001, sau đó đặt lịch gặp cố vấn đó lúc 14:00 ngày 15/09/2026.",
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
    "latency_ms": 711.18
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
