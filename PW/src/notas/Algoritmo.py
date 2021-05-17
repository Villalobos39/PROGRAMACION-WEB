from collections import Counter
import math

def knn(data, query, k, distance_fn, choice_fn):
    neighbor_distances_and_indices = []
    
    # 3. Para cada ejemplo en los datos
    for index, example in enumerate(data):
        # 3.1 Calcule la distancia entre el ejemplo de consulta y el actual
        # ejemplo de los datos.
        distance = distance_fn(example[:-1], query)
        
        # 3.2 Agrega la distancia y el índice del ejemplo a una colección ordenada
        neighbor_distances_and_indices.append((distance, index))
    
    # 4. Ordene la colección ordenada de distancias e índices de
    # de menor a mayor (en orden ascendente) por las distancias
    sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
    
    # 5. Elija las primeras K entradas de la colección ordenada
    k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]
    
    # 6. Obtenga las etiquetas de las entradas K seleccionadas
    k_nearest_labels = [data[i][-1] for distance, i in k_nearest_distances_and_indices]

    # 7. Si la regresión (choice_fn = mean), devuelve el promedio de las K etiquetas
    # 8. Si la clasificación (choice_fn = mode), devuelve el modo de las etiquetas K
    return k_nearest_distances_and_indices , choice_fn(k_nearest_labels)

def mean(labels):
    return sum(labels) / len(labels)

def mode(labels):
    return Counter(labels).most_common(1)[0][0]

def euclidean_distance(point1, point2):
    sum_squared_distance = 0
    for i in range(len(point1)):
        sum_squared_distance += math.pow(point1[i] - point2[i], 2)
    return math.sqrt(sum_squared_distance)

def main():
    '''
    # Regression Data
    # 
    # Column 0: height (inches)
    # Column 1: weight (pounds)
    '''
    reg_data = [
       [65.75, 112.99],
       [71.52, 136.49],
       [69.40, 153.03],
       [68.22, 142.34],
       [67.79, 144.30],
       [68.70, 123.30],
       [69.80, 141.49],
       [70.01, 136.46],
       [67.90, 112.37],
       [66.49, 127.45],
    ]
    
    # Pregunta:
    # Dados los datos que tenemos, ¿cuál es la mejor estimación del peso de una persona si mide 60 pulgadas de alto?
    reg_query = [60]
    reg_k_nearest_neighbors, reg_prediction = knn(
        reg_data, reg_query, k=3, distance_fn=euclidean_distance, choice_fn=mean
    )
    
    '''
    # Classification Data
    # 
    # Column 0: age
    # Column 1: likes pineapple
    '''
    clf_data = [
       [22, 1],
       [23, 1],
       [21, 1],
       [18, 1],
       [19, 1],
       [25, 0],
       [27, 0],
       [29, 0],
       [31, 0],
       [45, 0],
    ]
    # Pregunta:
    # Dados los datos que tenemos, ¿a un joven de 33 años le gustan las piñas en su pizza?
    clf_query = [33]
    clf_k_nearest_neighbors, clf_prediction = knn(
        clf_data, clf_query, k=3, distance_fn=euclidean_distance, choice_fn=mode
    )

if __name__ == '__main__':
    main()