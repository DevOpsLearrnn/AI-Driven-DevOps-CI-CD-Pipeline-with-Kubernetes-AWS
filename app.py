from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
      <head>
        <style>
          body {
            background-color: #f9fafb;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #1f2937;
            padding: 40px;
          }
          .container {
            background-color: #ffffff;
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.08);
            max-width: 750px;
            margin: auto;
          }
          h1 {
            color: #3b82f6;
            margin-bottom: 16px;
          }
          ul {
            margin: 0;
            padding-left: 20px;
          }
          footer {
            margin-top: 30px;
            font-size: 14px;
            color: #6b7280;
            border-top: 1px solid #e5e7eb;
            padding-top: 15px;
          }
          a {
            color: #2563eb;
            text-decoration: none;
          }
        </style>
      </head>
      <body>
        <div class="container">
          <h1>🚀 FastAPI CI/CD Pipeline Deployed Successfully!</h1>
          <p>This project demonstrates a robust CI/CD pipeline using modern DevOps tools:</p>
          <ul>
            <li>⚙️ Jenkins for Continuous Integration</li>
            <li>🐳 Docker for Containerization</li>
            <li>🔗 GitHub for Version Control</li>
            <li>☁️ AWS EC2 for Cloud Deployment</li>
          </ul>
          <p>✨ Code to Deployment is 100% automated. Built with best practices in DevOps engineering.</p>
          <footer>
            👨‍💻 GitHub: <a href="https://github.com/DevOpsLearrnn" target="_blank">DevOpsLearrnn</a> |
            🔗 LinkedIn: <a href="https://www.linkedin.com/in/mdafr273" target="_blank">mdafr273</a>
          </footer>
        </div>
      </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000)
