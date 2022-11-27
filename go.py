import tidalapi
import pathlib


class CtrlTidal():
    """Interface to Tidal account
    """
    def __init__(self) -> None:
        """starts a Tidal session
        """
        self.session = session = tidalapi.Session()
        session.login_oauth_simple()

    def searchForSong(self, songTitle: str):
        """searches for a song in Tidal

        Args:
            songTitle (str): Title and Artist of song

        Returns:
            tidalapi.tracks: tracks
        """
        models = list()
        models.append(tidalapi.media.Track)
        res = self.session.search(songTitle, models=models)
        return res["tracks"]
    
    def genPlaylist(self, playlistName: str, songs: list):
        playlist = self. session.user.create_playlist(playlistName, "An example of a playlist")
        for song in songs:
            tracks = self.searchForSong(song)
            if tracks:
                t1 = tracks[0]
                playlist.add([t1.id])
            else:
                print("could not find song")
    
    
def readSonglist(fName: pathlib.Path):
    with open(fName) as file:
        lines = [line.rstrip() for line in file]
    return lines

def main():
    # songs = ["Pierce The Veil - A Match Into Water",
    #         "Riff Raff - Tip Toe Wing In My Jawwdinz",
    #         "PVRIS - My House",
    #         "As It Is - Cheap Shots & Setbacks",
    #         "Black Veil Brides - Crown Of Thorns",
    #         "August Burns Red - The Wake",
    #         "We Came As Romans - Regenerate",
    #         "BlessTheFall - Youngbloods",
    #         "Memphis May Fire - My Generation",
    #         "Miss May I - Gone",
    #         "Amity Affliction - Don't Lean On Me",
    #         "Silverstein - A Midwestern State of Emergency",
    #         "I Killed The Prom Queen - Thirty-One & Sevens",
    #         "'68 - The Human Calculus",
    #         "Senses Fail - All You Need Is Already Within You",
    #         "H2O - Nothing To Prove",
    #         "Beartooth - Dead",
    #         "Rotting Out - Born",
    #         "Fit For A King - Hooked",
    #         "Hundredth - See Beyond",
    #         "Handguns - Heart vs. Head",
    #         "Beautiful Bodies - Invincible",
    #         "Slaves - Starving For Friends (Feat. Vic Fuentes)",
    #         "Our Last Night - I've Never Felt This Way",
    #         "Koo Koo Kanga Roo - Fanny Pack",
    #         "The Wonder Years - There, There",
    #         "PUP - Reservoir",
    #         "Citizen - Cement",
    #         "Moose Blood - Bukowski",
    #         "Knuckle Puck - Bedford Falls",
    #         "Mod Sun - My Hippy (Feat. Dizzy Wright)",
    #         "Man Overboard - Let It Go Back",
    #         "Neck Deep - Mileage",
    #         "Never Shout Never - Boom!",
    #         "Metro Station - Savior",
    #         "Baby Baby - Circus",
    #         "Lee Corey Oswald - Always Never",
    #         "The Dirty Nil - Nicotine",
    #         "Major League - Kaleidoscopes",
    #         "Seaway - Your Best Friend",
    #         "Have Mercy - Howl",
    #         "This Wild Life - No More Bad Days",
    #         "Trophy Eyes - My Name On Paper",
    #         "Set It Off - Forever Stuck In Our Mouth",
    #         "Hands Like Houses - I Am",
    #         "Being As An Ocean - The Poets Cry For More",
    #         "Candy Hearts - All The Ways You Let Me Down",
    #         "MC Lars - Never Afraid (Feat. Watsky)",
    #         "Kosha Dillz - Hangin Out",
    #         "New Beat Fund - Sunday Funday"]
    fName = pathlib.Path(r'C:\Users\Blade\Documents\Coding\Python\TidalIF\ListOfSongs.txt')
    songs = readSonglist(fName)
    dummy = CtrlTidal()
    dummy.genPlaylist(songs[0], songs[1:])

if __name__ == "__main__":
    main()