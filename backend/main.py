"""
CONECT: AI-Powered Career Ecosystem & Mentorship Platform for Women in STEM
Backend API Server built with FastAPI & Python
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import List, Optional
import os

app = FastAPI(
    title="CONECT Backend API",
    description="Career Opportunities, Networking & Mentorship Engine for Women in STEM",
    version="1.0.0"
)

# Enable CORS for cross-platform clients (Web & Mobile)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================================
# DATA MODELS
# ==========================================

class StudentProfile(BaseModel):
    student_id: Optional[str] = "std_01"
    name: str = "Ananya Sharma"
    branch: str = "Computer Science & Engineering"
    academic_year: int = 3
    cgpa: float = 8.85
    skills: List[str] = ["Python", "Machine Learning", "FastAPI", "React", "Data Structures"]

class BookingRequest(BaseModel):
    mentor_id: str
    student_name: str
    slot: str
    topic: str
    notes: Optional[str] = ""

class TrackerItem(BaseModel):
    opportunity_id: str
    status: str = "Saved"  # Saved, In Progress, Applied, Shortlisted
    urgency: Optional[str] = "Moderate"

class ProjectPost(BaseModel):
    title: str
    domain: str
    author: str
    description: str
    roles: List[str]

# ==========================================
# IN-MEMORY DATA STORE (SIMULATING POSTGRESQL)
# ==========================================

OPPORTUNITIES = [
    {
        "id": "opp-01",
        "title": "Google Generation Scholarship (APAC)",
        "organization": "Google",
        "category": "Scholarship",
        "description": "Merit-and-diversity scholarship for female students pursuing computer science or related engineering degrees with demonstrated leadership.",
        "requiredBranches": ["Computer Science & Engineering", "Information Technology", "Electronics & Communication"],
        "minCgpa": 8.0,
        "eligibleYears": [1, 2, 3],
        "requiredSkills": ["Python", "Data Structures", "Algorithms"],
        "deadline": "2026-11-15",
        "deadlineText": "Nov 15, 2026 (39 Days Left)",
        "perks": "$2,500 USD Tuition Grant + Google Mentorship Retreat",
        "isGenderSpecific": True,
        "logoBg": "bg-red-50 text-red-600 border-red-200"
    },
    {
        "id": "opp-02",
        "title": "Adobe Women-in-Technology Scholarship",
        "organization": "Adobe Research",
        "category": "Scholarship",
        "description": "Recognizing outstanding female engineering students who excel in computing, software architecture, and technological innovation.",
        "requiredBranches": ["Computer Science & Engineering", "Information Technology", "Artificial Intelligence"],
        "minCgpa": 8.5,
        "eligibleYears": [2, 3],
        "requiredSkills": ["Machine Learning", "Python", "Software Development"],
        "deadline": "2026-10-31",
        "deadlineText": "Oct 31, 2026 (24 Days Left)",
        "perks": "$10,000 USD Grant + Adobe Summer Internship + Mentorship",
        "isGenderSpecific": True,
        "logoBg": "bg-rose-50 text-rose-600 border-rose-200"
    },
    {
        "id": "opp-03",
        "title": "Amazon WoW Mentorship & SDE Internship",
        "organization": "Amazon",
        "category": "Internship",
        "description": "Structured female student development initiative offering technical skill-building, webinars, and fast-track interviews.",
        "requiredBranches": ["Computer Science & Engineering", "Information Technology", "Electronics & Communication", "Electrical Engineering"],
        "minCgpa": 7.0,
        "eligibleYears": [2, 3, 4],
        "requiredSkills": ["Data Structures", "Python", "Java"],
        "deadline": "2026-11-05",
        "deadlineText": "Nov 05, 2026 (29 Days Left)",
        "perks": "Fast-Track SDE Intern Loop + 1-on-1 Mentorship",
        "isGenderSpecific": True,
        "logoBg": "bg-amber-50 text-amber-700 border-amber-200"
    },
    {
        "id": "opp-04",
        "title": "DESIS Ascend Educare Diversity Fellowship",
        "organization": "D. E. Shaw India",
        "category": "Fellowship",
        "description": "Premier educational fellowship for talented female sophomores and pre-final year engineering students.",
        "requiredBranches": ["Computer Science & Engineering", "Information Technology"],
        "minCgpa": 8.0,
        "eligibleYears": [2, 3],
        "requiredSkills": ["Python", "Algorithms", "Problem Solving"],
        "deadline": "2026-11-20",
        "deadlineText": "Nov 20, 2026 (44 Days Left)",
        "perks": "INR 1,50,000 Grant + Executive Mentorship + Direct Interview",
        "isGenderSpecific": True,
        "logoBg": "bg-blue-50 text-blue-600 border-blue-200"
    },
    {
        "id": "opp-05",
        "title": "IEEE Women in Engineering (WIE) Project Grant",
        "organization": "IEEE WIE",
        "category": "Research Grant",
        "description": "Seed funding for female undergraduate research teams building smart technology and engineering solutions.",
        "requiredBranches": ["Computer Science & Engineering", "Electronics & Communication", "Electrical Engineering", "Mechanical Engineering", "Biotechnology"],
        "minCgpa": 7.5,
        "eligibleYears": [1, 2, 3, 4],
        "requiredSkills": ["Prototyping", "Research", "System Design"],
        "deadline": "2026-12-10",
        "deadlineText": "Dec 10, 2026 (64 Days Left)",
        "perks": "$1,000 Project Seed Grant + IEEE Conference Publication Support",
        "isGenderSpecific": True,
        "logoBg": "bg-purple-50 text-purple-700 border-purple-200"
    },
    {
        "id": "opp-06",
        "title": "CERN Summer Student Research Programme",
        "organization": "CERN (Switzerland)",
        "category": "Fellowship",
        "description": "Join day-to-day experimental physics, advanced engineering, and computing teams in Geneva for 8-13 weeks.",
        "requiredBranches": ["Computer Science & Engineering", "Electronics & Communication", "Mechanical Engineering"],
        "minCgpa": 8.5,
        "eligibleYears": [3, 4],
        "requiredSkills": ["Python", "C++", "Data Analysis"],
        "deadline": "2026-11-28",
        "deadlineText": "Nov 28, 2026 (52 Days Left)",
        "perks": "Full Swiss Living Allowance + International Lab Access",
        "isGenderSpecific": False,
        "logoBg": "bg-emerald-50 text-emerald-700 border-emerald-200"
    }
]

MENTORS = [
    {
        "id": "men-01",
        "name": "Dr. Radhika Sen",
        "title": "Principal Research Scientist",
        "company": "Google DeepMind",
        "domain": "Artificial Intelligence & NLP",
        "exp": "9 yrs",
        "rating": 4.95,
        "sessions": 68,
        "slots": ["Fri 6:00 PM IST", "Sat 11:00 AM IST", "Sun 4:00 PM IST"],
        "avatarBg": "bg-indigo-600",
        "bio": "Specializes in helping female students break into tier-1 AI research labs and win competitive fellowships."
    },
    {
        "id": "men-02",
        "name": "Pooja Kulkarni",
        "title": "Senior Software Engineer",
        "company": "Microsoft Azure",
        "domain": "Distributed Systems & Cloud",
        "exp": "6 yrs",
        "rating": 4.90,
        "sessions": 52,
        "slots": ["Thu 7:30 PM IST", "Sat 2:00 PM IST"],
        "avatarBg": "bg-teal-600",
        "bio": "Former IEEE WIE chair; specializes in system design interview prep, resume roast, and tech hiring."
    },
    {
        "id": "men-03",
        "name": "Anupriya Ghosh",
        "title": "Director of Product",
        "company": "Adobe India",
        "domain": "Product & Tech Leadership",
        "exp": "11 yrs",
        "rating": 4.98,
        "sessions": 89,
        "slots": ["Wed 8:00 PM IST", "Sun 10:00 AM IST"],
        "avatarBg": "bg-amber-600",
        "bio": "Empowering women in engineering to transition into high-impact product management and international scholarships."
    },
    {
        "id": "men-04",
        "name": "Suhani Verma",
        "title": "Hardware Systems Architect",
        "company": "Qualcomm / ISRO Collaborator",
        "domain": "VLSI & Embedded Systems",
        "exp": "7 yrs",
        "rating": 4.88,
        "sessions": 41,
        "slots": ["Sat 5:00 PM IST", "Sun 6:00 PM IST"],
        "avatarBg": "bg-rose-600",
        "bio": "Guiding female electrical and ECE students through core engineering roles, semiconductor internships, and thesis proposals."
    }
]

TRACKER_DATA = [
    {"id": "opp-02", "status": "In Progress", "urgency": "Urgent"},
    {"id": "opp-03", "status": "Saved", "urgency": "Moderate"},
    {"id": "opp-01", "status": "Saved", "urgency": "Moderate"},
    {"id": "opp-04", "status": "Saved", "urgency": "Normal"}
]

COMMUNITY_PROJECTS = [
    {
        "id": "proj-01",
        "title": "EcoSense: IoT + ML for Clean Water Monitoring in Rural Schools",
        "author": "Kavya Nair (3rd Year CSE, MANIT)",
        "domain": "IoT & Machine Learning",
        "description": "Developing low-cost water quality telemetry nodes for local community schools. Need a teammate skilled in embedded firmware (ESP32) and dashboard UI.",
        "roles": ["Embedded Systems (ECE)", "React/Tailwind Frontend"],
        "time": "2 hours ago"
    },
    {
        "id": "proj-02",
        "title": "Smart Braille Pad - IEEE WIE Student Hackathon Team",
        "author": "Meera Iyer (2nd Year ECE, NIT Trichy)",
        "domain": "Assistive Technology & Hardware",
        "description": "Preparing our prototype submission for the upcoming national WIE Hackathon. Seeking a fellow woman engineer to co-lead the PCB design and documentation.",
        "roles": ["Hardware/KiCAD Designer", "Python/Backend Developer"],
        "time": "Yesterday"
    }
]

BOOKED_SESSIONS = []

# ==========================================
# AI RECOMMENDATION & MATCHING ENGINE
# ==========================================

def compute_match(profile: StudentProfile, opp: dict):
    """
    NLP & Multi-factor Weighted Compatibility Matcher:
    - Branch affinity (30%)
    - CGPA compliance (25%)
    - Year eligibility (20%)
    - Semantic skill overlap (25%)
    """
    # 1. Branch match (30%)
    branch_match = profile.branch in opp["requiredBranches"]
    branch_score = 30 if branch_match else 10

    # 2. CGPA check (25%)
    cgpa_eligible = profile.cgpa >= opp["minCgpa"]
    if cgpa_eligible:
        cgpa_score = 25
    else:
        diff = opp["minCgpa"] - profile.cgpa
        cgpa_score = max(0, int(25 - (diff * 20)))

    # 3. Year check (20%)
    year_eligible = profile.academic_year in opp["eligibleYears"]
    year_score = 20 if year_eligible else 5

    # 4. Skill overlap (25%)
    p_skills = [s.lower().strip() for s in profile.skills]
    o_skills = [s.lower().strip() for s in opp["requiredSkills"]]
    matched = [s for s in o_skills if any(ps in s or s in ps for ps in p_skills)]
    skill_score = int((len(matched) / max(1, len(o_skills))) * 25)

    total_score = min(98, branch_score + cgpa_score + year_score + skill_score)
    is_eligible = branch_match and cgpa_eligible and year_eligible

    return {
        "opportunity_id": opp["id"],
        "title": opp["title"],
        "organization": opp["organization"],
        "category": opp["category"],
        "match_score": total_score,
        "is_eligible": is_eligible,
        "breakdown": {
            "branch_affinity_score": branch_score,
            "branch_matched": branch_match,
            "cgpa_compliance_score": cgpa_score,
            "cgpa_eligible": cgpa_eligible,
            "year_compliance_score": year_score,
            "year_eligible": year_eligible,
            "skill_overlap_score": skill_score,
            "matched_skills": matched
        }
    }

# ==========================================
# API ROUTERS
# ==========================================

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "CONECT Microservice API",
        "engine": "FastAPI + NLP Matcher"
    }

@app.get("/api/opportunities")
def get_opportunities(category: Optional[str] = None):
    if category and category.lower() != "all":
        return [o for o in OPPORTUNITIES if o["category"].lower() == category.lower()]
    return OPPORTUNITIES

@app.post("/api/match")
def match_opportunities(profile: StudentProfile):
    """
    AI Match Engine Endpoint: Accepts Student Profile and returns
    reranked opportunities with compatibility score and eligibility breakdowns.
    """
    results = []
    for opp in OPPORTUNITIES:
        match_info = compute_match(profile, opp)
        results.append({
            **opp,
            "ai_match": match_info
        })
    # Sort descending by match score
    results.sort(key=lambda x: x["ai_match"]["match_score"], reverse=True)
    return {
        "student": profile.model_dump(),
        "total_evaluated": len(results),
        "eligible_count": sum(1 for r in results if r["ai_match"]["is_eligible"]),
        "ranked_matches": results
    }

@app.get("/api/mentors")
def get_mentors():
    return MENTORS

@app.post("/api/mentors/book")
def book_mentor_session(req: BookingRequest):
    mentor = next((m for m in MENTORS if m["id"] == req.mentor_id), None)
    if not mentor:
        raise HTTPException(status_code=404, detail="Mentor not found")
    
    session = {
        "booking_id": f"sess_{len(BOOKED_SESSIONS) + 1}",
        "mentor_name": mentor["name"],
        "mentor_company": mentor["company"],
        "student_name": req.student_name,
        "slot": req.slot,
        "topic": req.topic,
        "status": "Confirmed",
        "meeting_link": f"https://meet.conect-stem.org/room/{mentor['id']}-{len(BOOKED_SESSIONS)+1}"
    }
    BOOKED_SESSIONS.append(session)
    return {
        "message": "Mentorship session confirmed successfully!",
        "session": session
    }

@app.get("/api/tracker")
def get_tracker():
    return TRACKER_DATA

@app.post("/api/tracker")
def update_tracker(item: TrackerItem):
    existing = next((t for t in TRACKER_DATA if t["id"] == item.opportunity_id), None)
    if existing:
        existing["status"] = item.status
        if item.urgency:
            existing["urgency"] = item.urgency
    else:
        TRACKER_DATA.append({
            "id": item.opportunity_id,
            "status": item.status,
            "urgency": item.urgency or "Moderate"
        })
    return {"message": "Tracker updated successfully", "tracker": TRACKER_DATA}

@app.get("/api/community")
def get_community_projects():
    return COMMUNITY_PROJECTS

@app.post("/api/community")
def create_community_project(post: ProjectPost):
    new_proj = {
        "id": f"proj-{len(COMMUNITY_PROJECTS) + 1}",
        "title": post.title,
        "domain": post.domain,
        "author": post.author,
        "description": post.description,
        "roles": post.roles,
        "time": "Just now"
    }
    COMMUNITY_PROJECTS.insert(0, new_proj)
    return {"message": "Project published to CONECT network", "project": new_proj}

# Mount static frontend files if folder exists
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
