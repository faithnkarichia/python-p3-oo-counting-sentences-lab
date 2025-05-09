#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # Will use the setter below

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value



    def is_sentence(self):
       return self.value.endswith(".")
    
    def is_question(self):
        return self.value.endswith("?")
    
    def is_exclamation(self):
        return self.value.endswith("!")
    def count_sentences(self):
      
       

        sentences = re.split(r'[.!?]', self.value)
        cleaned = [s.strip() for s in sentences if s.strip()]
        return len(cleaned)
        
    

      
       

