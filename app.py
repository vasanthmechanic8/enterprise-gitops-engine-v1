from flask import Flask
import os
import socket

app = Flask(__name__)

@app.get('/')
def home():
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>GitOps Engine</title>
        <style>
            body {{ font-family: Arial, sans-serif; background-color: #f4f6f9; text-align: center; padding-top: 50px; }}
            .card {{ background: white; padding: 30px; border-radius: 10px; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }}
            h1 {{ color: #1a73e8; }}
            .meta {{ color: #5f6368; font-family: monospace; }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 Enterprise GitOps Engine v1.0</h1>
            <p>Status: <strong style="color: green;">HEALTHY</strong></p>
            <hr>
            <p class="meta">Server Pod Name: {socket.gethostname()}</p>
            <p class="meta">Environment Mode: Production</p>
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
