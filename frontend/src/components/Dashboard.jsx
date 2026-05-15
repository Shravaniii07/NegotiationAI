import "./Dashboard.css";

export default function Dashboard({ data, mode }) {

    if (!data) return (
        <div className="dashboard-placeholder">
            <p>Start negotiating to see live {mode === 'dojo' ? 'performance scoring' : 'procurement insights'}</p>
        </div>
    );

    const { scorecard, strategy, personality, vendor_list, draft_emails } = data;

    return (
        <div className="dashboard-container">
            <h3 className="dashboard-title">
                {mode === "dojo" ? "🥋 Performance Scorecard" : "🔍 Procurement Insights"}
            </h3>
            
            <div className="stats-grid">
                {mode === "dojo" && scorecard && (
                    <>
                        <div className="stat-card score-card">
                            <span className="stat-label">Tactics</span>
                            <div className="score-ring">{scorecard.tactics_score}%</div>
                        </div>
                        <div className="stat-card score-card">
                            <span className="stat-label">Resilience</span>
                            <div className="score-ring">{scorecard.resilience_score}%</div>
                        </div>
                        <div className="stat-card feedback-card">
                            <span className="stat-label">AI Coach Feedback</span>
                            <p className="feedback-text">{scorecard.feedback}</p>
                        </div>
                    </>
                )}

                {mode === "procurement" && vendor_list && vendor_list.length > 0 && (
                    <div className="stat-card research-card">
                        <span className="stat-label">Vendor Comparison</span>
                        <table className="vendor-table">
                            <thead>
                                <tr>
                                    <th>Vendor</th>
                                    <th>Price</th>
                                    <th>Pros</th>
                                </tr>
                            </thead>
                            <tbody>
                                {vendor_list.map((v, i) => (
                                    <tr key={i}>
                                        <td>{v.name}</td>
                                        <td>{v.price_estimate}</td>
                                        <td>{v.pros}</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                )}

                {mode === "procurement" && draft_emails && draft_emails.length > 0 && (
                    <div className="stat-card email-card">
                        <span className="stat-label">Draft Outreach Emails</span>
                        {draft_emails.map((d, i) => (
                            <div key={i} className="draft-item">
                                <strong>To: {d.vendor}</strong>
                                <pre className="email-preview">{d.email}</pre>
                            </div>
                        ))}
                    </div>
                )}

                <div className="stat-card">
                    <span className="stat-label">Detected Tactic</span>
                    <span className="stat-value">{strategy}</span>
                </div>
                
                <div className="stat-card">
                    <span className="stat-label">Your Persona</span>
                    <span className="stat-value">{personality}</span>
                </div>
            </div>
        </div>
    );
}