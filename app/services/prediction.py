import httpx
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from app.core.config import settings
from app.schemas.cycle import CyclePrediction

class PredictionService:
    def __init__(self):
        self.api_key = settings.OPENROUTER_API_KEY
        self.api_url = settings.OPENROUTER_API_URL
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    async def predict_cycle(
        self,
        historical_cycles: List[Dict],
        current_symptoms: Dict,
        user_metadata: Dict
    ) -> CyclePrediction:
        """
        Predict next cycle dates using DeepSeek R1 via OpenRouter API
        """
        prompt = self._create_prediction_prompt(historical_cycles, current_symptoms, user_metadata)

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.api_url}/chat/completions",
                headers=self.headers,
                json={
                    "model": "deepseek-ai/deepseek-r1",
                    "messages": [
                        {"role": "system", "content": "You are a menstrual cycle prediction assistant. Analyze the provided data and predict the next ovulation and period dates."},
                        {"role": "user", "content": prompt}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 500
                }
            )

            if response.status_code != 200:
                raise Exception(f"Prediction API error: {response.text}")

            result = response.json()
            prediction = self._parse_prediction_response(result)

            return prediction

    def _create_prediction_prompt(
        self,
        historical_cycles: List[Dict],
        current_symptoms: Dict,
        user_metadata: Dict
    ) -> str:
        """Create a detailed prompt for the AI model"""
        prompt = f"""
        Analyze the following menstrual cycle data and predict the next ovulation and period dates:

        Historical Cycles:
        {historical_cycles}

        Current Symptoms:
        {current_symptoms}

        User Metadata:
        {user_metadata}

        Please provide:
        1. Predicted ovulation date
        2. Predicted period start date
        3. Confidence level (0-1)
        4. Any relevant notes or considerations
        """
        return prompt

    def _parse_prediction_response(self, response: Dict) -> CyclePrediction:
        """Parse the AI response into a CyclePrediction object"""
        # Extract dates and confidence from the response
        # This is a simplified version - you'll need to implement proper parsing
        # based on the actual response format from DeepSeek R1

        # For now, return a mock prediction
        return CyclePrediction(
            predicted_ovulation_date=datetime.now() + timedelta(days=14),
            predicted_period_start=datetime.now() + timedelta(days=28),
            confidence=0.85,
            metadata={"model": "deepseek-r1", "timestamp": datetime.now().isoformat()}
        )
