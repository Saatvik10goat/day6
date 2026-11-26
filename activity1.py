print("=== Smart School Day Planner ===")
print("Answer three quick question and i will plan ur day!/n")

day=input("What day is it (Monday:Sunday)").strip().capitalize()
weather=input("What is the weather (sunny/rainy/cloudy)").strip().lower()
homework=input("Are u done with ur homework (yes/no)").strip().lower()

print()
print(f"===ur plan for {day}===")
print("-"*35)

if day in("Saturday","Sunday"):
    print("Day type: Enjoy ur weekend")
elif day=="Monday":
    print("First day of the week plack your weekly planner")
elif day=="Friday":
    print("Last day of school. Return library books")
elif day in("Tuesday","Wednesday","Thursday"):
    print("Regular school day.Saty focused and wait for weekend!")
else:
    print("Day type: not detected enter proper day")

if weather=="sunny"and homework=="yes":
    print("After school.Go to the park the weather is sunny and ur H.W is done!")
if weather=="yes" or weather=="cloudy":
    print("Carry an umbrella it may get wet outside.")
if not(homework=="yes"):
    print("Homework not done yet. Complete it before going out!")
elif weather=="rainy" and not(homework=="yes"):
    print("Best plan: Stay in complete ur homework and watch ur favourite show.")
elif day in("Saturday","Sunday"):
    print("Perfect weekend weather. Head outside and play.")
else:
    print("Take it one step at a time-You have got this!")

print()
print("Plan Complete!Have A wonderful time")