# 🚀 SPEEDLINE

SPEEDLINE is a ready-to-use repository that also includes the existing **ScoreBot** project.

## 📁 Structure

```
SPEEDLINE/
├─ src/
│  └─ speedline/
│     ├─ scorebot/        # Your original ScoreBot project code
│     ├─ __init__.py
│     └─ core.py
├─ tests/
│  └─ test_sample.py
├─ config/
│  └─ settings.example.json
├─ .github/
│  └─ workflows/
│     └─ ci.yml
├─ .gitignore
├─ LICENSE
├─ README.md
├─ requirements.txt
└─ main.py
```

## ▶️ Running SPEEDLINE

Default entry point:

```bash
python main.py
```

Your original **ScoreBot** code is inside:

```text
src/speedline/scorebot/
```

You can modify `main.py` or `src/speedline/core.py` to call your ScoreBot logic.

## ✅ GitHub Usage

1. Extract this ZIP.
2. Open a terminal inside the extracted `SPEEDLINE` folder.
3. Run:

```bash
git init
git add .
git commit -m "Initial SPEEDLINE with ScoreBot"
git branch -M main
git remote add origin https://github.com/<YourUserName>/SPEEDLINE.git
git push -u origin main
```

---

## ▶️ How to Run ScoreBot (Flask App)

From the project root (where `main.py` and `run_scorebot.py` are):

```bash
python run_scorebot.py
```

Ye command automatically `src/speedline/scorebot/app.py` run karega
aur tumhara original ScoreBot Flask app start ho jayega
(jaise pehle Replit pe chalta tha).

Agar tum `main.py` se run karna chaho:

```bash
python main.py
```

Isse bhi wohi `run_speedline()` call hoga
jo ScoreBot Flask app start kar deta hai.
