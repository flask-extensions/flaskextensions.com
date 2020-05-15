import math

BASE = "SELECT " "{fields} " "FROM repos "

SEARCH = (
    "WHERE to_tsvector('simple', name || ' ' || description) "
    "@@ to_tsquery('simple', :term) "
)

ORDER = "ORDER BY stargazers_count DESC "

PAGINATION = "LIMIT {limit} OFFSET {offset}"

FIELDS = (
    "id, name, html_url, description, created_at, "
    "updated_at, stargazers_count, forks_count "
)

COUNT = "count(id) as total"


class Page(object):
    def __init__(self, items, page, page_size, total):
        self.items = items
        self.previous_page = None
        self.page_size = page_size
        self.page = page
        self.next_page = None
        self.has_previous = page > 1
        if self.has_previous:
            self.previous_page = page - 1
        previous_items = (page - 1) * page_size
        self.has_next = previous_items + len(items) < total
        if self.has_next:
            self.next_page = page + 1
        self.total = total
        self.pages = int(math.ceil(total / float(page_size)))

    def to_dict(self):
        return {
            "total": self.total,
            "page_size": self.page_size,
            "page": self.page,
            "previous": self.previous_page,
            "next": self.next_page,
            "pages": self.pages,
        }


def paginate(query, page, rpage_size):
    if page <= 0:
        raise AttributeError("page needs to be >= 1")
    if page_size <= 0:
        raise AttributeError("page_size needs to be >= 1")
    items = query.limit(page_size).offset((page - 1) * page_size).all()
    total = query.order_by(None).count()
    return Page(items, page, page_size, total)
