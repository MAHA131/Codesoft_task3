print("===================================")
print("      Movie Recommendation System")
print("===================================\n")

movies = {
    "action": [
        "John Wick",
        "Avengers",
        "Mad Max",
        "The Dark Knight"
    ],

    "comedy": [
        "3 Idiots",
        "The Mask",
        "Home Alone",
        "Dhamaal"
    ],

    "horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle",
        "It"
    ],

    "romance": [
        "Titanic",
        "The Notebook",
        "La La Land",
        "Veer-Zaara"
    ],

    "science fiction": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Gravity"
    ]
}

while True:

    print("\nAvailable genres:")
    for genre in movies:
        print("-", genre)

    print()

    
    user_choice = input(
        "Enter your favorite genre: "
    ).lower().strip()

    print()

    
    if user_choice in movies:

        print("Recommended movies for you:\n")

        
        for movie in movies[user_choice]:
            print("-", movie)

        print()

        
        while True:

            selected_movie = input(
                "Enter the movie name you want to watch: "
            ).strip()

            print()

            if selected_movie in movies[user_choice]:
                print("Great choice!")
                print("You selected:", selected_movie)

            else:
                print("Movie not found in this genre.")

            print()

            
            another_movie = input(
                "Do you want to select another movie? (yes/no): "
            ).lower().strip()

            print()

            if another_movie == "yes":
                continue
            else:
                break

    else:
        print("Genre not found.")
        print("Please choose a valid genre.")

    
    another_genre = input(
        "Do you want to choose another genre? (yes/no): "
    ).lower().strip()

    if another_genre != "yes":
        print("\nThank you for using Movie Recommendation System!")
        break