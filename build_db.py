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
    ('HDFC Millennia', 'HDFC', 1000, 1000, 'Cashback', '1.5%', 'Income > ₹25,000', 'Lounge Access, Fuel Cashback', 'https://apply.hdfc.com', 'https://images.fintra.co.in/cms/hdfc-millennia-credit-card-1.png'),
    ('SBI SimplyClick', 'SBI', 499, 499, 'Online Shopping', '1%', 'Income > ₹20,000', 'Amazon Voucher, Online Cashback', 'https://apply.sbicard.com', 'https://www.paisabazaar.com/wp-content/uploads/2021/12/SBI-SimplyCLICK-Credit-Card.jpg'),
    ('Axis ACE', 'Axis Bank', 500, 500, 'Cashback', '2%', 'Income > ₹30,000', 'Utility Cashback, Lounge Access', 'https://apply.axisbank.com', 'https://www.cardexpert.in/wp-content/uploads/2020/10/axis-bank-ace-credit-card-1.jpg'),
    ('ICICI AmazonPay', 'ICICI', 0, 0, 'Amazon Points', '5%', 'Income > ₹20,000', 'Amazon Cashback, No Joining Fee', 'https://apply.icici.com', 'https://cardinsider.com/wp-content/uploads/2021/06/amazon-pay.png'),
    ('HSBC Platinum', 'HSBC', 0, 0, 'Cashback', '1.5%', 'Income > ₹40,000', 'Dining Offers, Travel Discounts', 'https://apply.hsbc.com', 'https://www.hsbc.com.au/content/dam/hsbc/au/images/16-9/HSBC0688--HSBC-PLATINUM-Final.jpg/_jcr_content/renditions/cq5dam.web.1280.1280.jpeg'),
    ('RBL ShopRite', 'RBL', 500, 500, 'Shopping Rewards', '2%', 'Income > ₹25,000', 'Grocery Cashback, Fuel Surcharge Waiver', 'https://apply.rblbank.com', 'https://cdn0.desidime.com/attachments/photos/1002538/medium/rblrupay.jpg?1707211024'),
    ('Amex SmartEarn', 'American Express', 495, 495, 'MR Points', '1%', 'Income > ₹35,000', 'Online Shopping Rewards', 'https://apply.americanexpress.com', 'https://www.cardexpert.in/wp-content/uploads/2019/08/American-Express-SmartEarn-Credit-Card-300x210.png'),
    ('Kotak Royale Signature', 'Kotak', 999, 999, 'Reward Points', '2%', 'Income > ₹50,000', 'Lounge Access, Dining Offers', 'https://apply.kotak.com', 'https://cd9941cc.delivery.rocketcdn.me/wp-content/uploads/2021/07/Kotak-Royale-Signature-Credit-Card.webp'),
    ('Yes First Preferred', 'Yes Bank', 1000, 2500, 'Reward Points', '1.5%', 'Income > ₹50,000', 'Priority Pass, Concierge Service', 'https://apply.yesbank.in', 'https://tse4.mm.bing.net/th?id=OIP.dyGOoiFAeZtd-O6rSj-PqwAAAA&pid=Api&P=0&h=180'),
    ('IDFC First Wealth', 'IDFC', 0, 0, 'Reward Points', '2.5%', 'Income > ₹50,000', 'No Joining Fee, Lounge Access', 'https://apply.idfcfirstbank.com', 'https://www.paisabazaar.com/wp-content/uploads/2021/01/IDFC-First-wealth-Credit-Card.png'),
    ('AU Zenith+', 'AU Small Finance', 3000, 3000, 'Cashback', '1.75%', 'Income > ₹60,000', 'Luxury Lifestyle Offers', 'https://apply.aubank.in', 'https://www.paisabazaar.com/wp-content/uploads/2023/09/AU-Zenith-Credit-Card.png'),
    ('BOB Eterna', 'Bank of Baroda', 2499, 2499, 'Reward Points', '3.33%', 'Income > ₹40,000', 'Zomato Pro, Movie Benefits', 'https://apply.bankofbaroda.in', 'https://cms-resources.groww.in/uploads/Bo_B_Eterna_credit_card_958e17747d.png'),
    ('IndusInd Legend', 'IndusInd Bank', 5000, 5000, 'Reward Points', '1.5%', 'Income > ₹60,000', 'Lounge Access, Golf Access', 'https://apply.indusind.com', 'https://cardinsider.com/wp-content/uploads/2021/07/IndusInd-Legend-Credit-Card-2.png'),
    ('HDFC Regalia', 'HDFC', 2500, 2500, 'Reward Points', '4 points/₹150', 'Income > ₹50,000', 'Lounge Access, Travel Benefits', 'https://apply.hdfc.com', 'https://v.hdfcbank.com/content/dam/hdfc-aem-microsites/htdocs/common/credit-cards/calculators/images/cards/Regalia.png'),
    ('SBI Prime', 'SBI', 2999, 2999, 'Reward Points', '10 points/₹100', 'Income > ₹35,000', 'Lounge, Dining, Movie Offers', 'https://apply.sbicard.com', 'https://cms-resources.groww.in/uploads/sbi_prime_credit_card_e8d948c88d.png'),
    ('Axis Vistara Infinite', 'Axis Bank', 10000, 10000, 'Travel Miles', '6 CV Points/₹200', 'Income > ₹60,000', 'Free Tickets, Lounge Access', 'https://apply.axisbank.com', 'https://cdnapp.indialends.com/illive/images/axis-flow-new/Vistara_Infinite.png'),
    ('ICICI Platinum Chip', 'ICICI', 0, 0, 'Cashback', '1%', 'Income > ₹15,000', 'Fuel Surcharge Waiver', 'https://apply.icici.com', 'https://thumbor.forbes.com/thumbor/fit-in/x/https://www.forbes.com/advisor/in/wp-content/uploads/2021/10/icici_bank_platinum_chip_credit_card-1.png'),
    ('HDFC Diners Club Privilege', 'HDFC', 2500, 2500, 'Reward Points', '4 points/₹150', 'Income > ₹60,000', 'Diners Lounges, Golf Access', 'https://apply.hdfc.com', 'https://v.hdfcbank.com/content/dam/hdfc-aem-microsites/thereforyou/images/cards/Diners_Privilege.png'),
    ('SBI Elite', 'SBI', 4999, 4999, 'Reward Points', '10 points/₹100', 'Income > ₹50,000', 'Lounge, Movie, Concierge', 'https://apply.sbicard.com', 'https://1.bp.blogspot.com/-f5303XP7Z0g/XT1ujQ-xMaI/AAAAAAAAARo/OLM33NIjpKQSwbLffJQ6fDZHKbui7QJswCLcBGAs/s1600/SBI%2BELITE%2BCREDIT%2BCARD.jp'),
    ('Amex Platinum Travel', 'American Express', 3500, 5000, 'Travel Miles', 'MR Points', 'Income > ₹40,000', 'Taj Vouchers, Lounge', 'https://apply.americanexpress.com', 'https://www.adgully.com/img/800/50940_american-express-platinum-travel-card.jpg'),
    ('Federal Celesta', 'Federal Bank', 3500, 3500, 'Reward Points', '2%', 'Income > ₹45,000', 'Airport Lounge, Dining Offers', 'https://apply.federalbank.co.in', 'https://www.federalbank.co.in/documents/10180/85519258/1637x2600pxl+(1).jpg/2232329c-1814-ae42-90be-3a469fe4461b?t=1644865488375'),
    ('PNB RuPay Platinum', 'PNB', 0, 500, 'Reward Points', '1%', 'Income > ₹25,000', 'Fuel Surcharge Waiver', 'https://apply.pnbindia.in', 'https://cardinsider.com/wp-content/uploads/2021/07/PNB-RUPAY-PLATINUM-Card.png'),
    ('Bank of India Signature', 'BOI', 1500, 1500, 'Reward Points', '1.5%', 'Income > ₹30,000', 'Dining Discounts', 'https://apply.bankofindia.co.in', 'https://example.com/boi_signature.jpg'),
    ('Canara RuPay Select', 'Canara Bank', 0, 500, 'Reward Points', '1%', 'Income > ₹25,000', 'Health & Wellness Offers', 'https://apply.canarabank.in', 'https://cardinsider.com/wp-content/uploads/2021/08/Canara-Bank-RuPay-Select-Credit-Card-1.png'),
    ('Union Bank Rupay Platinum', 'Union Bank', 0, 500, 'Reward Points', '1%', 'Income > ₹25,000', 'Dining, Fuel Offers', 'https://apply.unionbankofindia.co.in', 'https://www.ubisl.co.in/images/credit-cards/Union-Platinum-RuPay-Credit-Card.jpg'),
    ('IDBI Royale Signature', 'IDBI', 1500, 1500, 'Reward Points', '2%', 'Income > ₹30,000', 'Travel Discounts, Golf Offers', 'https://apply.idbibank.in', 'https://bankbooklet.com/wp-content/uploads/IDBI-Bank-Royale-Signature-Credit-Card.jpg'),
    ('Yes Premia', 'Yes Bank', 1000, 1000, 'Reward Points', '2%', 'Income > ₹40,000', 'Lounge Access, Dining', 'https://apply.yesbank.in', 'https://tse2.mm.bing.net/th?id=OIP.Ax4IY0DTU9X8S00O9H-v-QHaHa&pid=Api&P=0&h=180'),
    ('HSBC Smart Value', 'HSBC', 0, 0, 'Cashback', '1.5%', 'Income > ₹30,000', 'EMI Offers, Dining', 'https://apply.hsbc.com', 'https://www.paisabazaar.com/wp-content/uploads/2019/08/HSBC-Smart-Value-Credit-Card-1.jpeg'),
    ('RBL Platinum Delight', 'RBL', 500, 500, 'Reward Points', '2%', 'Income > ₹30,000', 'Grocery Cashback', 'https://apply.rblbank.com', 'https://bestvaluesguide.com/wp-content/uploads/2023/11/RBL-Platinum-Delight-credit-card.png.webp'),
    ('Amex Membership Rewards', 'American Express', 1000, 1500, 'Reward Points', '1%', 'Income > ₹30,000', 'Bonus Points, Dining', 'https://apply.americanexpress.com', 'https://example.com/amex_rewards.jpg'),
    ('BOB Premier', 'Bank of Baroda', 1000, 1000, 'Reward Points', '2%', 'Income > ₹35,000', 'Movie, Dining Offers', 'https://apply.bankofbaroda.in', 'https://www.bankofbaroda.in/-/media/project/bob/countrywebsites/india/personal/cards/credit-cards/card-image/credit-card-premier.png?h=170&iar=0&w=280&hash=4B837BEBFB529EF81BC608A3A87835A0'),
    ('HDFC MoneyBack+', 'HDFC', 500, 500, 'Reward Points', '2%', 'Income > ₹30,000', 'Online Shopping, Cashback', 'https://apply.hdfc.com', 'https://cms-resources.groww.in/uploads/HDFC_Money_Back_Plus_Credit_Card_344b56d15f.png'),
    ('Axis Neo', 'Axis Bank', 250, 250, 'Reward Points', '1.5%', 'Income > ₹25,000', 'OTT Subscriptions, Shopping', 'https://apply.axisbank.com', 'https://finder.cardmaven.in/wp-content/uploads/2024/02/Axis-Bank-Neo.png'),
    ('ICICI Coral Contactless', 'ICICI', 500, 500, 'Reward Points', '1%', 'Income > ₹25,000', 'Movie, Dining Offers', 'https://apply.icici.com', 'https://www.paisabazaar.com/wp-content/uploads/2018/05/Capture.jpg'),
    ('SBI Unnati', 'SBI', 0, 0, 'Reward Points', '1%', 'Income > ₹15,000', 'Fuel Surcharge Waiver', 'https://apply.sbicard.com', 'https://cms-resources.groww.in/uploads/sbi_unnati_credit_card_3312f0639b.png')
]

cursor.executemany("""
INSERT INTO credit_cards (
    name, issuer, joining_fee, annual_fee, reward_type, reward_rate, eligibility, perks, apply_link, image_url
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", cards)

conn.commit()
conn.close()
