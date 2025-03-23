knowledge_base = {

    "Influenza": ["fever", "cough", "body aches", "fatigue", "headache"],
    "COVID-19": ["fever", "cough", "fatigue", "loss of taste or smell", "shortness of breath"],
    "Malaria": ["fever", "chills", "sweating", "headache", "nausea"],
    "Common Cold": ["runny nose", "sore throat", "cough", "sneezing", "fatigue"],
    "Pneumonia": ["cough", "fever", "chest pain", "shortness of breath", "fatigue"]


}
def diagnose(symptoms, knowledge_base):

    results = {}
    for disease, disease_symptoms in knowledge_base.items():
        match_count = sum(1 for symptom in symptoms if symptom in disease_symptoms)
        results[disease] = match_count

    return results

def suggest_diagnosis(results):

    best_match = max(results, key=results.get)
    return best_match
def get_symptoms():
    print("Enter your symptoms (separated by commas):")
    symptoms_string = input().lower()
    symptoms = [s.strip() for s in symptoms_string.split(",")]
    return symptoms

def main():
    symptoms = get_symptoms()
    results = diagnose(symptoms, knowledge_base)
    diagnosis = suggest_diagnosis(results)

    print("Possible diagnosis:", diagnosis)

if __name__ == "__main__":
    main()