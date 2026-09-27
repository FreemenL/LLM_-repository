import redis

print(redis.__version__)

r = redis.Redis(host='localhost', port=6379, db=0,decode_responses=True)

# try:
#     response = r.ping()
#     print(response)
# except Exception as e:
#     print("连接失败")

r.set("name","tom")
# r.set("gender","男")

# print(r.get("name"))
# print(r.get("gender"))
# print(r.get("hoppy"))
#
# # 带有时效的字符串
# r.set("role", "老鹰", ex=10)
# # 设置多个健至队
# r.mset({"height":175, "weight":102})
# print(r.mget(["height", "weight", "name"]))
#
#
#
# r.set("api_call_cnt", 0)
# r.incr("api_call_cnt") # +1
# r.incrby("api_call_cnt", 5) # +5
# print(r.get("api_call_cnt"))


# print(r.exists("model"))
# 设置过期时间（给已有key追加过期）
# r.expire("name", 10)

# r.hset("session:1000", mapping={
#     "user_id": "u001",
#     "model": "qwen3",
#     "last_prompt": "解释redis",
# })

# r.hset("session:1000", "status", "active")


# r.lpush("msg:history", "消息1")
# r.rpush("msg:history", "消息2", "消息3")



# 范围读取 lrange 0 -1 读取全部
# print(r.lrange("msg:history", 0, -1))

# 获取列表长度
# print(r.llen("msg:history"))
#
# # 弹出左侧第一个元素（先进先出，简易任务队列）
# print(r.lpop("msg:history"))
# # 弹出右侧最后一个元素
# print(r.rpop("msg:history"))
#
# # 按索引读取
# print(r.lindex("msg:history", 0))
# r.zadd("task:priority", {
#     "task_001": 10,
#     "task_002": 5,
#     "task_003": 20
# })
# print(r.zrange("task:priority", 0, -1))
# print(r.zrange("task:priority", 0, -1, withscores=True))
# print(r.zrevrange("task:priority", 0, -1, withscores=True))
# print(r.zcard("task:priority"))

# r.setbit("user_sign", 1, 1)
# print(r.getbit("user_sign",1))
# print(r.bitcount("user_sign"))


# r.pfadd("visit_uv", "u001", "u002", "u003")
# print(r.pfcount("visit_uv"))

# print(r.exists("test_key"))
# 设置过期时间，单位秒
# r.expire("name", 120)
# # 取消过期
# r.persist("test_key")
# # 查看剩余过期时间
# print(r.ttl("name"))
# # 切换数据库，redis 0~15一共16个db
# r.select(1)

#
# def get_llm_answer(prompt:str):
#     cache_key = f"llm_cache:{prompt}"
#     # 先查缓存
#     cached = r.get(cache_key)
#     if cached:
#         return f"【命中缓存】{cached}"
#     # 模拟调用大模型
#     llm_result = f"大模型回答：针对问题「{prompt}」的答案"
#     # 写入缓存，5分钟过期
#     r.set(cache_key, llm_result, ex=300)
#     return f"【新生成】{llm_result}"
#
# print(get_llm_answer("什么是RAG"))
# print(get_llm_answer("什么是RAG")) #第二次命中缓存

# 存储用户会话上下文（Hash）
# def save_session(session_id:str, user_id:str, history:str):
#     key = f"session:{session_id}"
#     r.hset(key, mapping={
#         "user_id": user_id,
#         "chat_history": history
#     })
#     r.expire(key, 3600*24) #会话保存1天
#
# def get_session(session_id:str):
#     return r.hgetall(f"session:{session_id}")
#
# save_session("s1001","u001","用户:你好\nAI:你好，有什么可以帮你？")
# print(get_session("s1001"))



# 简易分布式锁（大模型多进程 / 多 Agent 并发控制）

def try_lock(lock_key:str, lock_value="locked", expire=10):
    # set nx:key不存在才写入，ex过期时间，原子操作
    ok = r.set(lock_key, lock_value, nx=True, ex=expire)
    return ok

def release_lock(lock_key):
    r.delete(lock_key)

# 使用
if try_lock("llm_task_lock"):
    print("拿到锁，执行大模型任务")
    # 执行任务
    release_lock("llm_task_lock")
else:
    print("任务被其他进程占用")