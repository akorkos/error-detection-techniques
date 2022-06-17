msg = input("Δώσε εναν δυαδικό αριθμό (14-bit): ");
N = length(msg);

while (N ~= 14)
  msg = input("Δώσε εναν δυαδικό αριθμό (14-bit): ");
  N = length(msg);
endwhile

msg = computeParity(msg);

if (validateParity(msg))
  disp("Το μήνυμα δεν έχει υποστεί αλλοίωση.");
else
  disp("Το μήνυμα έχει υποστεί αλλοίωση.");
endif

msg = bitManipulation(msg, 1, 6);

if (validateParity(msg))
  disp("Το μήνυμα δεν έχει υποστεί αλλοίωση.");
else
  disp("Το μήνυμα έχει υποστεί αλλοίωση.");
endif

msg = bitManipulation(msg, 1, 12);

if (validateParity(msg))
  disp("Το μήνυμα δεν έχει υποστεί αλλοίωση.");
else
  disp("Το μήνυμα έχει υποστεί αλλοίωση.");
endif