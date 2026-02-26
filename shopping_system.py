import json
import engine_core

DATA_FILE = "users_data.json"

# -----------------------------
# Reward Catalog (Gift Voucher Only)
# -----------------------------
REWARDS = {
    100: "50 THB Gift Voucher",
    250: "100 THB Gift Voucher",
    500: "250 THB Gift Voucher",
    1000: "500 THB Gift Voucher",
    2000: "1000 THB Gift Voucher"
}


# -----------------------------
# Load / Save Data
# -----------------------------
def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# -----------------------------
# Show Reward Catalog
# -----------------------------
def show_rewards():
    print("\n===== Gift Voucher Rewards =====")
    for points, reward in REWARDS.items():
        print(f"{points} points -> {reward}")


# -----------------------------
# Main Program
# -----------------------------
def main():
    data = load_data()

    print("===== Reward Shopping System (THB) =====")
    username = input("Enter your username: ")

    if username not in data:
        data[username] = {"points": 0}
        print("New user created.")

    while True:
        print("\n1. Purchase")
        print("2. Check Points")
        print("3. Redeem Gift Voucher")
        print("4. View Reward Catalog")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            amount = float(input("Enter purchase amount (THB): "))
            earned = engine_core.calculate_points(amount)
            data[username]["points"] += earned

            print(f"You earned {earned} points.")
            print(f"Total Points: {data[username]['points']}")

        elif choice == "2":
            print(f"Total Points: {data[username]['points']}")

        elif choice == "3":
            show_rewards()
            redeem = int(input("Enter points to redeem: "))

            if redeem in REWARDS and data[username]["points"] >= redeem:
                data[username]["points"] -= redeem
                print(f"Redeemed: {REWARDS[redeem]}")
                print(f"Remaining Points: {data[username]['points']}")
            else:
                print("Not enough points or invalid selection.")

        elif choice == "4":
            show_rewards()

        elif choice == "5":
            save_data(data)
            print("Data saved. Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()