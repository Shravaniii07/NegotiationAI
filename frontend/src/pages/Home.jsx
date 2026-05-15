import { useState } from "react";
import ChatBox from "../components/ChatBox";
import Dashboard from "../components/Dashboard";
import "./Home.css";

export default function Home() {
    const [lastData, setLastData] = useState(null);
    const [mode, setMode] = useState("dojo");
    const [persona, setPersona] = useState("skeptical");

    return (
        <div className="home-wrapper">
            <header className="home-header">
                <h1 className="main-title">Negotiation Dojo & Procurement Hub</h1>
                <p className="subtitle">Practice your sales skills or automate your procurement with AI</p>
                
                <div className="mode-selector">
                    <button 
                        className={mode === "dojo" ? "active" : ""} 
                        onClick={() => { setMode("dojo"); setLastData(null); }}
                    >
                        🎓 Sales Dojo
                    </button>
                    <button 
                        className={mode === "procurement" ? "active" : ""} 
                        onClick={() => { setMode("procurement"); setLastData(null); }}
                    >
                        📦 Auto-Procurement
                    </button>
                </div>
            </header>

            <main className="home-content">
                <div className="chat-section">
                    <div className="persona-banner">
                        <span className="mode-badge">
                            {mode === "dojo" ? "🎓 Dojo Mode" : "📦 Procurement"}
                        </span>
                        <span>Persona: <strong>{persona}</strong></span>
                    </div>
                    <ChatBox setLastData={setLastData} mode={mode} persona={persona} />
                </div>
                
                <aside className="dashboard-section">
                    <Dashboard data={lastData} mode={mode} />
                </aside>
            </main>

            <footer className="home-footer">
                <p>© 2026 Sales Dojo AI • Powered by Groq & LangGraph</p>
            </footer>
        </div>
    );
}