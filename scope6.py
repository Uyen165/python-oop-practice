class CustomClassifier:
    def __init__(self, model_name):
        self.model_name = model_name
    def create_predictor(self, threshold):
        
        def predictor(scores_list):
            nonlocal threshold
            result = []
            for x in scores_list:
                if x >= threshold:
                    y = 1
                    result.append(y)
                else: 
                    y = 0
                    result.append(y)
            return result
        return predictor

data = [0.2, 0.6, 0.9]
doituong = CustomClassifier("Model")
ai = doituong.create_predictor(0.5)
print(ai(data)) #[0,1,1]
ai1 = doituong.create_predictor(1)
print(ai1(data)) #[0,0,0]

            