import json


def load_json_file():
    with open('posts.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def search_by_word(word):
    result = []
    for i in load_json_file():
        if word.lower() in i["content"].lower():
            result.append(i)
    return result


def add_post(post):
    posts = load_json_file()
    posts.append(post)
    with open('posts.json', 'w', encoding='utf-8') as file:
        json.dump(posts, file)
    return post
