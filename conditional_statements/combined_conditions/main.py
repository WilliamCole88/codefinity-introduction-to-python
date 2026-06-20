# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = True
promotion = discounted or not lowStock
print("Is the item eligible for promotion? ", promotion)