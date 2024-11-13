import csv
import tkinter as tk
from tkinter import messagebox

class PlayerStatsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NBA Player Statistics")
        
        # Instructions label
        self.label = tk.Label(root, text="Enter two player names and select their stat category (e.g., 'Steals', 'Scores', 'Rebounds'):")
        self.label.pack(padx=10, pady=5)
        
        # First player input and category selection
        self.textbox1_label = tk.Label(root, text="Player 1:")
        self.textbox1_label.pack()
        self.textbox1 = tk.Entry(root, font=('Georgia', 15), width=20)
        self.textbox1.pack(padx=10, pady=5)
        
        self.category1_label = tk.Label(root, text="Category 1:")
        self.category1_label.pack()
        self.category1_var = tk.StringVar(root)
        self.category1_var.set("Steals")  # default category
        self.category1_menu = tk.OptionMenu(root, self.category1_var, "Steals", "Scores", "Rebounds")
        self.category1_menu.pack(padx=10, pady=5)
        
        # Second player input and category selection
        self.textbox2_label = tk.Label(root, text="Player 2:")
        self.textbox2_label.pack()
        self.textbox2 = tk.Entry(root, font=('Georgia', 15), width=20)
        self.textbox2.pack(padx=10, pady=5)
        
        self.category2_label = tk.Label(root, text="Category 2:")
        self.category2_label.pack()
        self.category2_var = tk.StringVar(root)
        self.category2_var.set("Steals")  # default category
        self.category2_menu = tk.OptionMenu(root, self.category2_var, "Steals", "Scores", "Rebounds")
        self.category2_menu.pack(padx=10, pady=5)
        
        # Search button
        self.search_button = tk.Button(root, text="Search", command=self.search_players)
        self.search_button.pack(padx=10, pady=10)

    def read_csv_data(self, filename, player_name, category):
        # Define columns based on category
        columns = {
            "Steals": ["ID", "PlayerName", "GamesPlayed", "GamesStarted", "TotalSteals", "StealsPerGame"],
            "Scores": ["ID", "Name", "GamesPlayed", "GamesStarted", "MinutesPerGame", "PointsPerGame", 
                       "FieldGoalsMade", "FieldGoalsAttempted", "FieldGoalPercentage", 
                       "ThreePointFieldGoalsMade", "ThreePointFieldGoalsAttempted", "ThreePointFieldGoalPercentage", 
                       "FreeThrowsMade", "FreeThrowsAttempted", "FreeThrowsPercentage"],
            "Rebounds": ["ID", "PlayerName", "GamesPlayed", "GamesStarted", "MinutesPerGame", 
                         "OffensiveRebounds", "DefensiveRebounds", "TotalRebounds", "ReboundsPerGame"]
        }
        
        data = {col: [] for col in columns.get(category, [])}
        
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                # Ensure we only attempt to read columns that are present in this file
                for row in reader:
                    if row.get("PlayerName", "").strip() == player_name or row.get("Name", "").strip() == player_name:
                        for col in data.keys():
                            data[col].append(row.get(col, "N/A"))
                        break  # Stop after finding the first match
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except KeyError as e:
            print(f"Column not found in CSV file: {e}")
        
        return data

    def search_players(self):
        # Get player names and categories
        player_name1 = self.textbox1.get().strip()
        player_name2 = self.textbox2.get().strip()
        category1 = self.category1_var.get()
        category2 = self.category2_var.get()
        
        # Determine filenames based on category
        filename1 = f"nba-{category1}.csv"
        filename2 = f"nba-{category2}.csv"
        
        # Fetch data for each player
        player_data1 = self.read_csv_data(filename1, player_name1, category1)
        player_data2 = self.read_csv_data(filename2, player_name2, category2)
        
        # Display player data in the console
        if player_data1 and any(player_data1.values()):
            print(f"\nData for {player_name1} in {category1}:")
            for key, values in player_data1.items():
                print(f"{key}: {values[0]}")
        else:
            print(f"No data found for player '{player_name1}' in {category1}.")
            messagebox.showerror("Player Not Found", f"No data found for player '{player_name1}' in {category1}.")
        
        if player_data2 and any(player_data2.values()):
            print(f"\nData for {player_name2} in {category2}:")
            for key, values in player_data2.items():
                print(f"{key}: {values[0]}")
        else:
            print(f"No data found for player '{player_name2}' in {category2}.")
            messagebox.showerror("Player Not Found", f"No data found for player '{player_name2}' in {category2}.")

# Run the application
root = tk.Tk()
app = PlayerStatsApp(root)
root.mainloop()
