from services.groq_service import call_llm
import json

def analyze(state):
    mode = state.get("mode", "dojo")
    
    # 1. General Analysis
    analysis_prompt = f"Analyze the following negotiation input and summarize key points, objectives, and tone:\n\n{state['input']}"
    analysis = call_llm(analysis_prompt)
    
    scorecard = {}
    if mode == "dojo":
        # 2. Scorecard Generation (only for Dojo/Training)
        score_prompt = f"""
        Evaluate the user's negotiation skills based on this input: "{state['input']}"
        Provide a JSON object with:
        - "tactics_score": (0-100)
        - "resilience_score": (0-100)
        - "tone_score": (0-100)
        - "feedback": (Brief constructive advice)
        
        ONLY return the JSON.
        """
        score_raw = call_llm(score_prompt)
        try:
            # Clean possible markdown formatting
            score_clean = score_raw.replace("```json", "").replace("```", "").strip()
            scorecard = json.loads(score_clean)
        except:
            scorecard = {"tactics_score": 50, "resilience_score": 50, "tone_score": 50, "feedback": "Keep practicing!"}

    return {**state, "analysis": analysis, "scorecard": scorecard}
