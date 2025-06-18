def recommend_cards(user_income, preferred_reward_type=None, desired_perks=None, spending_habits=None, db_path="credit_cards.db"):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query = "SELECT name, issuer, joining_fee, annual_fee, reward_type, reward_rate, eligibility, perks, apply_link, image_url FROM credit_cards WHERE 1=1"
    params = []

    if user_income:
        query += " AND CAST(REPLACE(REPLACE(eligibility, 'Income > ₹', ''), ',', '') AS INTEGER) <= ?"
        params.append(user_income)

    if preferred_reward_type:
        query += " AND LOWER(reward_type) LIKE ?"
        params.append(f"%{preferred_reward_type.lower()}%")

    if desired_perks:
        perk_conditions = " OR ".join(["LOWER(perks) LIKE ?"] * len(desired_perks))
        query += f" AND ({perk_conditions})"
        params.extend([f"%{p.lower()}%" for p in desired_perks])


    cursor.execute(query, tuple(params))
    results = cursor.fetchall()
    conn.close()

    cards_with_info = []
    for card in results:
        reward_rate = extract_reward_rate(card[5])
        est_reward = simulate_rewards(spending_habits, reward_rate)
        reason = generate_reason(card[6], card[7], card[4])
        cards_with_info.append((card, est_reward, reason))

    cards_with_info.sort(key=lambda x: x[1], reverse=True)
    return cards_with_info[:5]


def extract_reward_rate(rate_str):
    try:
        if "%" in rate_str:
            return float(rate_str.replace('%', '').strip()) / 100
        elif "/" in rate_str:
            return 0.01  # flat fallback for points-based
        else:
            return float(rate_str)
    except:
        return 0.01


def simulate_rewards(spending_habits, reward_rate):
    if not spending_habits or not any(spending_habits.values()):
        estimated_monthly_spend = 10000  # fallback
    else:
        estimated_monthly_spend = sum(spending_habits.values())
    return round(estimated_monthly_spend * reward_rate * 12)


def generate_reason(eligibility, perks, reward_type):
    reasons = []
    if "Lounge" in perks:
        reasons.append("Ideal for frequent flyers")
    if "Fuel" in perks:
        reasons.append("Good for daily commuters")
    if "Movie" in perks:
        reasons.append("Great for movie lovers")
    if "Dining" in perks:
        reasons.append("Includes dining discounts")
    if reward_type.lower() == "cashback":
        reasons.append("Earns direct cashback")
    return " | ".join(reasons[:2]) or "Well-rounded benefits"
