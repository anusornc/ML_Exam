import numpy as np

# สร้างข้อมูลตัวอย่าง
heights = np.array([150, 160, 170, 180, 190])  # ส่วนสูง (cm)
weights = np.array([45, 55, 65, 75, 85])  # น้ำหนัก (kg)

# Normalize ข้อมูลให้มีค่าเฉลี่ย 0 และค่าเบี่ยงเบนมาตรฐาน 1
heights = (heights - np.mean(heights)) / np.std(heights)

# กำหนดค่า learning rate และจำนวนรอบ
learning_rate = 0.01
iterations = 1000

# สร้างฟังก์ชันสำหรับทำนายน้ำหนัก
def predict(X, w, b):
    return np.array(X) * w + b

# สร้างฟังก์ชันคำนวณ Mean Squared Error
def compute_cost(X, y, w, b):
    predictions = predict(X, w, b)
    return np.mean((predictions - y) ** 2)

# เริ่มต้นค่า weight และ bias
w = 0.0
b = 0.0

# ทำการเรียนรู้
for i in range(iterations):
    # คำนวณค่าทำนาย
    predictions = predict(heights, w, b)
    
    # คำนวณ gradients
    dw = (2 / len(heights)) * np.sum( เติม code )
    db = (2 / len(heights)) * np.sum( เติม code )
    
    # ปรับค่า weight และ bias
    w -= learning_rate * dw
    b -= learning_rate * db

    # Debugging: ดูค่า cost ทุก 100 iterations
    if i % 100 == 0:
        cost = compute_cost(heights, weights, w, b)
        print(f"Iteration {i}: Cost {cost:.4f}, w: {w:.4f}, b: {b:.4f}")

# ค่า Final weight และ bias
print(f"Final weight (w): {w:.4f}")
print(f"Final bias (b): {b:.4f}")

# ทดสอบทำนายน้ำหนักจากส่วนสูง
test_height = 175
normalized_test_height = (test_height - np.mean([150, 160, 170, 180, 190])) / np.std([150, 160, 170, 180, 190])
predicted_weight = predict(normalized_test_height, w, b)
print(f"Predicted weight for height {test_height}cm: {predicted_weight:.2f}kg")
