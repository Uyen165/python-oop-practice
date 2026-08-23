class ModelTrainer:
    def __init__(self, model_name):
        self.model_name = model_name

    def fit_data(self, importances):
        self._feature_importances = importances

    def get_importance(self):
        if hasattr(self, "_feature_importances"):
            return self._feature_importances
        else:
            print("Model chua duoc huan luyen!")
            return None
if __name__ == "__main__":
    m1 = ModelTrainer("Mo hinh 1")
    print(m1.get_importance())

    m2 = ModelTrainer("Mo hinh 2")
    m2.fit_data([0.1, 0.4, 0.5])
    print(m2.get_importance())