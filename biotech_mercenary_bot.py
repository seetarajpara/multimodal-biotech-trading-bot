import os
import requests
import pandas as pd
from openai import OpenAI

class BiotechMercenaryBot:
    def __init__(self, openai_api_key: str):
        """
        Initializes the system using standard off-the-shelf LLM wrappers.
        """
        self.client = OpenAI(api_key=openai_api_key)

    def calculate_rsi(self, price_data: list, period: int = 14) -> float:
        """
        Quantitative Module: Computes a baseline financial metric (RSI).
        Replicates standard technical analysis used in basic day-trading.
        """
        series = pd.Series(price_data)
        delta = series.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return float(rsi.iloc[-1])

    def analyze_clinical_sentiment(self, headline: str) -> dict:
        """
        Qualitative Module: Leverages an LLM via API to parse text.
        Extracts categorical sentiment score from clinical trial text data.
        """
        prompt = f"""
        Analyze this biotech clinical trial news headline for market impact.
        Classify sentiment as Positive, Neutral, or Negative.
        Provide a confidence score between 0.0 and 1.0.
        Output ONLY valid JSON with keys "sentiment" and "confidence".
        
        Headline: "{headline}"
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        
        import json
        return json.loads(response.choices[0].message.content)

    def fusion_integration_module(self, price_series: list, news_headline: str) -> str:
        """
        Decision Fusion Module: Integrates quantitative behavior with qualitative text signals.
        Outputs an actionable decision metric (Buy, Sell, or Hold).
        """
        # 1. Quant analysis
        current_rsi = self.calculate_rsi(price_series)
        
        # 2. Qual analysis
        text_insights = self.analyze_clinical_sentiment(news_headline)
        sentiment = text_insights.get("sentiment")
        confidence = text_insights.get("confidence", 0.5)
        
        # 3. Simple heuristic fusion matrix (replaces "fuzzy rules salad")
        if sentiment == "Positive" and current_rsi < 70 and confidence > 0.7:
            return f"BUY SIGNAL (RSI: {current_rsi:.2f}, Text Confidence: {confidence})"
        elif sentiment == "Negative" or current_rsi > 70:
            return f"SELL/EXIT SIGNAL (RSI: {current_rsi:.2f}, Text Confidence: {confidence})"
        else:
            return f"HOLD SIGNAL (RSI: {current_rsi:.2f}, Text Confidence: {confidence})"

# Example standard runtime execution
if __name__ == "__main__":
    # Mocking standard financial time-series data
    mock_prices = [10.2, 10.5, 10.4, 10.8, 11.1, 11.0, 11.5, 12.1, 11.9, 12.3, 12.8, 12.5, 13.1, 13.5, 14.2]
    mock_headline = "Phase III trials for breakthrough molecule show 40% improvement in progression-free survival."
    
    # Initialize wrapper with dummy key placeholder
    bot = BiotechMercenaryBot(openai_api_key=os.getenv("OPENAI_API_KEY", "mock_key_if_running_locally"))
    
    # Run the "patent-pending" integration pipeline logic
    print("Executing decision fusion pipeline...")
    print(bot.fusion_integration_module(mock_prices, mock_headline))
