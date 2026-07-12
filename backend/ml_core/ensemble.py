class ModelEnsembler:
    """
    Combines predictions from multiple models (Voting Classifier).
    1. Random Forest (Structured Data)
    2. Neural Network (Unstructured Data)
    3. Rule-Based Engine (Safety Constraints)
    """
    
    def weighted_average(self, predictions, weights):
        # Calculates final probability score based on model confidence
        total_score = sum(p * w for p, w in zip(predictions, weights))
        return total_score / sum(weights)

    def safety_override(self, ai_prediction, rule_based_flag):
        """
        If Rule-Based engine flags an emergency, override AI.
        Safety First Architecture.
        """
        if rule_based_flag == "EMERGENCY":
            return "Seek Immediate Medical Attention"
        return ai_prediction