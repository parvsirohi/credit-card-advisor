import sqlite3

conn = sqlite3.connect("credit_cards.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS credit_cards")
cursor.execute("""
CREATE TABLE credit_cards (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    issuer TEXT,
    joining_fee INTEGER,
    annual_fee INTEGER,
    reward_type TEXT,
    reward_rate TEXT,
    eligibility TEXT,
    perks TEXT,
    apply_link TEXT,
    image_url TEXT
)
""")

# Insert values (35 total cards)
cards = [
    ('HDFC Millennia', 'HDFC', 1000, 1000, 'Cashback', '1.5%', 'Income > ₹25,000', 'Lounge Access, Fuel Cashback', 'https://apply.hdfc.com', 'https://example.com/hdfc_millennia.jpg'),
    ('SBI SimplyClick', 'SBI', 499, 499, 'Online Shopping', '1%', 'Income > ₹20,000', 'Amazon Voucher, Online Cashback', 'https://apply.sbicard.com', 'https://example.com/sbi_click.jpg'),
    ('Axis ACE', 'Axis Bank', 500, 500, 'Cashback', '2%', 'Income > ₹30,000', 'Utility Cashback, Lounge Access', 'https://apply.axisbank.com', 'https://example.com/axis_ace.jpg'),
    ('ICICI AmazonPay', 'ICICI', 0, 0, 'Amazon Points', '5%', 'Income > ₹20,000', 'Amazon Cashback, No Joining Fee', 'https://apply.icici.com', 'https://example.com/icici_amazon.jpg'),
    ('HSBC Platinum', 'HSBC', 0, 0, 'Cashback', '1.5%', 'Income > ₹40,000', 'Dining Offers, Travel Discounts', 'https://apply.hsbc.com', 'https://example.com/hsbc_platinum.jpg'),
    ('RBL ShopRite', 'RBL', 500, 500, 'Shopping Rewards', '2%', 'Income > ₹25,000', 'Grocery Cashback, Fuel Surcharge Waiver', 'https://apply.rblbank.com', 'https://example.com/rbl_shoprite.jpg'),
    ('Amex SmartEarn', 'American Express', 495, 495, 'MR Points', '1%', 'Income > ₹35,000', 'Online Shopping Rewards', 'https://apply.americanexpress.com', 'https://example.com/amex_smartearn.jpg'),
    ('Kotak Royale Signature', 'Kotak', 999, 999, 'Reward Points', '2%', 'Income > ₹50,000', 'Lounge Access, Dining Offers', 'https://apply.kotak.com', 'https://example.com/kotak_royale.jpg'),
    ('Yes First Preferred', 'Yes Bank', 1000, 2500, 'Reward Points', '1.5%', 'Income > ₹50,000', 'Priority Pass, Concierge Service', 'https://apply.yesbank.in', 'https://example.com/yes_preferred.jpg'),
    ('IDFC First Wealth', 'IDFC', 0, 0, 'Reward Points', '2.5%', 'Income > ₹50,000', 'No Joining Fee, Lounge Access', 'https://apply.idfcfirstbank.com', 'https://example.com/idfc_wealth.jpg'),
    ('AU Zenith+', 'AU Small Finance', 3000, 3000, 'Cashback', '1.75%', 'Income > ₹60,000', 'Luxury Lifestyle Offers', 'https://apply.aubank.in', 'https://example.com/au_zenith.jpg'),
    ('BOB Eterna', 'Bank of Baroda', 2499, 2499, 'Reward Points', '3.33%', 'Income > ₹40,000', 'Zomato Pro, Movie Benefits', 'https://apply.bankofbaroda.in', 'https://example.com/bob_eterna.jpg'),
    ('IndusInd Legend', 'IndusInd Bank', 5000, 5000, 'Reward Points', '1.5%', 'Income > ₹60,000', 'Lounge Access, Golf Access', 'https://apply.indusind.com', 'https://example.com/indusind_legend.jpg'),
    ('HDFC Regalia', 'HDFC', 2500, 2500, 'Reward Points', '4 points/₹150', 'Income > ₹50,000', 'Lounge Access, Travel Benefits', 'https://apply.hdfc.com', 'https://example.com/hdfc_regalia.jpg'),
    ('SBI Prime', 'SBI', 2999, 2999, 'Reward Points', '10 points/₹100', 'Income > ₹35,000', 'Lounge, Dining, Movie Offers', 'https://apply.sbicard.com', 'https://example.com/sbi_prime.jpg'),
    ('Axis Vistara Infinite', 'Axis Bank', 10000, 10000, 'Travel Miles', '6 CV Points/₹200', 'Income > ₹60,000', 'Free Tickets, Lounge Access', 'https://apply.axisbank.com', 'https://example.com/axis_vistara.jpg'),
    ('ICICI Platinum Chip', 'ICICI', 0, 0, 'Cashback', '1%', 'Income > ₹15,000', 'Fuel Surcharge Waiver', 'https://apply.icici.com', 'https://example.com/icici_platinum.jpg'),
    ('HDFC Diners Club Privilege', 'HDFC', 2500, 2500, 'Reward Points', '4 points/₹150', 'Income > ₹60,000', 'Diners Lounges, Golf Access', 'https://apply.hdfc.com', 'https://example.com/hdfc_diners.jpg'),
    ('SBI Elite', 'SBI', 4999, 4999, 'Reward Points', '10 points/₹100', 'Income > ₹50,000', 'Lounge, Movie, Concierge', 'https://apply.sbicard.com', 'https://example.com/sbi_elite.jpg'),
    ('Amex Platinum Travel', 'American Express', 3500, 5000, 'Travel Miles', 'MR Points', 'Income > ₹40,000', 'Taj Vouchers, Lounge', 'https://apply.americanexpress.com', 'https://example.com/amex_platinum.jpg'),
    ('Federal Celesta', 'Federal Bank', 3500, 3500, 'Reward Points', '2%', 'Income > ₹45,000', 'Airport Lounge, Dining Offers', 'https://apply.federalbank.co.in', 'https://example.com/federal_celesta.jpg'),
    ('PNB RuPay Platinum', 'PNB', 0, 500, 'Reward Points', '1%', 'Income > ₹25,000', 'Fuel Surcharge Waiver', 'https://apply.pnbindia.in', 'https://example.com/pnb_rupay.jpg'),
    ('Bank of India Signature', 'BOI', 1500, 1500, 'Reward Points', '1.5%', 'Income > ₹30,000', 'Dining Discounts', 'https://apply.bankofindia.co.in', 'https://example.com/boi_signature.jpg'),
    ('Canara RuPay Select', 'Canara Bank', 0, 500, 'Reward Points', '1%', 'Income > ₹25,000', 'Health & Wellness Offers', 'https://apply.canarabank.in', 'https://example.com/canara_select.jpg'),
    ('Union Bank Rupay Platinum', 'Union Bank', 0, 500, 'Reward Points', '1%', 'Income > ₹25,000', 'Dining, Fuel Offers', 'https://apply.unionbankofindia.co.in', 'https://example.com/union_platinum.jpg'),
    ('IDBI Royale Signature', 'IDBI', 1500, 1500, 'Reward Points', '2%', 'Income > ₹30,000', 'Travel Discounts, Golf Offers', 'https://apply.idbibank.in', 'https://example.com/idbi_royale.jpg'),
    ('Yes Premia', 'Yes Bank', 1000, 1000, 'Reward Points', '2%', 'Income > ₹40,000', 'Lounge Access, Dining', 'https://apply.yesbank.in', 'https://example.com/yes_premia.jpg'),
    ('HSBC Smart Value', 'HSBC', 0, 0, 'Cashback', '1.5%', 'Income > ₹30,000', 'EMI Offers, Dining', 'https://apply.hsbc.com', 'https://example.com/hsbc_smart.jpg'),
    ('RBL Platinum Delight', 'RBL', 500, 500, 'Reward Points', '2%', 'Income > ₹30,000', 'Grocery Cashback', 'https://apply.rblbank.com', 'https://example.com/rbl_platinum.jpg'),
    ('Amex Membership Rewards', 'American Express', 1000, 1500, 'Reward Points', '1%', 'Income > ₹30,000', 'Bonus Points, Dining', 'https://apply.americanexpress.com', 'https://example.com/amex_rewards.jpg'),
    ('BOB Premier', 'Bank of Baroda', 1000, 1000, 'Reward Points', '2%', 'Income > ₹35,000', 'Movie, Dining Offers', 'https://apply.bankofbaroda.in', 'https://example.com/bob_premier.jpg'),
    ('HDFC MoneyBack+', 'HDFC', 500, 500, 'Reward Points', '2%', 'Income > ₹30,000', 'Online Shopping, Cashback', 'https://apply.hdfc.com', 'https://example.com/hdfc_moneyback.jpg'),
    ('Axis Neo', 'Axis Bank', 250, 250, 'Reward Points', '1.5%', 'Income > ₹25,000', 'OTT Subscriptions, Shopping', 'https://apply.axisbank.com', 'https://example.com/axis_neo.jpg'),
    ('ICICI Coral Contactless', 'ICICI', 500, 500, 'Reward Points', '1%', 'Income > ₹25,000', 'Movie, Dining Offers', 'https://apply.icici.com', 'https://example.com/icici_coral.jpg'),
    ('SBI Unnati', 'SBI', 0, 0, 'Reward Points', '1%', 'Income > ₹15,000', 'Fuel Surcharge Waiver', 'https://apply.sbicard.com', 'https://example.com/sbi_unnati.jpg')
]

cursor.executemany("""
INSERT INTO credit_cards (
    name, issuer, joining_fee, annual_fee, reward_type, reward_rate, eligibility, perks, apply_link, image_url
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", cards)

conn.commit()
conn.close()
