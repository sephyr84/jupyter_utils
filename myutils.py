from functools import wraps
import time

def my_timer(original_function):
  @wraps(original_function)
  def wrapper(*args, **kwargs):
    t1 = time.time()
    result = original_function(*args, **kwargs)
    t2 = time.time() - t1
    print('[ {} ] function execution time: {:10.4f} sec'.format(original_function.__name__, t2))
    return result
  return wrapper

def my_loader(original_function):
  @wraps(original_function)
  def wrapper(*args, **kwargs):
    result = original_function(*args, **kwargs)
    print('total_count: {:,}'.format(len(result))
    return result
  return wrapper

@my_loader
@my_timer
def as_pandas(cursor):
  return pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])
