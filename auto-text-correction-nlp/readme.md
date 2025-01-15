#  Text auto-correction for items read  using OCR 
We will be using the typos library. 
I was not able to get the compromise library to work. Compromise is a lightweight natural language processing (NLP) library perfect for this use case. 

- We are using a custom dictionary map
## OCR specific
I'll help you enhance the dictionary specifically for grocery ingredients and common OCR misreadings. Let's create an improved version focused on ingredient text recognition.




1. OCR-Specific Corrections:
   - Number/letter confusions (0/O, 1/I/l, 5/S)
   - Common scan artifacts
   - Decimal point/comma confusion
   - Percentage symbol fixes

2. Ingredient Categories:
   - Spices and Herbs (turmeric, coriander, etc.)
   - Preservatives and Additives (MSG, BHA, etc.)
   - Common Allergens (wheat, soy, nuts)
   - Measurements and Units (g, ml, kg)
   - Nutritional Terms (protein, carbohydrate)

3. Common OCR Patterns:
   - Decimal point fixes
   - Percentage symbol spacing
   - Colon standardization
   - Apostrophe normalization
