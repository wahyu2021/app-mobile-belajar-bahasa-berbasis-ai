from .main import celery_app
# Impor shared services di sini jika worker membutuhkannya di masa depan
# from shared.ai import stt_service

@celery_app.task(name="process_some_task")
def process_some_task(data: dict) -> dict:
    print(f"Worker received task with data: {data}")
    # Logika worker akan ditambahkan di sini
    return {"status": "completed", "result": "some_value"}