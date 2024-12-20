def get_weather_and_recommend_clothing():
    weather_description = input("What's the weather like today?(sunny/rainy/cold):")
    if"sunny"in weather_description:
        print("Wear a t-shirt and sunglasses.")
    elif"rainy" in weather_description:
        print("Don't forget your umbrella and a raincoat.")
    elif"cold"in weather_description:
        print("Make sure to wear a warm coat and a scarf.")
    else:
        print("Sorry, I don't have recommendations for this weather.")
if __name__ == "__main__":
    get_weather_and_recommend_clothing()