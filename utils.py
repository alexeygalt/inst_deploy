import json


def get_posts_all() -> list:
    """Получение всех постов из файла json"""
    with open('./data/data.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_comments_all() -> list:
    """Получение всех комментариев из файла json"""
    with open('./data/comments.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_by_user(user_name) -> list:
    """ Возвращает посты определенного пользователя """
    if not isinstance(user_name, str):
        raise TypeError('Имя пользователя - str!')

    result = [item for item in get_posts_all() if user_name == item['poster_name']]
    if not result:
        raise ValueError('Такого пользователя нет, либо он еще не сделал ни одного  поста')

    return result


def get_comments_by_post_id(post_id) -> list:
    """Возвращает комментарии определенного поста"""
    if not isinstance(post_id, int):
        raise TypeError('Идентификатор - целое число!')

    result = [item for item in get_comments_all() if post_id == item['post_id']]
    if not result:
        raise ValueError('Такого поста нет, либо у него еще нет ни одного комментария')

    return result


def search_for_posts(query) -> list:
    """ Возвращает список постов по ключевому слову"""
    if not isinstance(query, str):
        raise TypeError('Ключевое слово - str!')
    result = [item for item in get_posts_all() if query.lower() in item['content'].lower()]
    return result


def get_post_by_pk(pk) -> list:
    """Возвращает один пост по его идентификатору."""
    if not isinstance(pk, int):
        raise TypeError('Идентификатор - целое число!')
    result = [item for item in get_posts_all() if pk == item['pk']]
    return result


def get_tags_words(key_list) -> list:
    """Добавление ссылок на все слова хэштеги в посте"""
    result = []
    for key in key_list:
        for item in key['content'].split():
            if item.startswith('#'):
                result.append(f'<a href="/tag/{item[1:]}">{item}</a>')
            else:
                result.append(item)

    key_str = ' '.join(result)
    key_list[0]['content'] = key_str
    return key_list


def search_for_tag(query) -> list:
    """ Поиск постов содержащих хэштег"""
    if not isinstance(query, str):
        raise TypeError('Ключевое слово - str!')
    key = '#' + query
    result = [item for item in get_posts_all() if key.lower() in item['content'].lower()]
    return result


def get_bookmark_json() -> list:
    """Получение всех закладок из файла json"""
    with open('./data/bookmarks.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def add_bookmark(index):
    """ Добавление закладки в файл json """
    bookmarks = get_bookmark_json()
    bookmark = get_post_by_pk(index)[0]
    if bookmark not in bookmarks:
        bookmarks.append(bookmark)

    with open('./data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file, ensure_ascii=False)

    return index


def remove_bookmark(index):
    """Удаление закладки из файла json"""
    bookmarks = get_bookmark_json()
    bookmark = get_post_by_pk(index)[0]
    if bookmark in bookmarks:
        bookmarks.remove(bookmark)

    with open('./data/bookmarks.json', 'w', encoding='utf-8') as file:
        json.dump(bookmarks, file, ensure_ascii=False)

    return index
