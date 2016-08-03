from PL import Picture,ScreenShot

def find_picture_locations(pictures, picture = "SS"):
    bboxs = {}
    if picture == "SS":
        picture = ScreenShot()

    for path in pictures:
        bbox = picture.contains(Picture(path))
        bboxs[path] = bbox

    return bboxs

bboxes = find_picture_locations(["coin.png",])
print(bboxes)