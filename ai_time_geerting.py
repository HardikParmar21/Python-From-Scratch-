import datetime

def get_greeting():
  """
  This function determines the current time of day and returns an appropriate greeting.
  """
  current_time = datetime.datetime.now()
  hour = current_time.hour

  if hour < 12:
    greeting = "Good morning!"
  elif hour < 18:
    greeting = "Good afternoon!"
  else:
    greeting = "Good evening!"
  
  return greeting

# Example usage
greeting = get_greeting()
print(greeting)
