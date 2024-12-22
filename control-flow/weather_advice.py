def get_clothing_recommendation():
    weather_conditions = ["sunny", "rainy", "cold"]
user = input("What's the weather like today?(sunny/rainy/cold):")

if user =="sunny":
        print("Wear a t-shirt and sunglasses.")
elif user=="rainy":
        print("Don't forget your umbrella and a raincoat.")
elif user=="cold":
        print("Make sure to wear a warm coat and a scarf.")
else:
        print("Sorry, I don't have recommendations for this weather.")
if __name__=="__main__":
    weather = get_clothing_recommendation()