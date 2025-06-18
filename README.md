# 💳 AI Credit Card Advisor

A conversational AI-powered credit card recommendation system that assists users in selecting the best Indian credit cards based on their income, spending habits, and preferred perks. Powered by LangChain and Ollama, the system ensures a personalized, insightful user experience.

---

## 🌟 Key Features

* 🧠 LLM-powered agent using LangChain + Ollama (Mistral)
* 💬 Conversational Q\&A flow covering income, spending, and preferences
* 🗃️ Static SQLite database with 35+ curated Indian credit cards
* 💰 Reward simulation tailored to user spending patterns
* 🌐 Streamlit-based responsive web interface
* 🧾 Transparent view of Joining & Annual Fees
* 🖼️ Card images with fallback placeholder for broken/missing links
* 🔍 Optional filters for card comparison based on reward types or perks
* ⚠️ Intelligent fallback if no matching cards are found
* 🔄 Restart and comparison options for a seamless experience

---

## 📊 Demo

![Demo GIF](https://github.com/your-username/credit-card-advisor/blob/main/demo.gif)

---

## ⚙️ Setup Instructions (macOS/Linux/Windows)

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/credit-card-advisor.git
cd credit-card-advisor
```

### 2. Create and Activate Virtual Environment (macOS/Linux)

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Rebuild the Database

```bash
python build_db.py
```

### 5. Start the Ollama Model

```bash
ollama run mistral
```

### 6. Launch the Streamlit App

```bash
streamlit run app.py
```

---

## 🧠 Agent Flow

1. **Conversational Agent** prompts the user for:

   * Monthly income
   * Spending breakdown (fuel, groceries, dining)
   * Preferred rewards (cashback, points, etc.)
   * Desired perks (e.g., lounge access, movie tickets)
   * Current cards (optional)
   * Credit score (or “unknown”)

2. **Input Extraction** using `utils.py`

3. **Recommendation Engine** in `recommender.py`:

   * Filters and scores cards based on:

     * Eligibility
     * Reward type alignment
     * Perks relevance
     * Reward simulation (₹/year)

4. **UI Output (via Streamlit)**:

   * Card name, image (fallback-safe)
   * Joining and annual fees
   * Key reasons for recommendation
   * Estimated reward/cashback
   * “Apply Now” button linking externally

---

## 🌐 Live Deployment

[https://credit-card-advisor-parv.streamlit.app/]

---

## 📁 Folder Structure

```
credit-card-advisor/
├── app.py                # Streamlit UI and agent flow
├── build_db.py           # Creates and populates credit_cards.db
├── recommender.py        # Recommendation and scoring logic
├── utils.py              # Input parsing and helper methods
├── credit_cards.db       # SQLite DB with card data
├── requirements.txt      # Project dependencies
├── demo.gif              # App walkthrough or preview
└── .gitignore            # Cache and environment ignores
```

---

## 👤 Author

**Parv Sirohi**

---

## ✨ Future Enhancements

* 📱 Twilio WhatsApp bot integration for mobile access
* 📬 Collect user feedback per session
* 📈 Admin dashboard for tracking most recommended cards
* 🔔 Notifications for time-bound card deals
