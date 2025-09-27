crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high", 
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

print("CryptoBuddy: Hey there! Let's find you a green and growing crypto! 🌟")

while True:
    user_query = input("\nYou: ").lower()
    
    if "sustainable" in user_query or "eco" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: Invest in {recommend}! 🌱 It's eco-friendly!")
        
    elif "trend" in user_query or "rising" in user_query:
        for crypto, data in crypto_db.items():
            if data["price_trend"] == "rising":
                print(f"CryptoBuddy: {crypto} is trending up! 📈")
                
    elif "profit" in user_query or "grow" in user_query:
        for crypto, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                print(f"CryptoBuddy: {crypto} has high growth potential! 🚀")
                
    elif "exit" in user_query or "bye" in user_query:
        print("CryptoBuddy: Happy investing! Remember, crypto is risky - do your research! 💡")
        break
        
    else:
        print("CryptoBuddy: Ask me about sustainable cryptos, trends, or profits!")