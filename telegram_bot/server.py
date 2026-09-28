"""
server.py
─────────
Background Flask HTTP server for Render/Railway port binding and uptime health checks.
"""

import os
import logging
import threading
from flask import Flask, jsonify

logger = logging.getLogger("server")
app = Flask(__name__)

@app.route("/", methods=["GET", "HEAD"])
@app.route("/health", methods=["GET", "HEAD"])
def health():
    return jsonify({
        "status": "healthy",
        "service": "CAT 2026 Daily Master Mentor Bot",
        "mode": "cloud_active"
    }), 200

def start_server():
    port = int(os.getenv("PORT", 8080))
    logger.info("Starting background health-check server on port %d...", port)
    # Run in daemon thread
    thread = threading.Thread(
        target=lambda: app.run(host="0.0.0.0", port=port, use_reloader=False),
        daemon=True
    )
    thread.start()