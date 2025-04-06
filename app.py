from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
      <head>
        <style>
          body {
            background-color: #f0f4f8;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #1f2937;
            padding: 30px;
            line-height: 1.6;
          }
          .container {
            background-color: #ffffff;
            border-radius: 12px;
            padding: 25px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            max-width: 700px;
            margin: auto;
          }
          h1 {
            color: #3b82f6;
            margin-bottom: 10px;
          }
          ul {
            margin: 0;
            padding-left: 20px;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>🚀 FastAPI CI/CD Project Deployed</h1>
          <p>This project demonstrates a professional CI/CD pipeline setup using:</p>
          <ul>
            <li>✅ Jenkins for Continuous Integration</li>
            <li>🐳 Docker for Containerization</li>
            <li>📦 GitHub for Source Control</li>
            <li>☁️ AWS EC2 for Deployment</li>
          </ul>
          <p>Everything is automated from code commit to deployment, ensuring a streamlined DevOps workflow. Ready for scale!</p>
        </div>
      </body>
    </html>
    """
