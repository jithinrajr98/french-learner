
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
            "french_word_meaning" : ChatOllama(model=LLM_MODELS["french_word_meaning"]),
            "french_accent_correction" : ChatOllama(model=LLM_MODELS["french_accent_correction"])
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
        """/nothink Identify missing words from user's translation attempt"""
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
        
        prompt = f""" /no_think 
                    Provide detailed information about the French word: "{french_word}"

                    Respond in the following structured format:
                    - meaning: English meaning(s)

                    Example Output:
                    **Meaning**: to eat\n

                    Only return the structured output above. Do not include any explanations or extra text.
                    """
        response = self.llms["word_helper"].invoke(prompt).content
        return response
    
    def get_french_word_meaning(self,word: str) -> str:
        prompt = f"""/nothink What does the French word or sentence "{word}" mean in English? Return up to 3 meanings as a single comma seperated list. Do not explain."""

        response = self.llms["french_word_meaning"].invoke(prompt).content.strip()
       
        return response
    
    def correct_french_accents(self, word: str) -> str:
        prompt = f"""/nothink Correct any accent errors in this French text: "{word}"
        
        Important rules:
        1. Return ONLY the corrected French text with proper accents (é, è, ê, ë, à, â, ä, ç, î, ï, ô, ö, ù, û, ü, ÿ)
        2. Do not change correct accents that are already present
        3. If the input has no accent errors, return it exactly as-is
        4. Never add any explanation, commentary, or additional text
        5. Preserve all capitalization, spaces, and punctuation exactly as in the input
        6. Do not modify the text in any way other than correcting accents
        7. Do not add any additional quotes or formatting
        Return ONLY the corrected text:"""
        
        response = self.llms["french_accent_correction"].invoke(prompt).content.strip()
        response = re.sub(r'^[\'"]|[\'"]$', '', response)
        return response
        
    def example_generator(self, word: str) -> str:
        """Generate a simple example sentence in French using the given French word"""
        
        prompt = f"""/nothink Generate a very simple example sentence using the French word "{word}".
        
        Important rules:
        1. The sentence should be very simple and easy to understand
        2. Use basic vocabulary and structure
        3. Do not include any complex grammar or vocabulary
        4. Return ONLY the example sentence without any additional text or explanation
        5. Do not add english translation or commentary
        6. Sentence should be french only
        """
        
        response = self.llms["word_helper"].invoke(prompt).content.strip()
        response = re.sub(r'\([^)]*\)', '', response)
        response = re.sub(r'^[\'"]|[\'"]$', '', response)


        return response
            
        
        
llm_utils = LLMUtils()

    
        
        
        
        
        
        
        
    
    