conditions = ["sunny", "rainy", "cold"]
a = input("What's the weather like today? (sunny/rainy/cold): ").lower ()
print(a)
if a == "sunny":
    print ("Wear a t-shirt and sunglasses.")
elif a == "rainy":
    print( "Don't forget your umbrella and a raincoat.")
elif a == "cold":
    print("Make sure to wear a warm coat and a scarf." )
else :
    print("Sorry, I don't have recommendations for this weather.")

