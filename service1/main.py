from fastapi import FastAPI
import logging
import os

app = FastAPI()

# Configuración del logger
log_file = os.getenv('LOG_FILE', '/var/log/fastapi/service.log')
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Root endpoint called S1")
    return {"message": "Hola desde Servicio 1"}

@app.get("/ping")
def ping():
    logger.info("Ping endpoint called")
    return {"message": "pong"}
