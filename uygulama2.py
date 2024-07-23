import math

def oklid_mesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0])**2 + (nokta2[1] - nokta1[1])**2)

# Örnek kullanım
nokta1 = (1, 2)
nokta2 = (4, 6)

mesafe = oklid_mesafesi(nokta1, nokta2)
print("İki nokta arasındaki Öklid mesafesi:", mesafe)


#d = √(x₂-x₁)²+(y₂-y₁)² formülüne göre
import math

def oklid_mesafesi(nokta1, nokta2):
    # Formül: d = √((x₂ - x₁)² + (y₂ - y₁)²)
    x1, y1 = nokta1
    x2, y2 = nokta2
    mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return mesafe

# Örnek kullanım
nokta1 = (1, 2)
nokta2 = (4, 6)

mesafe = oklid_mesafesi(nokta1, nokta2)
print("İki nokta arasındaki Öklid mesafesi:", mesafe)




import math

# Öklid Mesafesi Hesaplayan Fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 8), (9, 10)]

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)
print("Minimum Öklid Mesafesi:", min_distance)
