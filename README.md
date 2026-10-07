# CONECT: Women in STEM Career & Mentorship Platform

> **IEEE WIE Ideathon (SAMWAD)** Project Submission Prototype  
> **Mission:** Centralized Opportunity Discovery, AI-Driven Eligibility Matching & Verified 1-on-1 Mentorship Network for Women in STEM.

---

## 🛠️ Technologies Used (As Defined in Slide 4)

Strictly aligns with the Technical Approach presented in Slide 4:

1. **Frontend / Client Layer:**
   - **Tailwind CSS & Modern HTML5 / ES6**: Highly responsive, mobile-and-web compatible UI styled with IEEE WIE corporate dark navy (`#0b1e36`) and amber accent accents.
   - **Cross-Platform Readiness**: Designed with mobile viewport responsiveness and Progressive Web App (PWA) guidelines.

2. **Backend & Microservice APIs:**
   - **FastAPI (Python)**: High-performance, asynchronous REST microservices engine for handling user sessions, opportunity retrieval, and mentorship bookings.
   - **Uvicorn ASGI Server**: Production-ready asynchronous server running on port `8000`.

3. **AI Recommendation & Eligibility Matching Engine:**
   - **Multi-Factor Weighted Compatibility Algorithm**:
     - Branch Affinity (30%)
     - CGPA Threshold Compliance (25%)
     - Academic Year Eligibility (20%)
     - Semantic Skill Overlap & Keyword Matching (25%)
   - Real-time re-ranking with detailed breakdown and missing prerequisite alerts.

4. **Data Persistence & Cache Simulation:**
   - Structured JSON-backed relational schema (simulating PostgreSQL) with live state tracking for applications, slots, and peer project posts.

---

## 🚀 How to Run the Prototype

### Option 1: Live Full-Stack FastAPI Server (Recommended)
1. Double-click `run_prototype.bat` or run:
   ```powershell
   & "C:\Program Files\Blender Foundation\Blender 5.2\5.2\python\bin\python.exe" -m uvicorn main:app --host 127.0.0.1 --port 8000
   ```
2. Open your browser and navigate to:
   - **Web App**: [http://localhost:8000](http://localhost:8000)
   - **Interactive API Documentation (Swagger)**: [http://localhost:8000/docs](http://localhost:8000/docs)

### Option 2: Standalone Browser Mode (Zero Setup)
Simply open the `frontend/index.html` file directly in Google Chrome, Microsoft Edge, or any modern web browser. The app includes client-side fallback reactive logic so all interactive features work seamlessly offline.

---

## 🌟 Interactive Features Built into the Prototype

1. **🎯 Personalized Opportunities Hub:**
   - Real-time filters for *Scholarships*, *Internships*, *Fellowships*, and *Research Grants*.
   - Dynamic **AI Match Badges** (e.g., `96% Match`) and **Eligibility Status** (`✅ Eligible` vs. `⚠️ CGPA Restricted`).
   - One-click *Track* and *Apply* actions.

2. **✏️ Dynamic Profile Switcher (Real-time AI Recalculation):**
   - Click the student avatar (`Ananya Sharma - CSE Year 3`) in the top right.
   - Change branch (e.g. from *CSE* to *Mechanical* or *Biotechnology*), adjust CGPA slider, or change academic year.
   - Watch the AI Match engine **instantly re-score and re-rank all opportunities**!

3. **👩‍💼 1-on-1 Mentorship Booking:**
   - Profiles of verified female leaders (Google DeepMind, Microsoft, Adobe, Qualcomm).
   - Interactive scheduling modal with time slot selection, consultation topic, and instant session confirmation.

4. **⏳ Automated Deadline Pipeline:**
   - Multi-stage application status tracker (*Saved* ➔ *In Progress* ➔ *Applied* ➔ *Shortlisted*).
   - Urgency badges (*Urgent*, *Moderate*, *Normal*) and Google Calendar reminder sync.

5. **🤝 Peer Collaboration & Hackathon Teammate Finder:**
   - Post new STEM project ideas and browse peer collaboration requests.

6. **⚡ Live Architecture & API Inspector (Slide 4 Proof):**
   - Live inspection panel showing incoming student profile payload and real FastAPI `/api/match` JSON responses.
