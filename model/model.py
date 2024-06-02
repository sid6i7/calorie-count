import google.generativeai as genai
import os
from dotenv import load_dotenv
from model.nutrition import NutritionScraper

load_dotenv()

key = os.environ['GOOGLE_API_KEY']
genai.configure(api_key=key)


class Model:
    def __init__(self) -> None:
        self.__prompt = """Here is a picture of a food item from India. Identify what type of food item it is. You're supposed to follow the response instructions STRICTLY as follows: Only respond with the name and nothing else. If you don't know or the image is not clear enough then reply with "I don't know" only and nothing else.
        """

        self.generation_config = {
            "temperature": 0.5,
            "top_p": 0.95,
            "max_output_tokens": 100,
            "response_mime_type": "text/plain",
        }

        self.model_name = "gemini-1.5-flash"

    def __upload_to_gemini(self, path):
        file = genai.upload_file(path)
        print(f"Uploaded file '{file.display_name}' as: {file.uri}")
        return file

    def identify_food(self, path):
        image = self.__upload_to_gemini(path)

        model = genai.GenerativeModel(
            model_name= self.model_name,
            generation_config=self.generation_config
        )

        chat_session = model.start_chat()

        response = chat_session.send_message({
            "role": "user",
            "parts": [
                image,
                self.__prompt
            ]
        })

        return response.text.strip()
    
    def get_nutrition(self, path):
        dish_name = self.identify_food(path)
        scraper = NutritionScraper()
        nutrition = scraper.get_nutrition(dish_name)
        print(nutrition)
        return nutrition