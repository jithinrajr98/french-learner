
from langchain_ollama import ChatOllama
from typing import List, Dict, Any
from ast import literal_eval
import re
from config.settings import LLM_MODELS


class LLMUtils:
    
    def __init__(self):
        self.llms = {
            "translator": ChatOllama(model=LLM_MODELS["translator"]),
            "evaluator": ChatOllama(model=LLM_MODELS["evaluator"]),
            "word_helper": ChatOllama(model=LLM_MODELS["word_helper"]),
            "french_word_meaning" : ChatOllama(model=LLM_MODELS["french_word_meaning"])
        }
        
    def get_french_translation(self, english_text: str) -> str:
        """Translate English text to French"""
        
        prompt = f"""
        You are a professional translator. Translate this English text to French.
        Return ONLY the French translation without any additional text.
        
        English: {english_text}
        French: """
        response = self.llms["translator"].invoke(prompt).content
        return response.strip('"').strip()
    
    
    def extract_missed_words(self, correct: str, attempt: str) -> List[str]:
        """Identify missing words from user's translation attempt"""
        prompt = f"""
        Compare these French translations:
        Correct: {correct}
        Attempt: {attempt}
        
        Identify which content words (nouns, verbs, adjectives, adverbs) 
        from the correct translation are missing in the attempt.
        Return ONLY a Python list of the missing words in their base form.
        Example: ['mot1', 'mot2']
        """
        try:
            response = self.llms["evaluator"].invoke(prompt).content
            return literal_eval(response)
        except:
            return []
        
        
        
    def get_word_details(self, french_word: str) -> Dict[str, Any]:
        """Get detailed information about a French word"""
        
        prompt = f"""
                    Provide detailed information about the French word: "{french_word}"

                    Respond in the following structured format:
                    - pos: part of speech (e.g., noun, verb, adjective)
                    - meaning: English meaning(s)
                    - infintive: infinitive form of the {french_word}"
                    - conjugations: present tense conjugations (only if it's a verb)

                    Example Output:

                    **POS**: verb  
                    **Meaning**: to eat
                    **Infinitive**: manger \n
                    **Conjugations**:  
                    je: mange  
                    tu: manges  
                    il/elle: mange  
                    nous: mangeons  
                    vous: mangez  
                    ils/elles: mangent  

                    Only return the structured output above. Do not include any explanations or extra text.
                    """
        response = self.llms["word_helper"].invoke(prompt).content
        return response
    
    def get_french_word_meaning(self,word: str) -> str:
        prompt = f"""What does the French word or sentence "{word}" mean in English? Return up to 3 meanings as a single comma seperated list. Do not explain."""

        response = self.llms["french_word_meaning"].invoke(prompt).content.strip()
       
        return response
        
        
        
llm_utils = LLMUtils()

    
        
        
        
        
        
        
        
    
    