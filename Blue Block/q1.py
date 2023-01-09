#define the Renter Class

class Renter(object):
  def __init__(self, name, room_number, days_booked):
    init = ''
    while(init!=f'X'):
      print("Make a Selection:\nRent a Room (R), Check Out (C), Print Motel Details (P), Exit Program (X)")
      init = input()
      init.lower()
      if(init == f'x'):
        break
   rent_room()