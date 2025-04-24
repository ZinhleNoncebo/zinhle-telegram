time_taken_for_triathlon=int(input("How many minutes did it take you to finish the triathlon?"))
if time_taken_for_triathlon<=100:
   print("Award: Provincial colours")
elif (time_taken_for_triathlon>=101) and (time_taken_for_triathlon<=105):
   print("Award: Provincial half colours")
elif (time_taken_for_triathlon)>=106 and (time_taken_for_triathlon<=110):
   print("Award: Provincial scroll")
else:
   print("No awards")