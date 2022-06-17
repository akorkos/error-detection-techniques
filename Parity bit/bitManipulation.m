function msg = bitManipulation(msg, i, j)
  if (msg(i, j))
    msg(i, j) = 0;
  else
    msg(i, j) = 1;
  endif
endfunction