class BufferManager:
    def __init__(self, buffer_size):
        self.buffer_size = buffer_size
        self.buffer = []

    def add_data(self, data):
        if len(self.buffer) >= self.buffer_size:
            self.buffer.pop(0)  # Remove the oldest data
        self.buffer.append(data)

    def get_buffer(self):
        return self.buffer

class DecisionEngine:
    def __init__(self, threshold):
        self.threshold = threshold

    def make_decision(self, current_data):
        # Example decision logic based on current data.
        if current_data > self.threshold:
            return "Record"
        else:
            return "Do not Record"

# Example usage:
# buffer_manager = BufferManager(buffer_size=10)
# decision_engine = DecisionEngine(threshold=5)
# 
# buffer_manager.add_data(3)
# decision = decision_engine.make_decision(6)
# print(decision)  # Output: Record
