class ModelEvaluator:
    def __init__(self, model_name, history_scores=None):
        self.model_name = model_name
        #Tránh bẫy Mutable Default Argument cho list, không bao giờ được dùng [] hay {} làm default value
        #Trường hợp ta không chủ động truyền danh sách, nó sẽ tạo mới từ đầu
        if history_scores is None:
            self.history_scores = []
        #Trường hợp ta chủ động truyền danh sách vào đầu vào
        else:
            self.history_scores = history_scores
    def add_score(self, score):
        self.history_scores.append(score)
eval1 = ModelEvaluator("ResNet")
eval2 = ModelEvaluator("VGG", [0.2, 0.4])
eval1.add_score(0.9)
eval2.add_score(0.5)
print(eval1.history_scores)
print(eval2.history_scores)