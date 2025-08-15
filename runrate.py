total_no_of_balls = int(input("Total number of balls: "))
total_no_of_runs = int(input("Total number of runs: "))
no_of_runs_scored = int(input("Number of runs scored: "))
no_of_balls_bowled = int(input("Number of balls bowled: "))

total_no_of_overs = total_no_of_balls // 6
total_no_of_overs_finished = no_of_balls_bowled / 6
current_run_rate = no_of_runs_scored // total_no_of_overs_finished
total_run_rate = total_no_of_runs / total_no_of_overs

print(f"Total overs: {total_no_of_overs}")
print(f"Overs finished: {total_no_of_overs_finished}")
print(f"Current run rate: {current_run_rate:.2f}")
print(f"Required run rate: {total_run_rate:.2f}")

if current_run_rate > total_run_rate:
    print("Eligible to win")
else:
    print("Not eligible to win")
