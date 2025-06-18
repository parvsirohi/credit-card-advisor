# main.py
from recommender import recommend_cards

# Sample user inputs
income = 35000
reward = "cashback"
perks = ["lounge", "fuel"]

cards = recommend_cards(user_income=income, preferred_reward_type=reward, desired_perks=perks)

for card in cards:
    print(f"""
Card Name: {card[0]}
Issuer: {card[1]}
Reward Type: {card[4]}
Reward Rate: {card[5]}
Perks: {card[7]}
Apply Link: {card[8]}
""")
