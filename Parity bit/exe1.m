msg = input("Δώσε εναν δυαδικό αριθμό (14-bit): ");
N = length(msg);

while (N ~= 14)
  msg = input("Δώσε εναν δυαδικό αριθμό (14-bit): ");
  N = length(msg);
end

msg = computeParity(msg);

disp("Το μήνυμα μαζί με το bit ισοτιμίας είναι: "), disp(msg)