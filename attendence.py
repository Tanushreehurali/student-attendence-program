import sys


if len(sys.argv) == 3:
    script_name = sys.argv[0]
    classes_held = int(sys.argv[1])
    classes_attended = int(sys.argv[2])
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    classes_held = 40        
    classes_attended = 32   
    print("No input given — using default values:")


attendance = (classes_attended / classes_held) * 100


print("Script Name:", script_name)
print("Classes Held:", classes_held)
print("Classes Attended:", classes_attended)
print("Attendance Percentage:", attendance, "%")
