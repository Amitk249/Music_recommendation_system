import pandas as pd
import json
import os

def load_data(data_path):
    files = [f for f in os.listdir(data_path) if f.endswith('.json')]
    playlists = []
    for file in files:
        with open(os.path.join(data_path, file), 'r') as f:
            playlists.extend(json.load(f)['playlists'])
    return playlists

def preprocess_data(playlists):
    tracks = []
    for playlist in playlists:
        for track in playlist['tracks']:
            tracks.append({
                'playlist_id': playlist['pid'],
                'track_name': track['track_name'],
                'track_uri': track['track_uri'],
                'artist_name': track['artist_name'],
                'album_name': track['album_name']
            })
    
    df_tracks = pd.DataFrame(tracks)
    df_tracks.drop_duplicates(subset=['track_uri'], inplace=True)
    return df_tracks

def main():
    data_path = 'E:\\Music_recommendation_system\\data'
    playlists = load_data(data_path)
    df_tracks = preprocess_data(playlists)
    df_tracks.to_csv('E:\\Music_recommendation_system\\data\\cleaned_spotify_tracks.csv', index=False)
    print("Data cleaning and preprocessing completed. Cleaned data saved to 'E:\\Music_recommendation_system\\data\\cleaned_spotify_tracks.csv'")

if __name__ == "__main__":
    main()
