import os
from dotenv import load_dotenv
import yfinance as yf
from biotech_mercenary_bot import BiotechMercenaryBot

# Load your local environment variables (where your OPENAI_API_KEY lives)
load_dotenv()

def run_production_test():
    # 1. Initialize your GitHub bot using your real OpenAI API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY not found in your environment variables.")
        return
        
    bot = BiotechMercenaryBot(openai_api_key=api_key)
    
    # 2. Pull REAL historical market data for a major biotech competitor [finance]
    # Let's test Guardant Health (GH) [finance]
    print("📥 Fetching real-time market data from Yahoo Finance for ticker: GH...")
    ticker = yf.Ticker("GH")
    historical_data = ticker.history(period="1mo") # Fetch 1 month of daily prices
    
    # Extract just the closing prices into a raw list for the quant module
    real_closing_prices = historical_data['Close'].tolist()
    
    if len(real_closing_prices) < 14:
        print("❌ Error: Not enough historical market data to calculate a 14-period RSI.")
        return

    # 3. Define a real-world test scenario headline based on an oncology press release
    test_headline = "Guardant Health receives FDA approval for Shield blood test for colorectal cancer screening."
    
    print("\n--- Starting Decision Fusion Pipeline Test ---")
    print(f"📰 Qualitative Input (Headline): '{test_headline}'")
    print(f"📈 Quantitative Input: Processing last {len(real_closing_prices)} closing prices...")
    
    # 4. Execute the pipeline
    try:
        execution_vector = bot.fusion_integration_module(real_closing_prices, test_headline)
        print("\n🎯 PIPELINE OUTPUT METRIC:")
        print(execution_vector)
        print("----------------------------------------------")
        print("✅ Pipeline execution successful. Architecture validated.")
    except Exception as e:
        print(f"❌ Pipeline Execution Failed: {str(e)}")

if __name__ == "__main__":
    run_production_test()

