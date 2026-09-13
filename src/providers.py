"""
🔌 MULTI-PROVIDER LLM ADAPTER (Google Gemini, OpenAI & Offline Mock)
Hỗ trợ Native Tool Calling và chuyển đổi linh hoạt qua biến môi trường LLM_PROVIDER.
"""

import os
import sys
import json
import re
from typing import Dict, Any, List
from dotenv import load_dotenv

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

load_dotenv()

class BaseLLMProvider:
    """Interface cơ sở cho các LLM Provider hỗ trợ Native Tool Calling"""
    def generate(self, prompt: str, system_prompt: str = "") -> str:
        raise NotImplementedError

    def generate_with_tools(
        self,
        prompt: str,
        tools_schema: List[Dict[str, Any]],
        system_prompt: str = "",
        history: List[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        raise NotImplementedError


class MockOfflineProvider(BaseLLMProvider):
    """Offline Mock Provider dùng để chạy thử mà không tốn API Key"""
    def __init__(self):
        self.model_name = "Offline-Mock-Model-2026"

    def generate(self, prompt: str, system_prompt: str = "") -> str:
        return f"[Mock Chatbot Response]: Xin chào! Tôi đã nhận được câu hỏi '{prompt}'. (Chế độ Chatbot không có Tool tra cứu dữ liệu thời gian thực)."

    def generate_with_tools(
        self,
        prompt: str,
        tools_schema: List[Dict[str, Any]],
        system_prompt: str = "",
        history: List[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        prompt_lower = prompt.lower()
        history = history or []
        student_match = re.search(r"sv\d{7}", prompt_lower)
        student_id = student_match.group(0).upper() if student_match else "SV2026001"
        tool_history = [entry for entry in history if entry.get("role") == "tool"]
        is_multi_step = "sau đó" in prompt_lower and "đặt lịch" in prompt_lower
        
        # Mô phỏng nhận diện intent gọi Tool
        if is_multi_step and not any(entry.get("tool_name") == "academic_query" for entry in tool_history):
            return {
                "type": "tool_call",
                "tool_name": "academic_query",
                "arguments": {"student_id": student_id},
                "thought": f"Tôi cần tra cứu cố vấn của {student_id} trước khi đặt lịch.",
                "history_entry": {
                    "role": "model",
                    "tool_name": "academic_query",
                    "arguments": {"student_id": student_id}
                }
            }
        elif is_multi_step and not any(entry.get("tool_name") == "schedule_appointment" for entry in tool_history):
            advisor_name = "PGS.TS Nguyễn Văn A"
            for entry in reversed(tool_history):
                result = entry.get("content", {})
                advisor_name = result.get("data", {}).get("advisor", advisor_name)
                break
            return {
                "type": "tool_call",
                "tool_name": "schedule_appointment",
                "arguments": {"student_id": student_id, "datetime_str": "14:00 15/09/2026", "advisor_name": advisor_name},
                "thought": f"Đã tìm thấy cố vấn {advisor_name}. Tôi sẽ tiếp tục đặt lịch.",
                "history_entry": {
                    "role": "model",
                    "tool_name": "schedule_appointment",
                    "arguments": {"student_id": student_id, "datetime_str": "14:00 15/09/2026", "advisor_name": advisor_name}
                }
            }
        elif is_multi_step and any(entry.get("tool_name") == "schedule_appointment" for entry in tool_history):
            booking = tool_history[-1].get("content", {})
            return {
                "type": "text",
                "content": f"[Mock Agent Response]: {booking.get('message', 'Đã hoàn tất đặt lịch tư vấn.')} ",
                "thought": "Đã tra cứu cố vấn và hoàn tất đặt lịch theo yêu cầu."
            }
        elif "đặt lịch" in prompt_lower and student_match:
            return {
                "type": "tool_call",
                "tool_name": "schedule_appointment",
                "arguments": {"student_id": student_id, "datetime_str": "14:00 15/09/2026", "advisor_name": "PGS.TS Nguyễn Văn A"},
                "thought": f"Người dùng yêu cầu đặt lịch hẹn tư vấn cho sinh viên {student_id}. Tôi sẽ gọi tool schedule_appointment.",
                "history_entry": {
                    "role": "model",
                    "tool_name": "schedule_appointment",
                    "arguments": {"student_id": student_id, "datetime_str": "14:00 15/09/2026", "advisor_name": "PGS.TS Nguyễn Văn A"}
                }
            }
        elif (student_match or "tra cứu" in prompt_lower or "lịch thi" in prompt_lower) and not tool_history:
            return {
                "type": "tool_call",
                "tool_name": "academic_query",
                "arguments": {"student_id": student_id},
                "thought": f"Người dùng muốn tra cứu thông tin học vụ hoặc lịch thi của {student_id}. Tôi sẽ gọi tool academic_query.",
                "history_entry": {
                    "role": "model",
                    "tool_name": "academic_query",
                    "arguments": {"student_id": student_id}
                }
            }
        else:
            if tool_history:
                last_result = tool_history[-1].get("content", {})
                if last_result.get("status") == "NOT_FOUND":
                    content = f"[Mock Agent Response]: {last_result.get('message', 'Không tìm thấy dữ liệu sinh viên yêu cầu.')}"
                elif last_result.get("status") == "SUCCESS" and "data" in last_result:
                    data = last_result["data"]
                    content = (
                        f"[Mock Agent Response]: {data.get('full_name', '')} thuộc lớp {data.get('class', '')}, "
                        f"GPA {data.get('gpa', '')}, trạng thái {data.get('status', '')}, "
                        f"cố vấn {data.get('advisor', '')}."
                    )
                else:
                    content = "[Mock Agent Response]: Đã hoàn tất các bước xử lý theo yêu cầu."
            else:
                content = "[Mock Agent Response]: Quy chế học vụ VinUni yêu cầu sinh viên tích lũy tối thiểu 120 tín chỉ và duy trì GPA trên 2.0 để tốt nghiệp."
            return {
                "type": "text",
                "content": content,
                "thought": "Đã nhận đủ Observation cần thiết và có thể trả lời người dùng."
            }


class GeminiProvider(BaseLLMProvider):
    """Google Gemini Provider (Native Tool Calling với Google GenAI SDK)"""
    def __init__(self, api_key: str = None, model: str = None):
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.model_name = model or os.getenv("LLM_MODEL") or "gemini-2.5-flash"

    def generate(self, prompt: str, system_prompt: str = "") -> str:
        if not self.api_key or self.api_key == "your_gemini_api_key_here":
            return "[Gemini Error]: Chưa cấu hình GEMINI_API_KEY trong file .env! Đang sử dụng chế độ Mock."
        try:
            from google import genai
            client = genai.Client(api_key=self.api_key)
            contents = f"{system_prompt}\n\n{prompt}" if system_prompt else prompt
            response = client.models.generate_content(model=self.model_name, contents=contents)
            return response.text
        except Exception as e:
            return f"[Gemini Exception]: {str(e)}"

    def generate_with_tools(
        self,
        prompt: str,
        tools_schema: List[Dict[str, Any]],
        system_prompt: str = "",
        history: List[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        if not self.api_key or self.api_key == "your_gemini_api_key_here":
            print("ℹ️ [Gemini Provider]: Chưa tìm thấy GEMINI_API_KEY hợp lệ. Tự động chuyển sang Mock Offline.")
            return MockOfflineProvider().generate_with_tools(prompt, tools_schema, system_prompt)
        
        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=self.api_key)
            
            # Chuẩn hóa function declarations cho Gemini SDK
            function_declarations = []
            for tool in tools_schema:
                # Bỏ qua các tool schema chưa được định nghĩa hoàn chỉnh
                if not tool.get("name") or not tool.get("parameters"):
                    continue
                function_declarations.append({
                    "name": tool["name"],
                    "description": tool.get("description", ""),
                    "parameters": tool.get("parameters", {})
                })

            config = types.GenerateContentConfig(
                system_instruction=system_prompt if system_prompt else None,
                tools=[{"function_declarations": function_declarations}] if function_declarations else None,
                temperature=0.2
            )

            contents = self._build_contents(prompt, history or [], types)
            response = client.models.generate_content(
                model=self.model_name,
                contents=contents,
                config=config
            )

            # Kiểm tra xem Gemini có trả về Tool Call không
            if response.function_calls:
                call = response.function_calls[0]
                args = dict(call.args) if hasattr(call, 'args') and call.args else {}
                return {
                    "type": "tool_call",
                    "tool_name": call.name,
                    "arguments": args,
                    "thought": f"Gemini quyết định gọi công cụ '{call.name}' với tham số: {json.dumps(args, ensure_ascii=False)}",
                    "history_entry": {
                        "role": "model",
                        "tool_name": call.name,
                        "arguments": args
                    }
                }
            else:
                return {
                    "type": "text",
                    "content": response.text or "",
                    "thought": "Gemini phản hồi trực tiếp bằng văn bản (không cần gọi công cụ)."
                }

        except Exception as e:
            print(f"⚠️ [Gemini API Warning]: Không thể kết nối live API ({str(e)}). Tự động fallback về Mock.")
            return MockOfflineProvider().generate_with_tools(prompt, tools_schema, system_prompt)

    @staticmethod
    def _build_contents(prompt: str, history: List[Dict[str, Any]], types) -> List[Any]:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        for entry in history:
            role = entry.get("role")
            if role == "model":
                contents.append(types.Content(
                    role="model",
                    parts=[types.Part.from_function_call(
                        name=entry["tool_name"],
                        args=entry.get("arguments", {})
                    )]
                ))
            elif role == "tool":
                contents.append(types.Content(
                    role="tool",
                    parts=[types.Part.from_function_response(
                        name=entry["tool_name"],
                        response={"result": entry.get("content", {})}
                    )]
                ))
        return contents


class OpenAIProvider(BaseLLMProvider):
    """OpenAI Provider (Native Tool Calling với OpenAI SDK)"""
    def __init__(self, api_key: str = None, model: str = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model_name = model or os.getenv("LLM_MODEL") or "gpt-4o-mini"

    def generate(self, prompt: str, system_prompt: str = "") -> str:
        if not self.api_key or self.api_key == "your_openai_api_key_here":
            return "[OpenAI Error]: Chưa cấu hình OPENAI_API_KEY trong file .env! Đang sử dụng chế độ Mock."
        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key)
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            response = client.chat.completions.create(model=self.model_name, messages=messages)
            return response.choices[0].message.content or ""
        except Exception as e:
            return f"[OpenAI Exception]: {str(e)}"

    def generate_with_tools(
        self,
        prompt: str,
        tools_schema: List[Dict[str, Any]],
        system_prompt: str = "",
        history: List[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        if not self.api_key or self.api_key == "your_openai_api_key_here":
            print("ℹ️ [OpenAI Provider]: Chưa tìm thấy OPENAI_API_KEY hợp lệ. Tự động chuyển sang Mock Offline.")
            return MockOfflineProvider().generate_with_tools(prompt, tools_schema, system_prompt)

        try:
            from openai import OpenAI
            client = OpenAI(api_key=self.api_key)

            tools = []
            for tool in tools_schema:
                if not tool.get("name"):
                    continue
                tools.append({
                    "type": "function",
                    "function": {
                        "name": tool["name"],
                        "description": tool.get("description", ""),
                        "parameters": tool.get("parameters", {})
                    }
                })

            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})

            response = client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                tools=tools if tools else None,
                tool_choice="auto" if tools else None
            )

            msg = response.choices[0].message
            if msg.tool_calls:
                call = msg.tool_calls[0]
                args = json.loads(call.function.arguments) if call.function.arguments else {}
                return {
                    "type": "tool_call",
                    "tool_name": call.function.name,
                    "arguments": args,
                    "thought": f"OpenAI quyết định gọi công cụ '{call.function.name}' với tham số: {json.dumps(args, ensure_ascii=False)}"
                }
            else:
                return {
                    "type": "text",
                    "content": msg.content or "",
                    "thought": "OpenAI phản hồi trực tiếp bằng văn bản (không cần gọi công cụ)."
                }
        except Exception as e:
            print(f"⚠️ [OpenAI API Warning]: Không thể kết nối live API ({str(e)}). Tự động fallback về Mock.")
            return MockOfflineProvider().generate_with_tools(prompt, tools_schema, system_prompt)


def get_llm_provider() -> BaseLLMProvider:
    """Factory function khởi tạo Provider theo LLM_PROVIDER env variable"""
    provider_type = os.getenv("LLM_PROVIDER", "gemini").lower()
    
    if provider_type == "gemini":
        key = os.getenv("GEMINI_API_KEY")
        if key and key != "your_gemini_api_key_here":
            return GeminiProvider()
        else:
            return MockOfflineProvider()
    elif provider_type == "openai":
        key = os.getenv("OPENAI_API_KEY")
        if key and key != "your_openai_api_key_here":
            return OpenAIProvider()
        else:
            return MockOfflineProvider()
    elif provider_type == "mock":
        return MockOfflineProvider()
    else:
        return MockOfflineProvider()
