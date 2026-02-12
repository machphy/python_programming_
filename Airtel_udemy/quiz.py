#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quiz/Parsh Program - लोगों को सवाल पूछने के लिए
"""

def run_quiz():
    """Quiz को चलाता है और score track करता है"""
    
    # Questions list - सवाल, विकल्प, सही उत्तर
    questions = [
        {
            "question": "Python का निर्माता कौन है?",
            "options": ["A) Guido van Rossum", "B) Dennis Ritchie", "C) Bjarne Stroustrup", "D) Mark Zuckerberg"],
            "correct": "A"
        },
        {
            "question": "Python का सर्वपहला version कब release हुआ?",
            "options": ["A) 1989", "B) 1991", "C) 1995", "D) 2000"],
            "correct": "B"
        },
        {
            "question": "निम्नलिखित में कौन एक valid variable name है?",
            "options": ["A) 1var", "B) var-1", "C) var_1", "D) var.1"],
            "correct": "C"
        },
        {
            "question": "Python में कितने fundamental data types हैं?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "correct": "C"
        },
        {
            "question": "List को duplicate करने का सही तरीका क्या है?",
            "options": ["A) list2 = list1", "B) list2 = list1.copy()", "C) list2 = list(list1)", "D) B और C दोनों"],
            "correct": "D"
        }
    ]
    
    print("=" * 50)
    print("         🎯 PYTHON QUIZ PROGRAM 🎯")
    print("=" * 50)
    print(f"\nकुल सवाल: {len(questions)}")
    print("हर सवाल के लिए सही विकल्प चुनें (A, B, C, या D)")
    print("=" * 50)
    
    score = 0
    
    # सभी सवाल पूछना
    for i, q in enumerate(questions, 1):
        print(f"\nसवाल {i}: {q['question']}")
        for option in q['options']:
            print(f"  {option}")
        
        while True:
            user_answer = input("\nआपका उत्तर (A/B/C/D): ").upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            print("❌ गलत input! कृपया A, B, C, या D दर्ज करें।")
        
        if user_answer == q['correct']:
            print("✅ सही उत्तर!")
            score += 1
        else:
            print(f"❌ गलत उत्तर। सही उत्तर: {q['correct']}")
    
    # Results
    print("\n" + "=" * 50)
    print("         📊 QUIZ RESULTS 📊")
    print("=" * 50)
    print(f"\nआपका स्कोर: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage == 100:
        print("\n🌟 शानदार! आप एक Python Expert हो! 🌟")
    elif percentage >= 80:
        print("\n👍 बहुत अच्छा! आपका ज्ञान बेहतरीन है।")
    elif percentage >= 60:
        print("\n😊 ठीक है! थोड़ा और अभ्यास करें।")
    else:
        print("\n💪 Python सीखते रहें, जल्द ही बेहतर हो जाएंगे!")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    run_quiz()
