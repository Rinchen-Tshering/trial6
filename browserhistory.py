from queue import LifoQueue

backward_history = LifoQueue()
forward_history = LifoQueue()
current_page = None

#Visit function
No_of_visits = int(input("Enter the number of url history: "))
print("Enter URls to visit: ")
for i in range(No_of_visits):
    url=input("URL: ")
    print("Visiting URL{url}")
    backward_history.put(current_page)
    current_page = url

#display current page
print(f"Current Page is {current_page}")

#go back
while input("do you want to go back? (yes/no): ").lower() == 'yes':
    if not backward_history.empty():
     forward_history.put(current_page)
     current_page = backward_history.get()
     print(f"going back to {current_page}")
    else:
        print("No previous page available")

#go forward
while input("Do you want to go forward? (yes/no): ").lower() == 'yes':
   if not forward_history.empty():
      backward_history.put(current_page)
      current_page = forward_history.get()
      print(f"Page Forwarded to{current_page}")
else:
   print("No next page available")