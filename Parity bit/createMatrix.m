function msgMatrix = createMatrix(msg, M, len)
  i = 1;
  j = 1;

  for k = 1 : len
    msgMatrix(i, j) = msg(k);
    if (mod(k, M) == 0)
      i = i + 1;
      j = 0;
    endif
    j = j + 1;
  endfor
endfunction