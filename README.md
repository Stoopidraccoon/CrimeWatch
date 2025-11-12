# CrimeWatch
CrimeWatch🕵️ — When silence hides the truth, this app gives it a voice. Report crimes safely, track justice in motion, and help build safer communities.

## 🎭 Prelude — Why this app exists

There are whispers in the city streets — unreported incidents, invisible cries, and cases that dissolve into paperwork.  
**CrimeWatch** is the answer: a digital megaphone for citizens, and a razor-sharp tool for authorities.  
It converts fear into evidence, silence into reports, and confusion into actionable cases.

> **Mission:** Empower citizens to safely report crimes, provide admins/police a clean workflow to act, and build data to prevent future harm.  
> **Vision:** A city where technology shortens the path from report to resolution.

---

## 🌟Features (What it does — like a hero)

- 🧾 **Citizen Reporting** — Submit an incident with title, description, time, tags, and optional photo/video.  
- 📍 **Geo-Tagging** — Attach exact location.  
- 🕵️‍♂️ **Priority & Categorization** — Auto-suggest category (theft, assault, fraud, cyber) and severity.   
- 🔁 **Report Tracking** — Unique case IDs; track status: Submitted → Verified → Investigating → Resolved.  
- 🧾 **Admin Dashboard** — Filter, verify, assign, comment, close cases.  
- 🔔 **Notifications** — Email / in-app alerts on status change.  
- 📊 **Analytics** — Heatmaps, area-wise stats. 
- 🔐 **Security-first** — Encrypted sensitive fields; role-based access (user, admin).

---

## 🎯 User Stories

- *As a worried resident*, I want to report suspicious activity quickly so that help reaches my street.  
- *As a survivor*, I want to submit evidence privately and get a confidential case ID.  
- *As a desk officer*, I want a clear queue of new reports sorted by severity so I can dispatch teams faster.  
- *As a data analyst*, I want aggregated trends so we can prevent repeated incidents.

---

## ⚙️ Functional Requirements

1. **Authentication & Roles**
   - Signup/Login (email + password) and OAuth optional.
   - Roles: `citizen`, `admin`.  
2. **Create Report**
   - Fields: `title`, `description`, `datetime`, `location`, `category`, `severity`, `media[]`, `anonymous(boolean)`.
3. **View / Update Report**
   - Citizens view own reports; admins view all.
   - Status updates with timestamp and actor.
4. **Admin Workflows**
   - Admins can view, verify, and update reports.
5. **Search & Filters**
   - Filter by `date range`, `location`, `category`, `status`.
6. **Notifications**
   -  Users get alerts for updates and status changes
7. **Media Handling**
   - Upload & serve images/videos (with size limits).
8. **Export**
   - Export reports CSV / JSON for offline analysis.

---

## 🧩 Non-Functional Requirements

- **Performance:**  App should load and respond quickly.  
- **Security:** Passwords and sensitive data are encrypted.   
- **Scalability:** System should handle multiple users efficiently  
- **Reliability:** Application uptime of at least 99% .   
- **Usability:** Clean accessible UI design.  
- **Maintainability:** Modular code, tests, and clear API contracts.

---

## 🛠️ Tech Stack

**Frontend:** HTML, CSS, JavaScript *(or React)*  
**Backend:** Python (Flask / Django)  
**Database:** SQLite / PostgreSQL  
**Design & Planning:**  
- [🎨 Figma Prototype](#)  
- [📋 Trello Board](#)
---

## 🧭 Architecture Overview 
┌──────────────────────────────────────────────┐
│                Frontend Layer                │
│        (HTML / CSS / JS / React)             │
│   • Collects user input                      │
│   • Displays case status, analytics, etc.    │
│   • Sends requests to backend APIs           │
└──────────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────┐
│             Backend / API Layer              │
│           (Python Flask / Django)            │
│   • Handles authentication & authorization   │
│   • Validates and processes user data        │
│   • Communicates with database               │
│   • Controls business logic and workflows    │
│   • Generates analytics data for dashboard   │
└──────────────────────────────────────────────┘
                     │
                     ▼
┌──────────────────────────────────────────────┐
│               Database Layer                 │
│                  (MySQL)                     │
│   • Stores users, reports, evidence, logs    │
│   • Ensures data integrity & security        │
│   • Enables filtering, tracking, and stats   │
└──────────────────────────────────────────────┘

## Summary

The architecture of CrimeWatch promotes clarity, modularity, and reliability.
By decoupling the UI, API, and data layers, the system ensures easier maintenance, scalability, and the ability to grow into a fully production-grade civic reporting platform.

