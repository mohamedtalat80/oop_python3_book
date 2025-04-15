import sys
def save_data():
    print("saving data")
try:
    print("Running program...")
    user_input = int(input("Enter a number to divide 10 by: "))
    result = 10 / user_input
    print(f"Result: {result}")
    if input("Type 'exit' to quit: ") == "exit":
        sys.exit("Exiting...")
except SystemExit as e:  # بيعلق كل حاجة، لكن بوضوح
    print(f"Caught System exit : {e}")
    save_data()
    raise 
finally:
    print ("there is a thing being saved ",)
