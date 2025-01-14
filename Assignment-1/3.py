# Q3. If the marks obtained by a student in five different subjects are input through the keyboard, 
# find out the aggregate marks and percentage marks obtained by the student. Assume that the 
# maximum marks that can be obtained by a student in each subject is 100. 
sub1_maths = float(input("Enter marks obtained in Mathematics(100 marks): "));
sub2_science = float(input("Enter marks obtained in Science(100 marks): "));
sub3_english = float(input("Enter marks obtained in English(100 marks): "));
sub4_computer = float(input("Enter marks obtained in Computer(100 marks): "));
sub5_economics = float(input("Enter marks obtained in Economics(100 marks): "));

aggregate_marks = sub1_maths + sub2_science + sub3_english + sub4_computer + sub5_economics;
print(f"Total marks obtained by the student : {aggregate_marks}")

percentage = (aggregate_marks / 500) * 100;
print(f"Percentage score by the student: {percentage}");