from functools import wraps
import time

class color:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'
 
def my_timer(original_function):
  @wraps(original_function)
  def wrapper(*args, **kwargs):
    t1 = time.time()
    result = original_function(*args, **kwargs)
    t2 = time.time() - t1
    print('[' + color.RED + original_function.__name__ + color.END + '] function execution time: {}'.format(str(datetime.timedelta(seconds=t2))))
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
