def save_picture(picture):
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path