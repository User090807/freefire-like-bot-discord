import json
import os
from datetime import datetime

# Arquivo de jobs em memória
JOBS = {}

def list_jobs():
    return list(JOBS.values())

async def enqueue_like_job(uid, count, region):
    """Agenda uma tarefa de like"""
    job_id = f"job_{len(JOBS)+1}"
    job = {
        "job_id": job_id,
        "uid": str(uid),
        "count": int(count),
        "region": str(region).upper(),
        "status": "queued",
        "created_at": datetime.now().isoformat()
    }
    JOBS[job_id] = job
    return job

async def simulate_job_progress(job_id):
    """Simula progresso do job"""
    if job_id in JOBS:
        JOBS[job_id]["status"] = "processing"
        # Simula processamento
        import asyncio
        await asyncio.sleep(0.5)
        JOBS[job_id]["status"] = "completed"
        return "completed"
    return "not_found"

def get_job_status(job_id):
    """Retorna status de um job"""
    if job_id in JOBS:
        return JOBS[job_id]
    return None
