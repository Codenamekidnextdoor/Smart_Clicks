# SmartClick Troubleshooting Guide 🔧

## Common Issues & Solutions

### Backend Issues

#### Issue 1: `ModuleNotFoundError: No module named 'uvicorn'`

**Solution:**
```bash
cd backend
pip install -r requirements.txt
```

#### Issue 2: `ERROR: No matching distribution found for pywin32==306`

**Solution:** Updated to pywin32==311 in requirements.txt. Run:
```bash
cd backend
pip install -r requirements.txt
```

#### Issue 3: Backend won't start

**Check:**
1. Are you in the backend directory? `cd backend`
2. Is virtual environment activated? `source .venv/bin/activate` (Linux/Mac) or `.venv\Scripts\activate` (Windows)
3. Are dependencies installed? `pip install -r requirements.txt`
4. Is port 8000 already in use? Try `python run.py` or change port in `run.py`

#### Issue 4: Database errors

**Solution:** The database will be created automatically at:
- Windows: `C:\Users\{username}\.smartclick\smartclick.db`
- Linux/Mac: `~/.smartclick/smartclick.db`

If issues persist, delete the database file and restart.

---

### Frontend Issues

#### Issue 1: `npm install` fails

**Solution:**
```bash
cd frontend
rm -rf node_modules package-lock.json  # or delete manually on Windows
npm install
```

#### Issue 2: TypeScript errors

**Solution:** These are expected until we build the components. The foundation is ready, components are next phase.

#### Issue 3: `npm run dev` shows default Vite page

**Expected behavior!** We haven't built the React components yet. This is Phase 3 (next).

---

### Installation Steps (Clean Install)

#### Backend
```bash
# 1. Navigate to backend
cd backend

# 2. Create virtual environment (optional but recommended)
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run backend
python run.py
```

#### Frontend
```bash
# 1. Navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Run dev server (when components are ready)
npm run dev
```

---

### Verification Checklist

#### Backend ✅
- [ ] Dependencies installed without errors
- [ ] `python run.py` starts server
- [ ] Can access http://127.0.0.1:8000
- [ ] Can access http://127.0.0.1:8000/docs
- [ ] Health check returns status: "healthy"

#### Frontend ✅
- [ ] Dependencies installed without errors
- [ ] `npm run dev` starts dev server
- [ ] Can access http://localhost:5173
- [ ] No console errors (TypeScript warnings are OK for now)

---

### Port Conflicts

#### Backend (Port 8000)

If port 8000 is in use, edit `backend/run.py`:
```python
uvicorn.run(
    "api.main:app",
    host="127.0.0.1",
    port=8001,  # Change this
    reload=True,
    log_level="info"
)
```

Then update `frontend/.env`:
```
VITE_API_URL=http://127.0.0.1:8001
```

#### Frontend (Port 5173)

Vite will automatically use the next available port if 5173 is taken.

---

### Environment Variables

#### Backend
No environment variables required for basic operation. The app uses:
- SQLite database (created automatically)
- Mock AI client (if watsonx credentials not configured)

#### Frontend
Create `frontend/.env` from `frontend/.env.example`:
```bash
cd frontend
cp .env.example .env
```

Edit if needed:
```
VITE_API_URL=http://127.0.0.1:8000
VITE_WS_URL=ws://127.0.0.1:8000
```

---

### Python Version

**Required:** Python 3.8+

**Check version:**
```bash
python --version
```

**If too old:**
- Download from https://www.python.org/downloads/
- Or use pyenv: `pyenv install 3.11`

---

### Node Version

**Required:** Node 16+

**Check version:**
```bash
node --version
npm --version
```

**If too old:**
- Download from https://nodejs.org/
- Or use nvm: `nvm install 20`

---

### Windows-Specific Issues

#### Issue: PowerShell execution policy

**Error:** `cannot be loaded because running scripts is disabled`

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### Issue: Long path names

**Error:** `The filename or extension is too long`

**Solution:**
1. Enable long paths in Windows
2. Or move project closer to root: `C:\SmartClick`

---

### macOS-Specific Issues

#### Issue: Permission denied

**Solution:**
```bash
chmod +x backend/run.py
```

#### Issue: SSL certificate errors

**Solution:**
```bash
pip install --upgrade certifi
```

---

### Linux-Specific Issues

#### Issue: Missing system dependencies

**Solution (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3-dev python3-pip nodejs npm
```

**Solution (Fedora/RHEL):**
```bash
sudo dnf install python3-devel python3-pip nodejs npm
```

---

### Getting Help

#### Check Logs

**Backend logs:**
- Console output when running `python run.py`
- Look for ERROR or WARNING messages

**Frontend logs:**
- Browser console (F12)
- Terminal output when running `npm run dev`

#### Common Log Messages

**"Address already in use"**
- Port conflict, change port or kill process

**"Module not found"**
- Missing dependency, run `pip install` or `npm install`

**"Connection refused"**
- Backend not running, start with `python run.py`

---

### Still Having Issues?

1. **Check the documentation:**
   - `FOUNDATION_REVIEW.md` - What's built and how to test
   - `MODERNIZATION_README.md` - Quick start guide
   - `PHASE_2_COMPLETE.md` - Phase summary

2. **Verify installation:**
   - Backend: `cd backend && pip list`
   - Frontend: `cd frontend && npm list`

3. **Clean install:**
   - Backend: Delete `venv`, recreate, reinstall
   - Frontend: Delete `node_modules`, reinstall

4. **Check versions:**
   - Python 3.8+
   - Node 16+
   - pip latest
   - npm latest

---

### Quick Reference

#### Start Backend
```bash
cd backend
python run.py
```

#### Start Frontend (when ready)
```bash
cd frontend
npm run dev
```

#### Test Backend
```bash
curl http://127.0.0.1:8000/health
```

#### View API Docs
```
http://127.0.0.1:8000/docs
```

---

**Most issues are solved by:**
1. Ensuring you're in the correct directory
2. Installing/reinstalling dependencies
3. Checking Python/Node versions
4. Restarting the servers

Good luck! 🚀