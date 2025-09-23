import csv
import matplotlib.pyplot as plt
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# -------------------------------
# Workout Data
# -------------------------------
workouts = []

# -------------------------------
# Functions
# -------------------------------
def add_workout(day, pushups, pullups, hiit_minutes, bodypart_trained, calories_burned):
    workout = {
        "day": day,
        "pushups": pushups,
        "pullups": pullups,
        "hiit_minutes": hiit_minutes,
        "bodypart_trained": bodypart_trained,
        "calories_burned": calories_burned
    }
    workouts.append(workout)
    console.print("[green]Workout added successfully![/green]")


def view_workouts():
    if not workouts:
        console.print("[red]No workouts logged yet.[/red]")
        return
    
    table = Table(title="Workout Log", header_style="bold magenta")
    for col in ["Day", "Pushups", "Pullups", "HIIT (min)", "Bodypart", "Calories"]:
        table.add_column(col, style="cyan")
    for w in workouts:
        table.add_row(str(w["day"]), str(w["pushups"]), str(w["pullups"]),
                      str(w["hiit_minutes"]), w["bodypart_trained"], str(w["calories_burned"]))
    console.print(table)


def weekly_summary():
    if not workouts:
        console.print("[red]No data to summarize.[/red]")
        return
    
    total_pushups = sum(w["pushups"] for w in workouts)
    total_pullups = sum(w["pullups"] for w in workouts)
    total_hiit = sum(w["hiit_minutes"] for w in workouts)
    total_calories = sum(w["calories_burned"] for w in workouts)
    days = len(workouts)

    console.print(Panel.fit(
        f"[bold yellow]--- Weekly Summary ---[/bold yellow]\n"
        f"Days tracked: {days}\n"
        f"Total Pushups: {total_pushups}\n"
        f"Total Pullups: {total_pullups}\n"
        f"Total HIIT minutes: {total_hiit}\n"
        f"Total Calories burned: {total_calories}\n"
        f"Average Pushups per day: {total_pushups // days}\n"
        f"Average Calories per day: {total_calories // days}",
        border_style="blue"
    ))


def ai_tips():
    if not workouts:
        console.print("[red]No data available for AI tips yet.[/red]")
        return
    
    last = workouts[-1]
    tips = []
    if last["pushups"] < 300:
        tips.append("Try increasing your pushups to build endurance.")
    if last["hiit_minutes"] < 15:
        tips.append("Add at least 15 mins of HIIT for fat burn.")
    if last["calories_burned"] < 500:
        tips.append("Push harder to burn more than 500 calories.")
    
    if not tips:
        tips.append("Great work! Keep consistency for long-term gains.")
    
    console.print(Panel("\n".join(tips), title="💡 AI Workout Tips", border_style="green"))


def save_workouts_to_csv(filename="workouts.csv"):
    if not workouts:
        console.print("[red]No workouts to save![/red]")
        return
    fieldnames = ["day", "pushups", "pullups", "hiit_minutes", "bodypart_trained", "calories_burned"]
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for w in workouts:
            writer.writerow(w)
    console.print(f"[green]Workouts saved to {filename}[/green]")


def load_workouts_from_csv(filename="workouts.csv"):
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                workouts.append({
                    "day": row["day"],
                    "pushups": int(row["pushups"]),
                    "pullups": int(row["pullups"]),
                    "hiit_minutes": int(row["hiit_minutes"]),
                    "bodypart_trained": row["bodypart_trained"],
                    "calories_burned": int(row["calories_burned"])
                })
        console.print(f"[cyan]Loaded workouts from {filename}[/cyan]")
    except FileNotFoundError:
        console.print("[red]No CSV file found yet. Start by adding workouts![/red]")


def show_graphs():
    if not workouts:
        console.print("[red]No data to plot.[/red]")
        return
    
    days = [w["day"] for w in workouts]
    calories = [w["calories_burned"] for w in workouts]
    pushups = [w["pushups"] for w in workouts]

    plt.figure(figsize=(8, 5))
    plt.plot(days, calories, marker="o", label="Calories Burned")
    plt.plot(days, pushups, marker="s", label="Pushups")
    plt.title("Workout Progress")
    plt.xlabel("Day")
    plt.ylabel("Count")
    plt.legend()
    plt.show()

# -------------------------------
# Menu
# -------------------------------
def main_menu():
    console.print(Panel.fit("[bold cyan]🏋️ Fitness Tracker Menu 🏋️[/bold cyan]", border_style="green"))

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Option", style="cyan", width=8)
    table.add_column("Action", style="yellow")

    table.add_row("1", "Add Workout")
    table.add_row("2", "View Workouts")
    table.add_row("3", "Weekly Summary")
    table.add_row("4", "AI Tips")
    table.add_row("5", "Save to CSV")
    table.add_row("6", "Load from CSV")
    table.add_row("7", "Show Graphs")
    table.add_row("0", "Exit")

    console.print(table)
    return console.input("\n[bold green]Enter your choice:[/bold green] ")


# -------------------------------
# Main Loop
# -------------------------------
if __name__ == "__main__":
    while True:
        choice = main_menu()
        if choice == "1":
            day = console.input("Enter day: ")
            pushups = int(console.input("Enter pushups: "))
            pullups = int(console.input("Enter pullups: "))
            hiit = int(console.input("Enter HIIT minutes: "))
            bodypart = console.input("Enter bodypart trained: ")
            calories = int(console.input("Enter calories burned: "))
            add_workout(day, pushups, pullups, hiit, bodypart, calories)
        elif choice == "2":
            view_workouts()
        elif choice == "3":
            weekly_summary()
        elif choice == "4":
            ai_tips()
        elif choice == "5":
            save_workouts_to_csv()
        elif choice == "6":
            load_workouts_from_csv()
        elif choice == "7":
            show_graphs()
        elif choice == "0":
            console.print("[bold red]Exiting... Goodbye![/bold red]")
            break
        else:
            console.print("[red]Invalid choice. Please try again.[/red]")
