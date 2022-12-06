from pytube import YouTube
import pytube
import os

class Yt():

    def __init__(self):
        self.url = str(input("Enter the URL of the video you want to download: \n>>> "))


    def mp3_yt(self):
        try:
            yt = YouTube(self.url)
            # extract only audio
            video = yt.streams.filter(only_audio=True).first()
            # check for destination to save file
            destination = './output_mp3'
            # download the file
            out_file = video.download(output_path=destination)
            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file) 
            # result of success
            print(yt.title + " has been successfully downloaded in .mp3 format.")
        except Exception as err:
            print(err)


    def mp4_yt(self):
        try:
            yt = YouTube(self.url)
            #specify the starage path of video
            path_out = "./output_mp4"
            #magic line to download the video
            pytube.YouTube(self.url).streams.get_highest_resolution().download(path_out)
            # result of success
            print(yt.title + " has been successfully downloaded in .mp4 format.")
        except Exception as err:
            print(err)


def main():
    try:
        instructions =  """
        *******************************************
                DOWNLOAD MP3, MP4 FROM YT
        * Instructions:
        - Select option download
        - Enter url
        *******************************************
                        OPTIONS
        [1] MP3
        [2] MP4
        *******************************************
        """
        print(instructions)
        option = int(input("Enter the option to download: \n>>> "))
        
        if option == 1:
            url = Yt()
            url.mp3_yt()
        elif option == 2:
            url = Yt()
            url.mp4_yt()
        else:
            print("option no valid")
    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()