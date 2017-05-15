from collections import Counter

def sort_hierarhically(lemmas):
    top_ten = get_most_frequent_ten(lemmas)

def get_most_frequent_ten(_list):
    _items = map(lambda x: x.lower(), _list)
    counted_items = Counter(_items)
    return counted_items.most_common()[:10]
