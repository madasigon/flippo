from flask import abort
import random, string

from flippo import redis_store


def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


class RedisFlip:  # osztaly a Redis adatbazis hasznalatahoz
    inventory_id = 'flips_all'

    def __init__(self, code):
        self.code = code
        self.set_id = 'flip-visits:%s' % code
        self.result_id = 'flip-result%s' % code
        self.size_id = 'flip-size%s' % code

    @classmethod
    def load(cls, code):
        if not redis_store.sismember(cls.inventory_id, code): abort(404, 'Flip non-existent!')
        return cls(code)

    @classmethod
    def make_new(cls, size):
        code = random_word(10)
        redis_store.sadd(cls.inventory_id, code)
        new = cls(code)
        redis_store.set(new.size_id, size)
        redis_store.set(new.result_id, random.choice([0,1]))
        return new

    def visits(self):
        return redis_store.scard(self.set_id)

    def size(self):
        return int(redis_store.get(self.size_id))

    def add_visit(self, ident):
        if redis_store.sismember(self.set_id, ident): return
        if self.visits() < self.size(): redis_store.sadd(self.set_id, ident)
        else: abort(403, 'This coin has already been flipped!')

    def done(self):
        return self.visits() == self.size()

    def result(self):
        return ['head','tails'][int(redis_store.get(self.result_id))]


class PythonFlip:  # osztaly, ami egy Python dict-et hasznal a cel maegvalositasahoz
    all = dict()

    def __init__(self, code, size):
        self.set = set([])
        self.result_ = random.choice([0,1])
        self.size_ = size
        self.code = code

    @classmethod
    def make_new(cls, size):
        code = random_word(10)
        new = cls(code, size)
        cls.all[code] = new
        return new

    @classmethod
    def load(cls, code):
        if code not in cls.all:
            abort(404, 'Flip non-existent!')
        return cls.all[code]

    def visits(self):
        return len(self.set)

    def size(self):
        return self.size_

    def add_visit(self, ident):
        if ident in self.set: return
        if self.visits() < self.size(): self.set.add(ident)
        else: abort(403, 'This coin has already been flipped!')

    def done(self):
        return self.visits() == self.size()

    def result(self):
        return ['head','tails'][self.result_]


Flip = PythonFlip # PythonFlip: python dict, RedisFlip: Redis adatbazis
