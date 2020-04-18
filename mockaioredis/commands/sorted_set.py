class SortedSetCommandsMixin:
    async def zadd(self, key, score, member):
        return self._redis.zadd(key, **{member: score})

    async def zrevrange(self, key, start, stop, withscores=False):
        return self._redis.zrevrange(key, start, stop, withscores=withscores)
