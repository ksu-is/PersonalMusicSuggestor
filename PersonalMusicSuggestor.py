def get_playlist_recommendation(score):
#Determines playlist recommendation based on the score.
    if score['jazz_fusion'] >= max(score.values()):
        return "Jazz Fusion Playlist: Includes Return to Forever, Weather Report, Mahuvishnu Orchestra."
    elif score['prog_rock'] >= max(score.values()):
        return "Prog Rock Playlist: Features Pink Floyd, Yes, King Crimson."
    elif score['smooth_jazz'] >= max(score.values()):
        return "Smooth Jazz Playlist: Offers tracks from George Benson, Masayoshi Takanaka, Dave Koz."
    elif score['japanese_jazz'] >= max(score.values()):
        return "Japanese Jazz Playlist: Features Casiopea, T-Square, Cortex."

def main():
    questions = [
        ("Do you enjoy music with a lot of instrumental complexity?", 'prog_rock', 'jazz_fusion'),
        ("Do you prefer soothing melodies and smooth rhythms?", 'smooth_jazz', 'japanese_jazz'),
        ("Are you interested in unique and innovative music styles?", 'jazz_fusion', 'japanese_jazz'),
        ("Do you like epic and thematic music compositions?", 'prog_rock', 'smooth_jazz')
    ]
    score = {'jazz_fusion': 0, 'prog_rock': 0, 'smooth_jazz': 0, 'japanese_jazz': 0}

    print("Welcome to the Music Genre Recommendation Quiz!\nAnswer the following questions to find out which playlist to listen to next.")

    for question, if_yes, if_no in questions:
        answer = input(question + " (yes/no) ").strip().lower()
        if answer == "yes":
            score[if_yes] += 1
        elif answer == "no":
            score[if_no] += 1
        else:
            print("Invalid response, please answer 'yes' or 'no'.")
    
    recommendation = get_playlist_recommendation(score)
    print("\nBased on your answers, we recommend the following music playlist:")
    print(recommendation)

if __name__ == "__main__":
    main()
