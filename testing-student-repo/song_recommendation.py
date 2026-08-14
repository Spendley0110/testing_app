import kagglehub

# Download latest version
path = kagglehub.dataset_download("joebeachcapital/30000-spotify-songs")

print("Path to dataset files:", path)
#I moved the csv file to the free_coding folder

def read_file(csv):
    "reads the csv file dataset and splits it into lists by '\n'."
    with open(csv, "r") as file:
        csv_file = file.readlines()
        new_csv = []
        id_list = []
        for i in csv_file:
            new_i = i.split(',')
            if new_i[0] in id_list:
                continue
            new_csv.append(new_i)
            id_list.append(new_i[0])
    return new_csv

def make_dictionary(csv_file):
    dict_list = []
    for i in range(1,len(csv_file)):
        if len(csv_file[i]) == 23:
            dict = {
                'track_id': csv_file[i][0],
                'track_name': csv_file[i][1],
                'track_artist': csv_file[i][2],
                'track_popularity': csv_file[i][3],
                'genre': csv_file[i][9],
                'danceability': csv_file[i][11],
                'energy': csv_file[i][12],
                'key': csv_file[i][13],
                'loudness': csv_file[i][14],
                'speechiness': csv_file[i][16],
                'acousticness': csv_file[i][17],
                'instrumentness': csv_file[i][18],
                'liveness': csv_file[i][19],
                'valence': csv_file[i][20],
                'tempo': csv_file[i][21],
            }
            dict_list.append(dict)

    return dict_list

def input_preference():
    while True:
        try:
            energy = int(input("Do you like energetic songs? Rate from 1(low) to 3(high)\n"))
            if energy not in [1, 2, 3]:
                raise ValueError
            genre = input("What kind of genre do you prefer? Choose from: edm ,r&b, latin, rock, rap, pop\n")
            tempo = int(input("Do you like fast tempo or slow tempo? Type 1 for fast and 2 for slow\n"))
            if tempo not in [1, 2]:
                raise ValueError
            popularity = input("Looking for top track songs or want to discover new songs? Type T or N\n")
            if popularity.upper() not in ['T', 'N']:
                raise ValueError
            return energy, genre, tempo, popularity
        except ValueError:
            print("Invalid input. Please try again.")
    return energy, genre, tempo, popularity

def filter_energy(energy,dict_list):
    energy_list = []
    if energy == 1:
        for dict in dict_list:
            if float(dict["energy"]) <= 0.3:
                energy_list.append(dict)
    elif energy == 2:
        for dict in dict_list:
            if float(dict["energy"]) <= 0.6:
                energy_list.append(dict)
    elif energy == 3:
        for dict in dict_list:
            if float(dict["energy"]) > 0.6:
                energy_list.append(dict)
    return energy_list

def filter_genre(genre, energy_list):
    genre_and_energy = []
    for dict in energy_list:
        if dict['genre'] == genre:
            genre_and_energy.append(dict)
    return genre_and_energy

def filter_tempo(tempo, genre_and_energy):
    temp_genre_energy = []
    if tempo == 1:
        for dict in genre_and_energy:
            if float(dict["tempo"]) <= 80:
                temp_genre_energy.append(dict)
    elif tempo == 2:
        for dict in genre_and_energy:
            if float(dict["tempo"]) <= 120:
                temp_genre_energy.append(dict)
    elif tempo == 3:
        for dict in genre_and_energy:
            if float(dict["tempo"]) > 120:
                temp_genre_energy.append(dict)
    return  temp_genre_energy


def recommend_song_popular_or_no(popularity, tempo_genre_energy):
    if popularity == 'Y':
        popularity_sorted = sorted(tempo_genre_energy, key = lambda x: x["track_popularity"])
        return popularity_sorted
    else:
        popularity_sorted = sorted(tempo_genre_energy, key = lambda x: x["track_popularity"], reverse = True)
        return popularity_sorted




def main():
dataset = 'spotify_songs copy.csv'
    dict_data = make_dictionary(dataset_list)
    #print(dict_data)
    energy, genre, tempo, popularity = input_preference()
    energy_list = filter_energy(energy,dict_data)
    genre_and_energy = filter_genre(genre, energy_list)
    tempo_and_genre_and_energy = filter_tempo(tempo, genre_and_energy)
    popularity_sorted = recommend_song_popular_or_no(popularity, tempo_and_genre_and_energy)
    print("Try these 5 songs!")
    for dict in popularity_sorted[:5]:
        print(f"{dict["track_name"]} by {dict["track_artist"]} id: {dict["track_id"]}")






if __name__ == '__main__':
    main()
