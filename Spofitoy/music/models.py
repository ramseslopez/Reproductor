from django.db import models

# Create your models here.

class Artist(models.Model):
    """
    Artist model
    """

    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = "artists/images", null = True)


    def __str__(self):
        """
        Get str representation
        """
        return self.name

    def __repr__(self):
        """ 
        Get str representation 
        """
        return self.__str__()


class Song(models.Model):
    """
    Song model
    """

    name = models.CharField(max_length = 200)
    song_file = models.FileField(null = True, upload_to = "songs")

    # Relations
    artists = models.ManyToManyField("music.Artist", related_name = "songs")

    def __str__(self):
        """
        Get str representation
        """
        artists_str = ""
        artists = list(self.artists.all())
        if len(artists) == 0:
            return f"{self.name}"
        artists_str = f"{artists[0].name}"
        for artist in artists[1:]:
            artists_str += f", {artist.name}"
        return f"{self.name} por {artists_str}"

    def __repr__(self):
        """
        Get str representation
        """
        return self.__str__()