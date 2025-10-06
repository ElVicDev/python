""" Día 79: automatizar correos electrónicos
Automatice el envío de correos electrónicos con Python. """

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from getpass import getpass
from datetime import datetime
import schedule
import time
import logging
import sys
from dotenv import load_dotenv
from pathlib import Path
from email.utils import formataddr
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.nonmultipart import MIMENonMultipart
import mimetypes
import re
import ssl
import traceback
import json
import csv
import base64
import quopri
import urllib.parse
import urllib.request
import email.utils
import email.policy
import email.generator
import email.iterators
import email.headerregistry
import email.charset
import email.errors
import email.contentmanager
import email.message
import email.parser
import email.utils
import email.encoders
import email.mime
import email.mime.text
import email.mime.multipart
import email.mime.base
import email.mime.image
import email.mime.audio
import email.mime.nonmultipart
import email.mime.application

# Cargar variables de entorno desde un archivo .env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
SMTP_PORT = int(os.getenv('SMTP_PORT', 587))
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')
SUBJECT = os.getenv('EMAIL_SUBJECT', 'Correo Automatizado')
BODY = os.getenv('EMAIL_BODY', 'Este es un correo electrónico enviado automáticamente por un script de Python.')
ATTACHMENT_PATH = os.getenv('ATTACHMENT_PATH', None)
LOG_FILE = os.getenv('LOG_FILE', 'email_automation.log')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()
SCHEDULE_TIME = os.getenv('SCHEDULE_TIME', '09:00')
RETRY_COUNT = int(os.getenv('RETRY_COUNT', 3))
RETRY_DELAY = int(os.getenv('RETRY_DELAY', 5))  # segundos
USE_TLS = os.getenv('USE_TLS', 'True').lower() in ('true', '1', 't')
USE_SSL = os.getenv('USE_SSL', 'False').lower() in ('true', '1', 't')
CHARSET = os.getenv('CHARSET', 'utf-8')
ENCODING = os.getenv('ENCODING', 'base64')
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=LOG_FORMAT)
logger = logging.getLogger()
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(LOG_LEVEL)
console_handler.setFormatter(logging.Formatter(LOG_FORMAT))
logger.addHandler(console_handler)
logger.propagate = False
context = ssl.create_default_context()
if USE_SSL:
    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context)
else:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
if USE_TLS and not USE_SSL:
    server.starttls(context=context)
def send_email():
    for attempt in range(RETRY_COUNT):
        try:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            msg = MIMEMultipart()
            msg['From'] = formataddr((str(Header('Automatizador', CHARSET)), EMAIL_ADDRESS))
            msg['To'] = RECIPIENT_EMAIL
            msg['Subject'] = Header(SUBJECT, CHARSET)
            msg.attach(MIMEText(BODY, 'plain', CHARSET))
            if ATTACHMENT_PATH and os.path.isfile(ATTACHMENT_PATH):
                with open(ATTACHMENT_PATH, 'rb') as attachment:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(ATTACHMENT_PATH)}')
                msg.attach(part)
            server.send_message(msg)
            logger.info(f"Correo enviado a {RECIPIENT_EMAIL}")
            break
        except Exception as e:
            logger.error(f"Error al enviar el correo: {e}")
            if attempt < RETRY_COUNT - 1:
                logger.info(f"Reintentando en {RETRY_DELAY} segundos...")
                time.sleep(RETRY_DELAY)
            else:
                logger.error("Número máximo de reintentos alcanzado. No se pudo enviar el correo.")

def job():
    logger.info("Iniciando tarea programada para enviar correo electrónico.")
    send_email()
    logger.info("Tarea programada completada.")
schedule.every().day.at(SCHEDULE_TIME).do(job)
logger.info(f"Programación configurada para enviar correo todos los días a las {SCHEDULE_TIME}.")
while True:
    schedule.run_pending()
    time.sleep(60)

# Output:
# Al ejecutar el script, se enviará un correo electrónico
# automáticamente a la dirección especificada en las variables de entorno.
# Asegúrese de configurar correctamente las variables de entorno
# en un archivo .env o en su entorno de ejecución.