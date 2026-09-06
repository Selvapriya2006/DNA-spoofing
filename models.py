<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Login - Cyber Secure Chat</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
  <style>
    body { background: #0d0d0d; color: #00ffcc; font-family: 'Courier New', monospace; }
    .card { background: #1a1a1a; border: 2px solid #00ffcc; border-radius: 14px; box-shadow: 0 0 30px #00ffcc44; }
    .card-fixed { width: 380px; }
    .heading-muted { color: #00ffcc88; }
    .alert-custom { background:#1a0000; border-color:#ff4444; color:#ff4444; }
    .form-control { background: #0d0d0d; border: 1px solid #00ffcc44; color: #00ffcc; }
    .form-control:focus { background: #0d0d0d; border-color: #00ffcc; color: #00ffcc; box-shadow: 0 0 8px #00ffcc44; }
    .form-control::placeholder { color: #00ffcc44; }
    .btn-cyber { background: linear-gradient(135deg, #00ffcc, #00ccff); color: #0d0d0d; font-weight: bold; border: none; }
    .btn-cyber:hover { background: linear-gradient(135deg, #00ccff, #00ffcc); box-shadow: 0 0 15px #00ffcc88; }
    .glow { text-shadow: 0 0 10px #00ffcc; }
    a { color: #00ffcc; }
    a:hover { color: #00ccff; }
  </style>
</head>
<body class="d-flex justify-content-center align-items-center vh-100">
  <div class="card p-4 card-fixed">
    <h3 class="text-center mb-4 glow">🔐 Cyber Secure Chat</h3>
    <h5 class="text-center mb-4 heading-muted">Login</h5>

    {% if error %}
    <div class="alert alert-danger alert-custom">
      {{ error }}
    </div>
    {% endif %}

    <form method="POST">
      {% csrf_token %}
      <div class="mb-3">
        <label class="form-label">Username</label>
        <input type="text" name="username" class="form-control" placeholder="Enter username" required>
      </div>
      <div class="mb-3">
        <label class="form-label">Password</label>
        <input type="password" name="password" class="form-control" placeholder="Enter password" required>
      </div>
      <button type="submit" class="btn btn-cyber w-100 mb-3">⚡ Login</button>
    </form>
    <p class="text-center mb-0">Don't have an account? <a href="/signup/">Sign Up</a></p>
  </div>
</body>
</html>
