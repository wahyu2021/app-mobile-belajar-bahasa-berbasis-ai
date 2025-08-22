# /shared/ai/llm_service.py

import os
import google.generativeai as genai

# Konfigurasi API key dari environment variable
try:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Error configuring Google AI: {e}")
    model = None

async def generate_narrative_feedback(mistakes: list) -> str:
    """
    Membuat prompt dan memanggil Gemini untuk mendapatkan feedback naratif.
    """
    if not model:
        return "Terus berlatih, kamu pasti bisa! (Error: AI model not configured)"

    # Prompt-guard: Menginstruksikan AI agar outputnya sesuai format
    mistake_summary = ", ".join([f"salah menulis '{m['token']}' menjadi '{m['user_input']}' (seharusnya '{m['target']}')" for m in mistakes])
    
    prompt = f"""
    Anda adalah seorang pelatih bahasa yang ramah dan suportif untuk sebuah game puzzle bahasa.
    Seorang pemain baru saja menyelesaikan level dan membuat kesalahan berikut: {mistake_summary}.

    Tugas Anda:
    Berikan umpan balik (feedback) yang SANGAT SINGKAT (cukup satu kalimat), positif, dan bilingual (Indonesia & Inggris).
    Fokus hanya pada kesalahan yang dibuat. Jangan terlalu panjang.

    Contoh output yang baik:
    - Penulisan '犬' sudah hampir benar, perhatikan lagi hiragana-nya ya! (Your spelling for '犬' is almost there, check the hiragana again!)
    - Kerja bagus! Sedikit lagi untuk partikel 'を', terus berlatih! (Great work! Just a little more practice on the 'を' particle!)

    Feedback untuk pemain:
    """

    try:
        response = await model.generate_content_async(prompt)
        ai_feedback = response.text.strip()
    except Exception as e:
        print(f"Error calling LLM API: {e}")
        ai_feedback = "Kerja bagus! Teruslah berlatih!" # Fallback jika API error

    return ai_feedback