# 🛵 Electric Scooter Support Chatbot (Rasa)

## 🤖 Overview

This is an intelligent, AI-powered customer support chatbot built using **Rasa** for an electric scooter company. The chatbot is capable of answering customer queries, providing product information, assisting with service bookings, and more—enhancing the customer experience through instant and automated responses.

---

## 🧠 Features

- 🚲 Product inquiries (models, specs, range, price)
- 🔋 Battery and charging info
- 🧾 Booking test rides or service appointments
- 🛠️ Troubleshooting and support
- 🗺️ Store locator
- 💬 Fallback and escalation to human support

---

## 🗂️ Project Structure

```
electric-scooter-chatbot/
├── data/
│   ├── nlu.yml             # User intents and training examples
│   ├── rules.yml           # Rule-based conversations
│   └── stories.yml         # Conversation flows
├── domain.yml              # Intents, responses, entities, actions
├── config.yml              # Pipeline and policy settings
├── actions/
│   └── actions.py          # Custom actions (e.g. check availability)
├── models/
│   └── *.tar.gz            # Trained Rasa model files
├── tests/
│   └── test_stories.yml    # Test cases for bot behavior
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/electric-scooter-chatbot.git
cd electric-scooter-chatbot
```

### 2. Create and Activate a Virtual Environment (Python 3.8)
```bash
python -m venv rasaenv
source rasaenv/bin/activate      # macOS/Linux
# or
rasaenv\Scripts\activate         # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model
```bash
rasa train
```

### 5. Run the Bot in Shell
```bash
rasa shell
```

### 6. Run Actions Server (if using custom actions)
```bash
rasa run actions
```

---

## 🧪 Testing

You can run conversation tests using:
```bash
rasa test
```

---

## 📌 Future Enhancements

- 🌐 Multi-language support
- 📱 Integration with WhatsApp/Facebook
- 🛒 In-chat product ordering
- 📊 Integration with analytics tools for FAQ tracking

---

## 🤝 Contributing

Pull requests are welcome! Please open an issue first to discuss what you'd like to change or add.

---

## 📄 License

[MIT License](LICENSE)

---

## 🔗 Useful Links

- [Rasa Docs](https://rasa.com/docs/)
- [Rasa GitHub](https://github.com/RasaHQ/rasa)
- [Electric Scooter Company Website](#)
