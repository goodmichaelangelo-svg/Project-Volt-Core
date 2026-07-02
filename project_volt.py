# Project Volt Core Protocol v1.0
neighborhood_grid = {
    "Enoch_Momoh": {"battery_percentage": 88, "role": "Seller"},
    "Neighbor_A": {"battery_percentage": 15, "role": "Buyer"},
    "Neighbor_B": {"battery_percentage": 42, "role": "Neutral"}
}

print("--- Project Volt: Scanning Grid Status ---")

for user, data in neighborhood_grid.items():
    if data["battery_percentage"] < 20:
        print(f"⚠️ ALERT: {user} is in darkness! Initiating automated P2P energy transfer...")
    elif data["battery_percentage"] > 80:
        print(f"🔋 STATUS: {user} has surplus energy available for the market")
        # Project Volt Automation Engine

def transfer_energy(seller, buyer, kilowatts_needed):
    """Handles the automated P2P energy transaction logic"""
    print(f"\n--- Initiating Transfer: {kilowatts_needed}kW from {seller} to {buyer} ---")
    
    # Simulate a transaction fee ($0.01) that builds your trillion-dollar revenue
    transaction_fee = 0.01
    
    print(f"⚡ Physical energy routed successfully via Project Volt hardware.")
    print(f"💰 Transaction complete. Fee of ${transaction_fee} deposited into Enoch's Wallet.")

# Triggering the function automatically when a buyer is found
transfer_energy(seller="Enoch_Momoh", buyer="Neighbor_A", kilowatts_needed=5)# Project Volt Core: Fintech & Wallet Logic

# Database simulating user cash balances in Naira or Digital Dollars
user_wallets = {
    "Enoch_Momoh": 1500.00,  # Your startup wallet balance
    "Neighbor_A": 5000.00,   # Buyer's wallet balance
    "System_Revenue": 0.00   # This tracks your transaction fee profits
}

def execute_automated_payment(seller, buyer, energy_cost):
    """Calculates and transfers funds automatically for the energy grid"""
    print(f"\n--- Processing Automated Billing: {seller} -> {buyer} ---")
    
    # Define your 1-cent transaction fee ($0.01 converted or flat unit)
    platform_fee = 10.00  
    total_buyer_deduction = energy_cost + platform_fee
    
    # Check if the buyer has enough money in their phone app
    if user_wallets[buyer] >= total_buyer_deduction:
        # Deduct money from buyer
        user_wallets[buyer] -= total_buyer_deduction
        # Add energy cost to your wallet (seller)
        user_wallets[seller] += energy_cost
        # Add the platform fee to your corporate revenue wallet
        user_wallets["System_Revenue"] += platform_fee
        
        print("✅ PAYMENT SUCCESSFUL: Ledger updated securely.")
        print(f"💰 Enoch's Personal Balance: ₦{user_wallets[seller]}")
        print(f"🚀 Project Volt Corporate Revenue: ₦{user_wallets['System_Revenue']}")
    else:
        print("❌ TRANSACTION DENIED: Insufficient wallet balance in buyer's app.")

# Project Volt Interactive Phone App Simulator

print("\n=============================================")
print("🤖 PROJECT VOLT: DECENTRALIZED APP ONLINE")
print("=============================================")

while True:
    print("\n[MAIN MENU]")
    print("1. View My Balance")
    print("2. Request Automated Energy P2P Transfer")
    print("3. Exit System")
    
    choice = input("\nEnter choice (1-3): ")
    
    if choice == "1":
        print(f"\n💳 Wallet Balance for Enoch_Momoh: ₦{user_wallets['Enoch_Momoh']}")
        print(f"📈 Total Company Platform Profits: ₦{user_wallets['System_Revenue']}")
        
    elif choice == "2":
        buyer_name = input("Enter Buyer Name (e.g., Neighbor_A): ")
        if buyer_name in user_wallets:
            try:
                amount = float(input("Enter value of electricity to transfer (₦): "))
                # Triggering your billing function using the live keyboard inputs
                execute_automated_payment(seller="Enoch_Momoh", buyer=buyer_name, energy_cost=amount)
            except ValueError:
                print("❌ Invalid amount entered. Please type a number.")
        else:
            print("❌ User not found in neighborhood database.")
            
    elif choice == "3":
        print("\n🔒 Shutting down Project Volt network core. Goodbye, CEO Enoch.")
        break
    else:
        print("❌ Invalid option. Select 1, 2, or 3.")


   