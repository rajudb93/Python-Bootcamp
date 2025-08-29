# Smart Token Dispenser Generator
def token_dispenser(start=1):
    token = start
    try:
        while True:
            reset = yield token
            if reset is not None:
                token = reset
            else:
                token += 1
    except GeneratorExit:
        print("Dispenser closed.")


# ---------------------------
# Calling / Driver function
# ---------------------------
def main():
    gen = token_dispenser(1)   # start from 1
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3

    # Reset token using send()
    print(gen.send(10))  # Reset to 10 → yields 10
    print(next(gen))     # 11
    print(next(gen))     # 12

    # Close the generator
    gen.close()          # Prints: "Dispenser closed."


if __name__ == "__main__":
    main()
