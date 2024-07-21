"""
Módulo de aplicação WEB Flask
"""
import os
from flask import Flask
from core.logs.logger import setup_logger

logger = setup_logger(__name__)

app = Flask(__name__)
