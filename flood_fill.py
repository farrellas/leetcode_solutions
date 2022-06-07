def floodFill(image, sr, sc, newColor):
    # save old color to check surrounding squares
    oldColor = image[sr][sc]
    if oldColor == newColor:
        return image
    # change color
    image[sr][sc] = newColor
    # set a list of neighboring squares
    neighbors = [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]
    for location in neighbors:
        if 0 <= location[0] < len(image) and 0 <= location[1] < len(image[0]):
            if  image[location[0]][location[1]] == oldColor:
                floodFill(image, location[0], location[1], newColor)

    return image