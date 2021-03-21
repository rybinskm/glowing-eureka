def movie_path(movie):
    """
    Function, which returns full path to correct movie file.
    movie:
        File name with the file extension.
    path:
        String with path to the movie folder.
    :return:
        Full path included movie file.
    """
    path = "C:\\Repo\\Videos\\"
    full_movie_path = f"{path}{movie}"
    return full_movie_path
