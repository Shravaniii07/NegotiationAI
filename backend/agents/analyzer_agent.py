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
        Provide a JSON object with exactly these fields (values between 0-100):
        - "tactics_score": (0-100)
        - "resilience_score": (0-100)
        - "tone_score": (0-100)
        - "deal_value_score": (0-100, where 100 means they are maintaining profit margins well, and lower means they are conceding too much value)
        - "emotions": {{ "confidence": (0-100), "empathy": (0-100), "aggression": (0-100), "logic": (0-100) }}
        - "feedback": (Brief constructive advice)
        
        ONLY return the raw JSON object, no markdown, no other text.
        """
        score_raw = call_llm(score_prompt)
        try:
            # Clean possible markdown formatting
            score_clean = score_raw.replace("```json", "").replace("```", "").strip()
            scorecard = json.loads(score_clean)
            
            # Ensure emotions exist in case AI hallucinates structure
            if "emotions" not in scorecard:
                scorecard["emotions"] = {"confidence": 50, "empathy": 50, "aggression": 50, "logic": 50}
            if "deal_value_score" not in scorecard:
                scorecard["deal_value_score"] = 50
                
        except:
            scorecard = {
                "tactics_score": 50, "resilience_score": 50, "tone_score": 50, "deal_value_score": 50,
                "emotions": {"confidence": 50, "empathy": 50, "aggression": 50, "logic": 50},
                "feedback": "Keep practicing!"
            }

    return {**state, "analysis": analysis, "scorecard": scorecard}
