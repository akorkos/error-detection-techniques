msg = input("Δώσε εναν δυαδικό αριθμό (28-bit): ");

N = 4;
M = 7;
len = 28;

msgMatrix = zeros(N + 1, M + 1);

msgMatrix = createMatrix(msg, M, len);

msgMatrix = compute2dParity(msgMatrix, N, M);

disp(msgMatrix);