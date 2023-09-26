

def linearSearchProduct(productList, targetProduct):
  indices = []

  for index, product in enumerate(productList):
    if product == targetProduct:
      indices.append(index)

  return indices

#example usage:
products = ["Shoes" , "boat" , "loafer", "Shoes" , "Sandal" , "Shoes"]
target="Shoes"
result = linearSearchProduct(products, target)
print(result)