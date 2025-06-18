import re

def extract_info(text):
    result = {
        "income": None,
        "rewards": None,
        "perks": [],
        "spend": {},
        "credit_score": None,
        "existing_cards": None,
    }

    # Income
    income_match = re.search(r"(income|monthly income)\s*(is|:)?\s*₹?\s*([\d,]+)", text, re.IGNORECASE)
    if income_match:
        result["income"] = int(income_match.group(3).replace(",", ""))

    # Credit Score
    score_match = re.search(r"(credit\s*score|cibil)\s*(is|:)?\s*(\d{3})", text, re.IGNORECASE)
    if score_match:
        result["credit_score"] = int(score_match.group(3))
    elif "unknown" in text.lower():
        result["credit_score"] = "unknown"

    # Reward type
    if "cashback" in text.lower():
        result["rewards"] = "cashback"
    elif "travel" in text.lower():
        result["rewards"] = "travel"
    elif "reward point" in text.lower():
        result["rewards"] = "reward points"

    # Perks
    for perk in ["fuel", "lounge", "grocery", "movie", "dining"]:
        if perk in text.lower():
            result["perks"].append(perk)

    # Spending habits
    spend_matches = re.findall(r"spend\s*₹?\s*(\d+)\s*(on|for)\s*(\w+)", text, re.IGNORECASE)
    for amount, _, category in spend_matches:
        result["spend"][category.lower()] = int(amount)

    # Existing cards
    card_match = re.search(r"(have|use)\s*(a|an|any)?\s*(existing\s*)?(credit\s*)?cards?\s*[:\-]?\s*(.*)", text, re.IGNORECASE)
    if card_match:
        result["existing_cards"] = card_match.group(5).strip()

    return result


def get_next_question(answers, questions):
    for q in questions:
        if q["key"] not in answers or not answers[q["key"]]:
            return q
    return None


def format_summary(answers):
    def nice(k, v):
        if isinstance(v, dict):
            return f"{k.title()}:\n" + "\n".join([f"  - {cat}: ₹{amt}" for cat, amt in v.items()])
        elif isinstance(v, list):
            return f"{k.title()}: {', '.join(v)}"
        elif v:
            return f"{k.title()}: {v}"
        return f"{k.title()}: Not provided"

    return "\n".join([nice(k, v) for k, v in answers.items()])
